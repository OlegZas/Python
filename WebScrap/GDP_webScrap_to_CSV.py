import pandas as pd 
import sqlite3
from bs4 import BeautifulSoup
import requests 
import logging
from datetime import datetime

# 1. Configure Logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s : %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

url = "https://web.archive.org/web/20230902185326/https://en.wikipedia.org/wiki/List_of_countries_by_GDP_%28nominal%29"
db_name = "Countries.db"
table_name = "Countries"
csv_path = "countries.csv"

logging.info("Preliminaries complete. Initiating ETL process")

# 2. Extraction
data_list = []
try:
    html_page = requests.get(url).text
    data = BeautifulSoup(html_page, 'html.parser')
    tables = data.find_all('tbody')
    # The GDP data is in the 3rd table (index 2)
    rows = tables[2].find_all('tr') 
    logging.info("Data extraction complete. Initiating Transformation process")
except Exception as e:
    logging.error(f"Extraction failed: {e}")
    exit()

# 3. Transformation
for row in rows:
    col = row.find_all('td')
    if len(col) >= 3:
        country = col[0].get_text(strip=True)
        gdp_raw = col[2].get_text(strip=True)
        
        if gdp_raw and '—' not in gdp_raw:
            try:
                # Remove commas and handle potential text issues
                clean_gdp = gdp_raw.replace(',', '')
                
                # Check if it's a valid number before converting
                if clean_gdp.replace('.', '', 1).isdigit():
                    gdp_val = float(clean_gdp)
                    
                    # Filter: GDP >= 100 Billion (100,000 Million)
                    if gdp_val >= 100000:
                        data_list.append({
                            "Country": country, 
                            "GDP_USD_Billions": round(gdp_val/1000, 2)
                        })
            except ValueError:
                # This catches rows that aren't numbers (like the 'billion' text)
                continue

# Create DataFrame
df = pd.DataFrame(data_list)
print(df) # Show the result in terminal
logging.info("Data transformation complete. Initiating loading process")

# 4. Loading
try:
    # Save to CSV
    df.to_csv(csv_path, index=False)
    
    # Save to SQL
    conn = sqlite3.connect(db_name)
    df.to_sql(table_name, conn, if_exists='replace', index=False)
    conn.close()
    
    logging.info("Data loaded to Database and CSV. ETL Process Complete.")
except Exception as e:
    logging.error(f"Loading failed: {e}")

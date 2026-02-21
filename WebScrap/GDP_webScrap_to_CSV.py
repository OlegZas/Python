import pandas as pd 
import sqlite3
from bs4 import BeautifulSoup
import requests 
import logging
import sys

# --- Professional Logger Setup (File + Console) ---
logger = logging.getLogger()
logger.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s : %(message)s', '%Y-%m-%d %H:%M:%S')

# 1. File Handler (Appends to etl_project_log.txt)
file_handler = logging.FileHandler('etl_project_log.txt')
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

# 2. Console Handler (Prints to your terminal)
console_handler = logging.StreamHandler()
console_handler.setFormatter(formatter)
logger.addHandler(console_handler)

# --- Configuration ---
url = "https://web.archive.org/web/20230902185326/https://en.wikipedia.org/wiki/List_of_countries_by_GDP_%28nominal%29"
db_name = "Countries.db"
table_name = "Countries"
csv_path = "countries.csv"
headers = {"User-Agent": "Mozilla/5.0"}

logging.info("Preliminaries complete. Initiating ETL process")

# --- 1. Extraction ---
data_list = []
try:
    logging.info("Fetching webpage... (Waiting for Archive.org)")
    response = requests.get(url, headers=headers, timeout=30)
    response.raise_for_status()
    
    data = BeautifulSoup(response.text, 'html.parser')
    tables = data.find_all('tbody')
    # The GDP data is in the 3rd table (index 2)
    rows = tables[2].find_all('tr') 
    logging.info("Data extraction complete. Initiating Transformation process")
except Exception as e:
    logging.error(f"Extraction failed: {e}")
    sys.exit()

# --- 2. Transformation ---
for row in rows:
    col = row.find_all('td')
    if len(col) >= 3:
        country = col[0].get_text(strip=True)
        gdp_raw = col[2].get_text(strip=True)
        
        if gdp_raw and '—' not in gdp_raw:
            try:
                # Remove commas
                clean_gdp = gdp_raw.replace(',', '')
                
                # Check if valid number (skips legend text)
                if clean_gdp.replace('.', '', 1).isdigit():
                    gdp_val = float(clean_gdp)
                    
                    # Filter: GDP >= 100 Billion
                    if gdp_val >= 100000:
                        data_list.append({
                            "Country": country, 
                            "GDP_USD_Billions": round(gdp_val/1000, 2)
                        })
            except ValueError:
                continue

# Create DataFrame (preserves append order)
df = pd.DataFrame(data_list)
logging.info("Data transformation complete. Initiating loading process")

# --- 3. Loading ---
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

# Final Terminal Output
print("\n--- Processed Data ---")
print(df.head())

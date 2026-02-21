#Countries_by_GDP.csv
import pandas as pd 
import sqlite3
from bs4 import BeautifulSoup
import requests 

url="https://web.archive.org/web/20230902185326/https://en.wikipedia.org/wiki/List_of_countries_by_GDP_%28nominal%29"
db_name = "Countries.db"
table_name = "Countries"
csv_path = "countries.csv"

# Initialize list to store data (more efficient than appending to DF)
data_list = []

html_page = requests.get(url).text
data = BeautifulSoup(html_page, 'html.parser')

# The GDP data is in the 3rd table on this specific archived page
tables = data.find_all('tbody')
rows = tables[2].find_all('tr') 

for row in rows:
    col = row.find_all('td')
    # Ensure the row has enough columns (Country is usually col 0, IMF GDP is col 2)
    if len(col) >= 3:
        country = col[0].get_text(strip=True)
        gdp_raw = col[2].get_text(strip=True)
        
        # Clean the GDP string (remove commas and handle non-numeric data)
        if gdp_raw and '—' not in gdp_raw:
            gdp_val = float(gdp_raw.replace(',', ''))
            
            # Filter: GDP >= 100 Billion (Table is in Millions, so 100,000)
            if gdp_val >= 100000:
                data_list.append({"Country": country, "GDP_USD_Millions": gdp_val})

# Create DataFrame once at the end
df = pd.DataFrame(data_list)
print(df)

# Save to CSV and SQL
df.to_csv(csv_path, index=False)
conn = sqlite3.connect(db_name)
df.to_sql(table_name, conn, if_exists='replace', index=False)
conn.close()

import requests
import sqlite3
import pandas as pd
import numpy as np
from bs4 import BeautifulSoup
from datetime import datetime

# Configuration
url = 'https://web.archive.org/web/20230908091635/https://en.wikipedia.org/wiki/List_of_largest_banks'
db_name = 'Banks.db'
table_name = 'Largest_banks'
csv_path = './Largest_banks_data.csv'
exchange_rate_path = './exchange_rate.csv'

def log_progress(message):
    '''Logs the progress of the code at different stages.'''
    timestamp_format = '%Y-%m-%d-%H:%M:%S'
    now = datetime.now()
    timestamp = now.strftime(timestamp_format)
    with open("code_log.txt", "a") as f:
        f.write(f"{timestamp} : {message}\n")

def extract(url):
    '''Scrapes the top 10 banks by market capitalization from Wikipedia.'''
    html_page = requests.get(url).text
    data = BeautifulSoup(html_page, 'html.parser')
    df = pd.DataFrame(columns=["Name", "MC_USD_Billion"])
    
    # Locate the table under "By market capitalization"
    tables = data.find_all('tbody')
    rows = tables[0].find_all('tr') # Index 0 usually holds the relevant table in this archive

    for row in rows:
        col = row.find_all('td')
        if len(col) != 0:
            # Extract Bank Name and Market Cap (stripping newlines and extra chars)
            bank_name = col[1].get_text(strip=True)
            market_cap = float(col[2].get_text(strip=True).replace(',', ''))
            new_row = {"Name": bank_name, "MC_USD_Billion": market_cap}
            df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)
            
    return df.head(10) # We only need the Top 10

def transform(df, csv_path):
    '''Adds currency converted columns based on exchange rates.'''
    # Read exchange rate CSV (Expected columns: Currency, Rate)
    exchange_df = pd.read_csv(csv_path)
    rates = exchange_df.set_index('Currency').to_dict()['Rate']
    
    # Calculate new columns rounded to 2 decimal places
    df['MC_GBP_Billion'] = [np.round(x * rates['GBP'], 2) for x in df['MC_USD_Billion']]
    df['MC_EUR_Billion'] = [np.round(x * rates['EUR'], 2) for x in df['MC_USD_Billion']]
    df['MC_INR_Billion'] = [np.round(x * rates['INR'], 2) for x in df['MC_USD_Billion']]
    
    return df

def load_to_csv(df, output_path):
    df.to_csv(output_path, index=False)

def load_to_db(df, sql_connection, table_name):
    df.to_sql(table_name, sql_connection, if_exists='replace', index=False)

def run_queries(query_statement, sql_connection):
    print(query_statement)
    query_output = pd.read_sql(query_statement, sql_connection)
    print(query_output)

# --- Execution Flow ---

log_progress('Preliminaries complete. Initiating ETL process')

df = extract(url)
log_progress('Data extraction complete. Initiating Transformation process')

df = transform(df, exchange_rate_path)
log_progress('Data transformation complete. Initiating Loading process')

load_to_csv(df, csv_path)
log_progress('Data saved to CSV file')

sql_connection = sqlite3.connect(db_name)
log_progress('SQL Connection initiated')

load_to_db(df, sql_connection, table_name)
log_progress('Data loaded to Database as a table, Executing queries')

# Example Query
run_queries(f"SELECT * FROM {table_name} WHERE MC_USD_Billion > 100", sql_connection)
log_progress('Process Complete')

sql_connection.close()
log_progress('Server Connection closed')
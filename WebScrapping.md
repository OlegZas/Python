# Web Scraping and Data Extraction Pipeline

This guide outlines the process of extracting high-ranking film data from a web source, processing it with Pandas, and persisting it to both CSV and SQLite.

<img width="706" height="245" alt="image" src="https://github.com/user-attachments/assets/6eb3984b-af3b-4279-87b6-31c271cbbfdb" />

---

## 1. Install Dependencies
Ensure you have the necessary libraries installed in your environment.

> pip install pandas beautifulsoup4 requests

<img width="975" height="411" alt="image" src="https://github.com/user-attachments/assets/0e3dcc39-2d1c-497b-9a65-ff5b232096b0" />

---

## 2. Import Libraries
Import the core modules for web requests, HTML parsing, and data management.

> import requests
> import pandas as pd
> from bs4 import BeautifulSoup
> import sqlite3

<img width="817" height="306" alt="image" src="https://github.com/user-attachments/assets/2d244591-47de-43bc-a070-335f6e071223" />

---

## 3. Declare Variables
Define the environment properties, including the target URL and local storage paths.

> url = 'https://web.archive.org/web/20230902185655/https://en.everybodywiki.com/100_Most_Highly-Ranked_Films'
> db_name = 'Movies.db'
> table_name = 'Top_50'
> csv_path = '/home/project/top_50_films.csv'
> df = pd.DataFrame(columns=["Average Rank", "Film", "Year"])
> count = 0

---
## 3.5 Load page as HTML and parse. 
- Use requests.get(url).text function to load the web page as HTML document and then parse the text with BeautifulSoup. 

<img width="975" height="418" alt="image" src="https://github.com/user-attachments/assets/f56b9462-a52e-422d-a53b-092e7831d801" />

## 4. Fetch and Parse Content
Load the webpage content as an HTML document and initialize the BeautifulSoup parser.

> html_page = requests.get(url).text
> data = BeautifulSoup(html_page, 'html.parser')

<img width="975" height="449" alt="image" src="https://github.com/user-attachments/assets/2d7d11a8-e7b0-4dbd-ac73-8ac72c9dadd8" />

---

## 5. Locate Table Body
Navigate the HTML tree to find the specific table data.

> tables = data.find_all('tbody')
> rows = tables[0].find_all('tr')

---

## 6. Iterate and Extract Data
Loop through the table rows, extract the relevant columns, and append them to the DataFrame.

> for row in rows:
>     if count < 50:
>         col = row.find_all('td')
>         if len(col) != 0:
>             data_dict = {"Average Rank": col[0].contents[0],
>                          "Film": col[1].contents[0],
>                          "Year": col[2].contents[0]}
>             df1 = pd.DataFrame(data_dict, index=[0])
>             df = pd.concat([df, df1], ignore_index=True)
>             count += 1
>     else:
>         break

<img width="975" height="729" alt="image" src="https://github.com/user-attachments/assets/25d5020b-b31c-4d98-81d6-6d8d285b5a59" />

---

## 7. Data Persistence
Save the processed data to a local CSV file and an SQLite3 database.

### Save to CSV
> df.to_csv(csv_path)

### Save to SQL Database
> conn = sqlite3.connect(db_name)
> df.to_sql(table_name, conn, if_exists='replace', index=False)
> conn.close()

<img width="799" height="515" alt="image" src="https://github.com/user-attachments/assets/e08abb32-61da-4d37-9fe6-340d12de1c2b" />

---

## 8. Run the Script
Execute the script from your terminal to begin the extraction.

> python movie_scraper.py

<img width="975" height="879" alt="image" src="https://github.com/user-attachments/assets/cff03046-344e-44ee-bdc9-bac41b36db4d" />

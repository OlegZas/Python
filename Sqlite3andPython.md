#  Database Management with SQLite3 and Pandas

This guide demonstrates how to load data into a SQL database, perform queries, and append new records using Python.

---

##  1. Environment Setup
Install the required data manipulation library using the specific Python version.

> python3.11 -m pip install pandas

---

##  2. Import Libraries
Load the modules necessary for database interaction and data framing.

> import sqlite3
> import pandas as pd

---

##  3. Database Connection
Initialize and connect to the SQLite database file.

> conn = sqlite3.connect('STAFF.db')

---

##  4. Define Metadata
Set the target table name and the required attributes/columns.

> table_name = 'INSTRUCTOR'
> attribute_list = ['ID', 'FNAME', 'LNAME', 'CITY', 'CCODE']

---

##  5. Load Data to SQL
Use the Pandas `to_sql` method to push the DataFrame content into the database.

> df.to_sql(table_name, conn, if_exists='replace', index=False)
> print('Table is ready')

---

##  6. Execute Queries
Run SQL queries to verify data integrity and retrieve specific information.

### Select All Records
> query_statement = f"SELECT * FROM {table_name}"
> query_output = pd.read_sql(query_statement, conn)
> print(query_statement)
> print(query_output)

### Select Specific Column
> query_statement = f"SELECT FNAME FROM {table_name}"
> query_output = pd.read_sql(query_statement, conn)
> print(query_statement)
> print(query_output)

---

##  7. Append New Data
Create a new data record and append it to the existing SQL table.

> data_dict = {'ID' : [100],
>              'FNAME' : ['John'],
>              'LNAME' : ['Doe'],
>              'CITY' : ['Paris'],
>              'CCODE' : ['FR']}
> data_append = pd.DataFrame(data_dict)
> data_append.to_sql(table_name, conn, if_exists='append', index=False)
> print('Data appended successfully')

---

## 8. Terminate Connection
Always close the connection to prevent database locks or memory leaks.

> conn.close()

<img width="931" height="1038" alt="image" src="https://github.com/user-attachments/assets/788affa3-b594-4d21-ad83-48e13ce52762" />

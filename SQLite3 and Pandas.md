## Working with SQLite3 and Pandas

**SQLite3** is a *serverless, zero-configuration* database engine.  
Unlike traditional databases (like MySQL or PostgreSQL), it **does not require a separate server** — the entire database is stored as a **single file** on your disk.

---

## 1. Establishing a Connection

To interact with a database, you first need to create a **connection object**.  
This object acts as the bridge between your Python script and the database file.

> Python

> import sqlite3  
>  
> # Creates 'my_data.db' if it doesn't exist, or opens it if it does  
> connection = sqlite3.connect('my_data.db')

---

## 2. Loading Data (Pandas → SQLite)

The **`to_sql()`** method allows you to export a DataFrame directly into a database table.  
This is **much faster** than writing manual INSERT statements.

> Python

> df.to_sql('employees', connection, if_exists='replace', index=False)

### Key Parameters

**if_exists**
- `'fail'` → Stops if the table already exists  
- `'replace'` → Drops the old table and creates a new one  
- `'append'` → Adds new rows to the existing table  

**index**
- Set to **False** to prevent Pandas from saving row numbers as a column

---

## 3. Fetching Data (SQLite → Pandas)

To retrieve data, use **`read_sql()`**.  
This executes a SQL query and automatically returns results as a Pandas DataFrame.

> Python

> import pandas as pd  
>  
> query = "SELECT * FROM employees WHERE department = 'Sales'"  
> df_sales = pd.read_sql(query, connection)

---

## Common SQL Query Cheat Sheet

| Query | Purpose | Example |
|------|---------|---------|
| `SELECT *` | Get all data | SELECT * FROM users |
| `SELECT COUNT(*)` | Count rows | SELECT COUNT(*) FROM orders |
| `SELECT col_name` | Get specific columns | SELECT email FROM leads |
| `WHERE` | Filter results | SELECT * FROM products WHERE price > 50 |
| `LIMIT` | Restrict output size | SELECT * FROM logs LIMIT 5 |

---

## Important: Closing the Connection

Always close the connection when finished to prevent data corruption or memory leaks.

> Python

> connection.close()

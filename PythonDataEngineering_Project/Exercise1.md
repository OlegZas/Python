# Practice Exercises

Follow the process learned in this lab to perform ETL operations on the data available in the link below.

Data source link:  
"https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0221EN-SkillsNetwork/labs/module%206/Lab%20-%20Extract%20Transform%20Load/data/datasource.zip"

---

## Instructions

1. **Create a folder and Python file**  
   - Create a folder called `data_source` and change the current directory to it:  
     "mkdir -p /home/project/data_source"  
     "cd /home/project/data_source"  
   - Create a Python file for ETL practice:  
     "touch etl_practice.py"

2. **Download and unzip the data**  
   - Download the data from the link above  
     "wget <data_source_link>"  
   - Unzip the downloaded file  
     "unzip datasource.zip"

3. **Inspect the data**  
   - The data contains four headers:  
     `'car_model', 'year_of_manufacture', 'price', 'fuel'`

4. **Extraction**  
   - Implement extraction functions for:  
     - CSV files  
     - JSON files  
     - XML files

5. **Transformation**  
   - Transform the values under the `'price'` column so they are rounded to 2 decimal places

6. **Loading**  
   - Implement a function to save the transformed data to a target file:  
     `"transformed_data.csv"`

7. **Logging**  
   - Implement a logging function for the ETL process  
   - Save logs to: `"log_file.txt"`

8. **Testing**  
   - Test all implemented functions and log events as done in the lab

---

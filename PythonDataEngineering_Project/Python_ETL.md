# ETL Lab Instructions

## 1. Download Data

In a shell of your IDE, run the following to download the zip file containing data in multiple formats:

# wget https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0221EN-SkillsNetwork/labs/module%206/Lab%20-%20Extract%20Transform%20Load/data/source.zip

## 2. Unzip the File

# unzip source.zip
<img width="848" height="873" alt="image" src="https://github.com/user-attachments/assets/0de82212-15da-4df6-9c6a-8a31655cbe5a" />

## 3. Parse Information from Files

1. Install Pandas library:

# python3.11 -m pip install pandas

2. Import required libraries:

# import glob
# import pandas as pd
# import xml.etree.ElementTree as ET
# from datetime import datetime

3. Parsing different file types:
   - Use `xml.etree.ElementTree` to parse `.xml` files
   - Use `pandas` to read `.csv` and `.json` files
   - Use `glob` to access file info and call the correct extraction function
   - Use `datetime` to get current date/time for logging

## 4. Set File Paths

# log_file = "log_file.txt"
# target_file = "transformed_data.csv"

## 5. Develop Extraction Functions

- Create separate functions to extract data from `.csv`, `.json`, and `.xml` files.
<img width="801" height="856" alt="image" src="https://github.com/user-attachments/assets/3f7ad85a-ca6d-4c1e-a247-971f20430a0c" />

## 6. Identify File Type

- Implement a function to determine which extraction function to use based on the file type.
<img width="476" height="653" alt="image" src="https://github.com/user-attachments/assets/ba657971-4e4a-42ad-9827-916f4b09f835" />

## 7. Transform the Data

- Convert height to meters and weight to kilograms.
<img width="541" height="248" alt="image" src="https://github.com/user-attachments/assets/7a08f433-f60f-494b-9a07-69d67ef4e806" />

## 8. Load Function

- Create a function to load the transformed data into the target file.
<img width="517" height="107" alt="image" src="https://github.com/user-attachments/assets/215f5f69-1888-488a-bbc0-3e2c9ecac148" />

## 9. Logging Function

- Implement a function to log messages into the log file.
<img width="489" height="214" alt="image" src="https://github.com/user-attachments/assets/528e7469-35da-4d62-947b-e69448ba5825" />

## 10. Main Method

- Call all the above functions in a main method to run the ETL pipeline.
<img width="553" height="629" alt="image" src="https://github.com/user-attachments/assets/272b06df-720c-461c-a294-8a14828d1a34" />

## 11. ETL Code Result

- The output of the ETL process (transformed data) will be stored in `transformed_data.csv`.
<img width="656" height="997" alt="image" src="https://github.com/user-attachments/assets/29fcc8a2-fb72-4054-96e0-e50564332331" />

## 12. Log File Result

- All log messages will be stored in `log_file.txt`.

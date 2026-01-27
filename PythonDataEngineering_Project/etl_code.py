import glob
import pandas as pd
import xml.etree.ElementTree as ET
from datetime import datetime


log_file = "log_file.txt"
target_file = "transformed_data.csv"


# ---------------- LOG FUNCTION ----------------
def log_progress(message):
    timestamp_format = '%Y-%m-%d-%H:%M:%S'
    now = datetime.now()
    timestamp = now.strftime(timestamp_format)

    with open(log_file, "a") as f:
        f.write(timestamp + ',' + message + '\n')


# ---------------- EXTRACT FUNCTIONS ----------------
def extract_from_csv(file_to_process):
    dataframe = pd.read_csv(file_to_process)
    return dataframe


def extract_from_json(file_to_process):
    dataframe = pd.read_json(file_to_process, lines=True)
    return dataframe


def extract_from_xml(file_to_process):

    dataframe = pd.DataFrame(columns=["name", "height", "weight"])

    tree = ET.parse(file_to_process)
    root = tree.getroot()

    for person in root:
        name = person.find("name").text
        height = float(person.find("height").text)
        weight = float(person.find("weight").text)

        row = {
            "name": name,
            "height": height,
            "weight": weight
        }

        dataframe = pd.concat(
            [dataframe, pd.DataFrame([row])],
            ignore_index=True
        )

    return dataframe


def extract():

    extracted_data = pd.DataFrame(
        columns=["name", "height", "weight"]
    )

    # CSV files
    for csvfile in glob.glob("*.csv"):
        if csvfile != target_file:
            df = extract_from_csv(csvfile)
            extracted_data = pd.concat(
                [extracted_data, df],
                ignore_index=True
            )

    # JSON files
    for jsonfile in glob.glob("*.json"):
        df = extract_from_json(jsonfile)
        extracted_data = pd.concat(
            [extracted_data, df],
            ignore_index=True
        )

    # XML files
    for xmlfile in glob.glob("*.xml"):
        df = extract_from_xml(xmlfile)
        extracted_data = pd.concat(
            [extracted_data, df],
            ignore_index=True
        )

    return extracted_data


# ---------------- TRANSFORM ----------------
def transform(data):

    # inches → meters
    data["height"] = round(data["height"] * 0.0254, 2)

    # pounds → kg
    data["weight"] = round(data["weight"] * 0.45359237, 2)

    return data


# ---------------- LOAD ----------------
def load_data(target_file, transformed_data):
    transformed_data.to_csv(target_file, index=False)


# ---------------- MAIN ETL PROCESS ----------------
def main():

    log_progress("ETL Job Started")

    # Extract
    log_progress("Extract phase Started")
    extracted_data = extract()
    log_progress("Extract phase Ended")

    # Transform
    log_progress("Transform phase Started")
    transformed_data = transform(extracted_data)

    print("Transformed Data:")
    print(transformed_data)

    log_progress("Transform phase Ended")

    # Load
    log_progress("Load phase Started")
    load_data(target_file, transformed_data)
    log_progress("Load phase Ended")

    log_progress("ETL Job Ended")


# Run program
if __name__ == "__main__":
    main()

'''Exercise 3
Create a function 'parse_data' that takes in a json file (provided) loads it, and
returns the result.

In this case the students.json file contains the following content:
 {
   "students": [
     {"name": "Alice", "age": 20},
     {"name": "Bob", "age": 22},
     {"name": "Charlie", "age": 21}
   ]
 }

To validate, load the json file into the colab session files and run your function.
It should return a dictionary with these elements.

Include error handling, and a specific FileNotFoundError exception that if triggered
returns "File '{json_file}' not found."

'''

import json

#function here
def parse_data(json_file):
    """
    Loads and parses a JSON file into a Python dictionary with error handling.
    """
    try:
        with open(json_file, 'r') as file:
            data = json.load(file)
        return data
    except FileNotFoundError:
        return f"File '{json_file}' not found."
    except json.JSONDecodeError:
        return "Error: The file is not a valid JSON format."
    except Exception:
        return "An error occurred while parsing the data."


# Parse and print student data
result = parse_data("students.json")
assert result['students'][0]['name'] == 'Alice'
assert parse_data("testing.json") == "File 'testing.json' not found."


print("Exercise 3 is correct.")
total_score += 4
''' Exercise 1
Define a function 'pickle_data' that takes in two inputs: data, and filename

The function should read in the data and dump it into a pickle file named the
filename input.

For complete credit, wrap the pickling in a try/except codeblock to ensure it functions
robustly. If an exception is raised, have it return: 'An error occurred while pickling the data.'
'''

import pickle


def pickle_data(data, filename):
    try:
        with open(filename, 'wb') as file:
            pickle.dump(data, file)
        return f"Data pickled successfully to '{filename}'"
    except Exception:
        return "An error occurred while pickling the data."


# Sample problem: Storing information about books
books_info = {
    '001': {'title': 'Python Programming', 'author': 'John Doe', 'year': 2020},
    '002': {'title': 'Data Science Essentials', 'author': 'Jane Smith', 'year': 2019},
    '003': {'title': 'Web Development with Flask', 'author': 'Alex Johnson', 'year': 2021}
}


# Pickle the data
pickle_filename = 'books_data.pickle'

assert pickle_data(books_info, pickle_filename) == "Data pickled successfully to 'books_data.pickle'"
pickle_data(pickle, pickle_filename)
assert pickle_data(pickle, 'pickle_filename.pickle') == "An error occurred while pickling the data."

print("Exercise 1 is correct.")
total_score += 4


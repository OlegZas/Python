'''Exercise 2
Now create a function: unpickle_data that takes the pickled file and unpickles
it. The function should return the data.

Have the function also incorporate a try/except block that will return the
following custom errors:
- for a FileNotFoundError have it return: "File '{filename}' not found."
- For all other exceptions have it return: 'An error occurred while unpickling the data.'
'''

#function here
import pickle

def unpickle_data(filename):
    try:
        with open(filename, 'rb') as file:
            data = pickle.load(file)
        return data
    except FileNotFoundError:
        return f"File '{filename}' not found."
    except Exception:
        return 'An error occurred while unpickling the data.'

# Unpickle the data
pickle_data(books_info, pickle_filename)

result = unpickle_data(pickle_filename)
assert result['001']['title'] == 'Python Programming'
assert unpickle_data('nofile.pickle') == "File 'nofile.pickle' not found."

print("Exercise 2 is correct.")
total_score += 3
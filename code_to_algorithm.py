import time
import re
from collections import OrderedDict


def read_file(filename):
    """Reads Python code from a file."""
    try:
        with open(filename, "r") as f:
            code = f.readlines()
        for i in range(len(code)):
            code[i] = code[i].rstrip()  # Remove trailing newline characters
        return code
    except FileNotFoundError:
        return ["Error: File not found."]


def convert_to_algorithm(code):
    """Converts Python code to a human-readable algorithm description."""

    complex_alterations = OrderedDict({'as': ' as the ', 'assert': ' assert as ', 'async': ' asynchrounous ', 'await': ' await the ', 'break': ' Break the flow of code ', 'class': 'Define a class', 'continue': ' Break this particular iteration of code ', 'def': ' Define a funtion ', 'del': ' delete the ', 'elif': ' Otherwise if ', 'else:': ' Otherwise ', 'except': ' except the ', 'finally': ' finally ', 'for': ' Initiate a for loop with variable ', 'from': ' from the ', 'global': ' Define a global variable ', 'if': ' Check whether ', 'import': ' Import a module named ', 'in': ' in the ', ' is ': ' is a ', 'lambda': ' lamda ', 'nonlocal': ' nonlocal value ', ' not ': ' not in ', ' or ': '(or else)', 'pass': ' pass the ', 'raise': ' raise the ', 'return': ' Return the ', 'try': ' Try the ', 'while': ' Initiate a while loop with condition ', 'with': ' with the ','False': 'False', 'None': 'None', 'True': 'True', ' and ': '(and)'
        
        # ... (rest of your complex_alterations dictionary)
    })

    arithmetic_alterations = OrderedDict({
        '==': 'is equal to',
        '>=': 'greater than or equal to',
        '<=': 'lesser than or equal to',
        '++': 'is incremented by 1',
        '--': 'decremented by 1',
        ' > ': 'is greater than ',
        ' < ': 'is lesser than ',
        ' = ': 'is equal to ',

# ... (rest of your arithmetic_alterations dictionary)
    })

    higher_order_alterations = OrderedDict({
        'print(': 'Display the following in the console (',
        'len(': 'Length of (',
        'range(': 'range of (',
        'round(': 'Round it to ('# ... (rest of your higher_order_alterations dictionary)
    })

    ignore_elements = ['']

    algorithm = ['START']
    for code_line in code:

        if '#' in code_line:
            code_line = code_line[:code_line.index('#')]  # Remove comments

        if 'input(' in code_line and 'print(' not in code_line:
            variable_name = re.search(r'\w+', code_line).group()  # Extract variable name
            code_line = f'Accept a variable {variable_name} from user'

        else:
            for key in higher_order_alterations:
                if key in code_line:
                    code_line = code_line.replace(key, higher_order_alterations[key])

            for key in complex_alterations:
                if key in code_line:
                    code_line = code_line.replace(key, complex_alterations[key])

            for key in arithmetic_alterations:
                if key in code_line:
                    code_line = code_line.replace(key, arithmetic_alterations[key])

        if not code_line or code_line in ignore_elements:
            continue

        if code_line[-1] == ':':
            code_line = code_line[:-1]  # Remove trailing colon

        if code_line[0] == ' ':
            algorithm[-1] += '\n\t' + code_line
        else:
            algorithm.append('Next Step '+code_line)

    return algorithm


def write_algorithm_to_file(algorithm, filename="Algorithm.txt"):
    """Saves the algorithm description to a text file."""
    with open(filename, 'w') as f:
        for i, step in enumerate(algorithm):
            f.write(f"STEP {i+1}: {step}\n")
        f.write("STEP {}: STOP".format(i+2))


# Example usage (optional)
if __name__ == '__main__':
    start_time = time.time()
    code = read_file("PythonCode.py")  # Replace with your actual file reading logic
    algorithm = convert_to_algorithm(code)
    write_algorithm_to_file(algorithm)
    print(f"Algorithm generation completed in {time.time() - start_time:.2f} seconds.")

import string
import itertools

# Print logical symbols and their ASCII characters.
print("And  ^ , ∧\nOr  v, ∨\nNot ~ , ¬\nThen  >\nIFF <>\nAll variables must be 1 character long\n")

# Get and preprocess the input expression.
expression = input("Please enter a logical expression: ").replace(' ', '').replace('v', '∨').replace('^', '∧').replace('~', '¬')

# Define correct variable list using lowercase letters (excluding 'v').
correct_variable_list = list(string.ascii_lowercase)
correct_variable_list.remove('v')

# Extract unique variables from the expression.
variable_list = [char for char in expression if char in correct_variable_list]

# Generate all possible truth assignments for the variables.
interpretations = list(itertools.product([0, 1], repeat=len(variable_list)))

# Initialize a flag to track satisfiability.
flag = False

# Iterate through each interpretation to check satisfiability.
for i, interpretation in enumerate(interpretations):
    exp = expression
    
    # Substitute truth values into the expression.
    for var, value in zip(variable_list, interpretation):
        exp = exp.replace(var, str(value))

    # Define simplification rules for replacements.
    simplifications = {
        'F': '0',
        'T': '1',
        '¬(1)': '(0)',
        '¬(0)': '(1)',
        '¬1': '0',
        '¬0': '1',
        '(1∨0)': '(1)',
        '(0∨1)': '(1)',
        '(1∨1)': '(1)',
        '(0∨0)': '(0)',
        '1∨0': '1',
        '0∨1': '1',
        '1∨1': '1',
        '0∨0': '0',
        '(1∧1)': '(1)',
        '(1∧0)': '(0)',
        '(0∧1)': '(0)',
        '(0∧0)': '(0)',
        '1∧1': '1',
        '1∧0': '0',
        '0∧1': '0',
        '0∧0': '0',
        '(1>1)': '(1)',
        '(0>1)': '(1)',
        '(0>0)': '(1)',
        '(1>0)': '(0)',
        '1>1': '1',
        '0>1': '1',
        '0>0': '1',
        '1>0': '0',
        '(1<>1)': '(1)',
        '(0<>0)': '(1)',
        '(1<>0)': '(0)',
        '(0<>1)': '(0)',
        '1<>1': '1',
        '0<>0': '1',
        '1<>0': '0',
        '0<>1': '0',
        '(1)': '1',
        '(0)': '0'
    }

    # Apply simplifications iteratively until expression is simplified.
    while exp != '0' and exp != '1':
        for key, value in simplifications.items():
            exp = exp.replace(key, value)

    # Check if the expression is satisfied.
    if exp == '1':
        print('This Expression is Satisfiable for:')
        for var, value in zip(variable_list, interpretation):
            print(var, ":", value)
        flag = True

# If no satisfying interpretation is found, print a message.
if not flag:
    print('This Expression is Not Satisfiable')

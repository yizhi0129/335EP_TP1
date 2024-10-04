import numpy as np
from scipy import stats

def is_constant(file_path):
    value = None
    with open(file_path, 'r') as file:
        for line in file:
            data = line.strip().split()
            current_value = float(data[4]) 

            if value is None:
                value = current_value 

            if current_value != value:
                return False  
    return True  


def is_normal_distribution(file_path):
    values = []

    with open(file_path, 'r') as file:
        for line in file:
            data = line.strip().split()
            values.append(float(data[4]))  

    values = np.array(values)

    stat, p_value = stats.shapiro(values)

    return p_value > 0.05
# numerical methods to check if the values follow a normal distribution

def check_files_for_conditions(files):
    constant_files = []
    normal_distribution_files = []

    for file in files:
        if is_constant(file):
            constant_files.append(file)

        if is_normal_distribution(file):
            normal_distribution_files.append(file)

    return constant_files, normal_distribution_files

files = ['trace_a.data', 'trace_b.data', 'trace_c.data']

constant_files, normal_distribution_files = check_files_for_conditions(files)

print(f"Request size is constant for file {constant_files}")
print(f"Request size follows a normal distribution for file {normal_distribution_files}")

# could not execute 
# problem with scipy import
def time_range(file_path):
    first_value = None
    last_value = None

    with open(file_path, 'r') as file:
        first_line = file.readline().strip()
        first_value = float(first_line.split()[1]) 

        for line in file:
            if line.strip():  
                last_line = line.strip()

        last_value = float(last_line.split()[1]) 

    return last_value - first_value

result_a = time_range('trace_a.data')
result_b = time_range('trace_b.data')
result_c = time_range('trace_c.data')

print(f"trace_a: work time {result_a} s")
print(f"trace_b: work time {result_b} s")
print(f"trace_c: work time {result_c} s")

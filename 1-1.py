def process_trace_file(file_path):
    count = 0
    sum_write = 0.0

    with open(file_path, 'r') as file:
        for line in file:
            data = line.strip().split()
            op_type = int(data[2])  
            writting_size = float(data[4])  

            if op_type == 1:
                count += 1
                sum_write += writting_size

    return count, sum_write

count_a, sum_a = process_trace_file('trace_a.data')
count_b, sum_b = process_trace_file('trace_b.data')
count_c, sum_c = process_trace_file('trace_c.data')


print(f"trace_a: count = {count_a}, sum = {sum_a} Bytes")
print(f"trace_b: count = {count_b}, sum = {sum_b} Bytes")
print(f"trace_c: count = {count_c}, sum = {sum_c} Bytes")

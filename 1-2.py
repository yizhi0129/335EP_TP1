def address_space(file_path):
    min_admax_ad = float('inf')
    max_ad = float('-inf')
    address_size = 0 

    with open(file_path, 'r') as file:
        for line in file:
            data = line.strip().split()
            address = float(data[3])  
            address_size = float(data[4])   

            if address > max_ad:
                max_ad = address
                max_address_size = address_size 

            if address < min_admax_ad:
                min_admax_ad = address

    result = (max_ad - min_admax_ad) + max_address_size

    return result

result_a = address_space('trace_a.data')
result_b = address_space('trace_b.data')
result_c = address_space('trace_c.data')

print(f"trace_a: address space = {result_a} Bytes")
print(f"trace_b: address space = {result_b} Bytes")
print(f"trace_c: address space = {result_c} Bytes")

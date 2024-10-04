def find_longest_read_stream(file_path):
    longest_stream = 0
    current_stream = 0

    with open(file_path, 'r') as file:
        for line in file:
            data = line.strip().split()
            operation_type = int(data[2]) 

            if operation_type == 0:
                current_stream += 1 
            else:
                if current_stream > longest_stream:
                    longest_stream = current_stream
                current_stream = 0 

        if current_stream > longest_stream:
            longest_stream = current_stream

    return longest_stream

longest_stream_a = find_longest_read_stream('trace_a.data')
longest_stream_b = find_longest_read_stream('trace_b.data')
longest_stream_c = find_longest_read_stream('trace_c.data')

if longest_stream_a >= longest_stream_b and longest_stream_a >= longest_stream_c:
    longest_trace = 'trace_a.data'
    longest_stream = longest_stream_a
elif longest_stream_b >= longest_stream_a and longest_stream_b >= longest_stream_c:
    longest_trace = 'trace_b.data'
    longest_stream = longest_stream_b
else:
    longest_trace = 'trace_c.data'
    longest_stream = longest_stream_c

print(f"The file with the longest stream of read operations is {longest_trace} with a stream length of {longest_stream}.")

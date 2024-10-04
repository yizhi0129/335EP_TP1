import numpy as np
import random

def generate_requests(output_file, N, t_min, t_max, n_r, n_w, p_h, h, s_med, stddev):
    
    # MB to bits
    h_bit = h * 1024 * 1024 
    c_bit = c * 1024 * 1024
    
    with open(output_file, 'w') as f:
        time = 0.0  

        n_mod = n_r + n_w
        
        for i in range(N):
            request_id = i  
            dt = random.uniform(t_min, t_max)  
            time += dt  
                       
            if i % n_mod < n_r:
                operation = 0  # n_r reads
            else:
                operation = 1  # then n_w writes
            
            if random.random() < p_h:
                address = random.randint(0, h_bit - 1) # p_h probability of address size h in MB
            else:
                address = random.randint(0, c_bit - 1) # (1 - p_h) probability of address size c in MB

            # request size following normal distribution in KB
            request_size = max(1, int(np.random.normal(s_med, stddev)))  
            
            f.write(f"{request_id} {time:.2f} {operation} {address} {request_size}\n")

output_file = 'generated_trace.data'
N = 10000
t_min = 0.5  
t_max = 1.5
n_r = 200
n_w = 800
p_h = 0.8  
h = 200  # MB
c = 800  # MB
s_med = 512  # KB
stddev = 128 # KB

generate_requests(output_file, N, t_min, t_max, n_r, n_w, p_h, h, s_med, stddev)

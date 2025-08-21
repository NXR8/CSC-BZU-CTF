def long_to_bytes(n):
    byte_array = bytearray()
    while n > 0:
        byte_array.append(n & 0xff)
        n = n >> 8
    return bytes(byte_array[::-1])

def nth_root(x, n):
    high = 1
    while high ** n < x:
        high *= 2
    low = high // 2
    while low <= high:
        mid = (low + high) // 2
        if mid ** n < x:
            low = mid + 1
        elif mid ** n > x:
            high = mid - 1
        else:
            return mid
    return high

#N = <Provided by the server>

e = 3

#C = <Provided by the server> 

i = 0
while True:
    # Try to find the cube root of (i*N + c)
    m_candidate = nth_root(i*N + C, e)
    
    # Convert the candidate message to bytes
    flag_candidate = long_to_bytes(m_candidate)
    
    # Check if this looks like the flag (contains 'pico')
    if b'CSC-BZU' in flag_candidate:
        # Clean up the flag string and print it
        flag = str(flag_candidate)[2:-1].lstrip(" ")
        print(f"Found the flag with i = {i}:")
        print(flag)
        break
    i+=1

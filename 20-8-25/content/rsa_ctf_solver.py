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

N = 101713220423079878037526494147515626568328681878007768545038437917999201502586160129514842603434644804573178692350341553219079007490389659540102577237879576621330935649478015668041797539420118789680529067267675604200670236074580579171846438830857880615619859699780310286810830644957964630797525265807097060161

e = 3

c = 23378992974408776356502498065179120399834694058723934240831364435513413157374101158334503099576284737873526883422919363279432755274708971921746983766264168652645021714551246188891774461062071363572169385910137502901435874947337912832085341232340069407004269569897371517982309753618372513702247130386830677085
i = 0
while True:
    # Try to find the cube root of (i*N + c)
    m_candidate = nth_root(i*N + c, e)
    
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

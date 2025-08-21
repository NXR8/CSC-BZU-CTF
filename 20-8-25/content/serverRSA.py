from Crypto.Util.number import getPrime, bytes_to_long
import socket
import threading

def generate_rsa_params():
    flag = b'CSC-BZU{i_w1ll_m@k3_3_l4rg3_1n_s3c0nd_t1m3}'
    e = 3
    p = getPrime(512)
    q = getPrime(512)
    N = p * q
    c = pow(bytes_to_long(flag), e, N)
    return N, e, c

def handle_client(conn, addr):
    print(f"Connection from {addr}")
    N, e, c = generate_rsa_params()
    
    # Send values separated by newlines
    conn.sendall(f"N = {N}\n\ne = {e}\n\nC = {c}\n\n".encode())
    conn.close()

def start_server(host='0.0.0.0', port=69):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.bind((host, port))
        s.listen()
        print(f"Server listening on {host}:{port}")
        
        while True:
            conn, addr = s.accept()
            threading.Thread(target=handle_client, args=(conn, addr)).start()

if __name__ == "__main__":
    start_server()

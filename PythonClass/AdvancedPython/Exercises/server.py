import socket
import pickle

def run_server():
    people = {
        "Oleg": {"Role": "Data Engineer", "Location": "California", "Hobby": "Ultra-marathons"},
        "Meche": {"Role": "Travel Planner", "Location": "Costa Rica", "Hobby": "Adventures"},
        "Diby": {"Role": "Artist", "Location": "Singapore", "Hobby": "Reading"}
    }

    host = '127.0.0.1' # Localhost
    port = 65432       

    # 2. Socket Communication 
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen()

    print(f"Listening on [{host}:{port}]")

    while True:
        conn, addr = server_socket.accept()
        print(f"Connection established with {addr}")
        data = conn.recv(1024).decode('utf-8') 
        
        if not data:
            break
            
        requested_name = data.strip()
        print(f"Client asked for: {requested_name}")

        if requested_name in people:
            response_data = people[requested_name]
        else:
            response_data = {"Error": f"The person '{requested_name}' does not exist in the database."}

        pickled_response = pickle.dumps(response_data)
        
        conn.sendall(pickled_response)
        
        conn.close()

if __name__ == "__main__":
    run_server()
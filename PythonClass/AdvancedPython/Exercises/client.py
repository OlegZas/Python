import socket
import pickle

def run_client():
    host = '127.0.0.1'  
    port = 65432        

    # 1. User Input
    name_to_search = input("Enter the name of the individual you are interested in (Oleg;Meche;Diby): ")

    # 2. Socket Comm
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    try:
        client_socket.connect((host, port))
        
        client_socket.sendall(name_to_search.encode('utf-8'))

        # 3. response from the server
        received_data = client_socket.recv(4096) 
        
        response_dict = pickle.loads(received_data)

        # 4. Display Output 
        print("\n--- Server Response ---")
        if "Error" in response_dict: #eror check
            print(response_dict["Error"])
        else:
            print(f"Information for {name_to_search}:")
            for key, value in response_dict.items():
                print(f"  - {key}: {value}")
                
    except ConnectionRefusedError:
        print("Could not connect to the server. Is server.py running?")
    finally:
        client_socket.close()

if __name__ == "__main__":
    run_client()
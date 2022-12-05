import socket
import select
import pickle
HEADER_LENGTH = 10
IP = "127.0.0.1"
PORT = 1234

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
zoomiConnected = False
fletConnected = False
server_socket.bind((IP, PORT))

server_socket.listen()

sockets_list = [server_socket]

clients = {}

print(f"Listening for connections on {IP}:{PORT}")

def recieve_message(client_socket):

    try:

        message_header = client_socket.recv(HEADER_LENGTH)

        if not len(message_header):
            return False

        message_length = int(message_header.decode("utf-8"))
        return {"header": message_header, "data": client_socket.recv(message_length)}
    except:

        return False


while True:
    read_sockets, _, exception_sockets = select.select(
        sockets_list, [], sockets_list)

    for notified_socket in read_sockets:
        # someone just connected
        if notified_socket == server_socket:
            client_socket, client_address = server_socket.accept()

            user = recieve_message(client_socket)
            if user is False:
                continue

            sockets_list.append(client_socket)

            clients[client_socket] = user

            print(
                f"Accepted new connection from {client_address[0]}:{client_address[1]} username:{user['data'].decode('utf-8')}")
            message = {"source" : "server", "info":"online", "name": user['data'].decode('utf-8')}
            user = "server"
            user = user.encode('utf-8')
            user_header = f"{len(user) :< {HEADER_LENGTH}}".encode(
            "utf-8")
            message = pickle.dumps(message)
            message_header = f"{len(message) :< {HEADER_LENGTH}}".encode(
            "utf-8")
            for client_socket in clients:
                if client_socket != notified_socket:
                    client_socket.send(user_header +user + message_header + message)
            
        else:
            message = recieve_message(notified_socket)
            if message is False:
                disconnectedClient =clients[notified_socket]['data'].decode('utf-8')
                print(
                    f"Closed connection from {disconnectedClient}")
                sockets_list.remove(notified_socket)
                del clients[notified_socket]
                message = {"source" : "server", "info":"offline", "name": disconnectedClient}
                user = "server".encode('utf-8')
                user_header = f"{len(user) :< {HEADER_LENGTH}}".encode(
                "utf-8")
                message = pickle.dumps(message)
                message_header = f"{len(message) :< {HEADER_LENGTH}}".encode(
                "utf-8")
                # for client_socket in clients:
                #     if client_socket != notified_socket:
                #         client_socket.send( user_header + user + message_header + message)
                continue

            user = clients[notified_socket]

            print(
                f"Recieved Message From {user['data'].decode('utf-8')}: {pickle.loads(message['data'])}")
            for client_socket in clients:
                if client_socket != notified_socket:
                        client_socket.send(
                            user['header'] + user['data'] + message['header'] + message['data'])

    for notified_socket in exception_sockets:
        
        sockets_list.remove(notified_socket)

        del clients[notified_socket]

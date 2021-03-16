import socket
import time
server_port = 21060
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
input_s = 'Hello, server!'
client_socket.sendto(bytes(input_s, encoding='utf8'), ('127.0.0.1', server_port))
input_s_modified, address = client_socket.recvfrom(65535)
print ('[CLIENT] Response from server {}, is: "{}"'.format(address, str(input_s_modified.decode('utf8'))))
while True:
    print("Server response: ")
    my_time = time.localtime(time.time())
    my_time_parsed = time.strftime("%S",my_time)
    print(my_time_parsed)
    time.sleep(60)
client_socket.close()
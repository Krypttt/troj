import socket
from impro_conve import int_to_nbyte, nbyte_to_int

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(), 1235))
s.listen(5)
while True:
    conn, addr = s.accept()
    data, _ = nbyte_to_int(conn)
    print("Received {} from {} at port {}".format(data, addr[0], addr[1]))
    conn.close()

s.close()

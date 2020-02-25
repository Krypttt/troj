import socket
from impro_conve import int_to_nbyte, nbyte_to_int

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((socket.gethostname(), 1235))
s.send(int_to_nbyte(5201314))
s.close()

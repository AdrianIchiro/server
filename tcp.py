import socket

targeturl = "www.udemy.com"
targetport = 80

conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
conn.connect((targeturl, targetport))
conn.send(b"GET / HTTP/1.1\rnHost: udemy.com\r\n\r\n")


result = conn.recv(4096)
print(result.decode())
conn.close()

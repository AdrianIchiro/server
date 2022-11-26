import socket

conn = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
conn.sendto(b"tes aja", ("127.0.0.1", 9997))

data, addr = conn.recvfrom(4090)
print("pesan dari server : \"{}\"".format(data.decode()))

conn.close()

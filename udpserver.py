import socket

ip = "127.0.0.1"
port = 9997

server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server.bind((ip, port))

print("Server On")

while True:
    data = server.recvfrom(1024)
    iptarget = data[1]
    pesan = data[0]

    print("Ip : \"{}\"".format(iptarget))
    print("Pesan : \"{}\"".format(pesan))

    server.sendto(b"Halo selamat datang di server saya", iptarget)

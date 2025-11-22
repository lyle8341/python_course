import socket

socket_server = socket.socket()

socket_server.bind(("localhost", 8888))

# 接受的连接数量
socket_server.listen(1)

conn, address = socket_server.accept()

print(f"接收到了客户端的连接，客户端的信息是: {address}")

# recv接收的参数是缓冲区大小，一般1024即可
# decode 将字节数组转成字符串对象
data: str = conn.recv(1024).decode("UTF-8")
print(f"客户端发来的消息是: {data}")

msg = input("请输入回复消息:").encode("UTF-8")
conn.send(msg)

# 关闭当前连接
conn.close()

# 关闭socket server
socket_server.close()


# 客户端
# https://github.com/nicedayzhu/netAssist/releases
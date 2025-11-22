import socket

# 1.创建socket
socket_client = socket.socket()
# 2.连接到服务端
socket_client.connect(("localhost", 8888))
# 3.发送消息

while True:
    send_msg = input("请输入要发送的消息")
    if send_msg == 'exit':
        break
    socket_client.send(send_msg.encode("UTF-8"))

    recv_data = socket_client.recv(1024)
    print(f"收到服务端消息: {recv_data.decode('UTF-8')}")

socket_client.close()

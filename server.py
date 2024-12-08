import ssl
import socket

def dechifrz(string, count):
    arr = []
    for j in range(count // 2):
        temp = [[''] * 6, [''] * 6]
        for i in range(6):
            temp[0][i] = string[0]
            string = string[1:]
            temp[1][i] = string[0]
            string = string[1:]
        arr.append(temp[0])
        arr.append(temp[1])
    return arr

def reconstruct_text(arr):
    text = ''
    for row in arr:
        for char in row:
            if char == '':
                text += ' '
            else:
                text += char
    return text


CERT_FILE = "C:\\Users\\Куаныш\\OneDrive\\Документы\\project_hackaton\\certs\\server.crt"
KEY_FILE = "C:\\Users\\Куаныш\\OneDrive\\Документы\\project_hackaton\\certs\\private.key"

context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
context.load_cert_chain(certfile=CERT_FILE, keyfile=KEY_FILE)

HOST = 'localhost'
PORT = 8443

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
    server_socket.bind((HOST, PORT))
    server_socket.listen(5)
    print(f"SSL-сервер запущен на {HOST}:{PORT}...")

    with context.wrap_socket(server_socket, server_side=True) as ssl_socket:
        while True:
            client_socket, client_addr = ssl_socket.accept()
            print(f"Клиент подключён: {client_addr}")

            with client_socket:
                while True:
                    data = client_socket.recv(1024)
                    if not data:
                        break
                    print(f"Получено сообщение: {data.decode('utf-8')}")
                    count = len(data.decode('utf-8')) // 12 * 2
                    arr = dechifrz(data.decode('utf-8'), count)
                    original_text = reconstruct_text(arr)
                    client_socket.sendall(original_text.encode('utf-8'))
                    print(f"Отправлено обратно: {data.decode('utf-8')}")

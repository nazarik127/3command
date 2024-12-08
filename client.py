import ssl
import socket

def chifrz(arr, count = 2):
    string = ''
    for i in range(count//2):
        arr_temp = arr[:2]
        arr = arr[2:]
        for i in range(6):
            for j in range(2):
                string += arr_temp[j][i]
    return string

def fill_arr(text):
    count = 0
    arr = []
    a = True
    mass = [' ',' ',' ',' ',' ',' ']
    while a:
        count += 1
        temp = []
        for i in range(6):
            temp.append(text[0])
            text = text[1:]
            if text == '':
                if count % 2 != 0:
                    if i < 5:
                        for j in range(1):
                            for g in range(5-i):
                                temp.append(' ')
                            arr.append(temp)
                            arr.append(mass)
                            return arr, count+1
                elif i < 5:
                    for g in range(5-i):
                        temp.append(' ')
                arr.append(temp)
                return arr, count
        arr.append(temp)
    return arr, count

server_cert = "C:\\Users\\Куаныш\\OneDrive\\Документы\\project_hackaton\\certs\\server.crt"

context = ssl.create_default_context(ssl.Purpose.SERVER_AUTH, cafile=server_cert)

with socket.create_connection(("localhost", 8443)) as sock:
    with context.wrap_socket(sock, server_hostname="localhost") as ssl_sock:
        print("Соединение с сервером установлено.")
        try:
            while True:
                message = input("Введите сообщение для сервера: ").strip()
                arr, count = fill_arr(message)
                message = chifrz(arr, count)
                print(f'chifrz: {message}')
                ssl_sock.sendall(message.encode('utf-8'))
                response = ssl_sock.recv(1024)
                print(f"Ответ от сервера: {response.decode('utf-8')}")
        except KeyboardInterrupt:
            print("Отключение клиента.")

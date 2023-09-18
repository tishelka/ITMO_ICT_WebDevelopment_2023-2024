import socket

server_address = ('localhost', 8080)


while True:
    try:
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        client_socket.connect(server_address)
        discipline = input(
            "Введите название дисциплины (или 'exit' для выхода): ")
        if discipline.lower() == 'exit':
            break
        grade = input("Введите оценку: ")

        post_request = "POST / HTTP/1.1\r\n"
        post_request += "Host: {}\r\n".format(server_address[0])
        post_request += "Content-Type: application/x-www-form-urlencoded\r\n"
        post_request += "Content-Length: {}\r\n\r\n".format(
            len("discipline={}&grade={}".format(discipline, grade)))
        post_request += "discipline={}&grade={}".format(discipline, grade)

        client_socket.send(post_request.encode('utf-8'))

        response = client_socket.recv(1024).decode('utf-8')
        print(response)
    except Exception as e:
        print("Ошибка: {}".format(e))

client_socket.close()

import socket
import re
import json

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_address = ('localhost', 8080)

server_socket.bind(server_address)

server_socket.listen(1)

print("Сервер запущен на {}:{}".format(server_address[0], server_address[1]))

grades = {}


def handle_request(request):
    global grades
    response = ""

    if request.startswith("GET"):
        response += "HTTP/1.1 200 OK\r\nContent-Type: application/json; charset=utf-8\r\n\r\n"
        response += json.dumps(grades, ensure_ascii=False)

    elif request.startswith("POST"):
        match = re.search(r"discipline=(\w+)&grade=(\d+)", request)
        if match:
            discipline = match.group(1)
            grade = match.group(2)
            grades[discipline] = grade
            response += "HTTP/1.1 200 OK\r\nContent-Type: text/plain\r\n\r\n"
            response += "Информация о дисциплине и оценке сохранена."
        else:
            response += "HTTP/1.1 400 Bad Request\r\nContent-Type: text/plain\r\n\r\n"
            response += "Ошибка: Некорректные данные в POST запросе."

    return response


while True:
    client_socket, client_address = server_socket.accept()
    print("Подключение от {}:{}".format(client_address[0], client_address[1]))

    request = client_socket.recv(1024).decode('utf-8')

    response = handle_request(request)

    client_socket.send(response.encode('utf-8'))

    client_socket.close()

import socket

html = """<!DOCTYPE html>
<html>
    <head> <title>ESP32 Login</title> </head>
    <body>
        <h1>Login Page</h1>
        <form action="/login" method="POST">
            <label for="username">Username:</label><br>
            <input type="text" id="username" name="username"><br>
            <label for="password">Password:</label><br>
            <input type="password" id="password" name="password"><br><br>
            <input type="submit" value="Submit">
        </form>
    </body>
</html>
"""

def web_server():
    addr = socket.getaddrinfo('0.0.0.0', 80)[0][-1]
    s = socket.socket()
    s.bind(addr)
    s.listen(1)
    print('Listening on', addr)

    while True:
        cl, addr = s.accept()
        print('Client connected from', addr)
        request = cl.recv(1024)
        request = str(request)

        if 'POST /login' in request:
            user_start = request.find('username=') + 9
            user_end = request.find('&', user_start)
            username = request[user_start:user_end]

            pass_start = request.find('password=') + 9
            pass_end = request.find(' ', pass_start)
            password = request[pass_start:pass_end]

            print('Username:', username)
            print('Password:', password)

        response = html
        cl.send('HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n\r\n')
        cl.send(response)
        cl.close()

web_server()

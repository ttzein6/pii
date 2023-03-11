import socket
import re

def parse_request(request):
    """Parses the HTTP request string and returns the request method and path."""
    parts = request.split()
    method = parts[0]
    path = parts[1]
    return method, path

def get_response(request):
    """Returns the appropriate HTTP response for the given request."""
    method, path = parse_request(request)
    response = ''
    status_code = 200

    # if path == '/account':
    #     if method == 'GET':
    #         with open('account.html', 'r') as f:
    #             response = f.read()
        # elif method == 'POST':
        #     with open('account-created.html', 'r') as f:
        #         response = f.read()
        # elif method == 'PUT':
        #     with open('account-updated.html', 'r') as f:
        #         response = f.read()
        # elif method == 'DELETE':
        #     with open('account-deleted.html', 'r') as f:
        #         response = f.read()
        # elif method == 'PATCH':
        #     with open('account-patched.html', 'r') as f:
        #         response = f.read()
        # else:
        #     status_code = 405
    if re.match('^/user/([\w-]+)$', path):
        if method == 'GET':
            with open('account.html', 'r') as f:
                response = f.read()
                username = re.search('^/user/([\w-]+)$', path).group(1)
                response = response.replace('{username}', username)
        else:
            status_code = 405
    elif path == '/login' or path == '/login/':
        if method == 'GET':
            with open('login.html', 'r') as f:
                response = f.read()
        else:
            status_code = 405
    elif path == '/signup' or path == '/signup/':
        if method == 'GET':
            with open('signup.html', 'r') as f:
                response = f.read()
        else:
            status_code = 405
    elif path == '' or path == '/':
        if method == 'GET':
            with open('getRecieved.html', 'r') as f:
                response = f.read()
        else:
            status_code = 405
    else:
        status_code = 404
        with open('404.html', 'r') as f:
            response = f.read()

    return response, status_code

def run_server():
    """Runs the server and listens for incoming requests."""
    HOST = '127.0.0.1'
    PORT = 8000

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.bind((HOST, PORT))
        s.listen()

        print(f'Server running on http://{HOST}:{PORT}')

        while True:
            conn, addr = s.accept()
            with conn:
                print(f'Connected by {addr}')
                request = conn.recv(1024).decode('utf-8')
                print(request)

                response, status_code = get_response(request)

                headers = 'HTTP/1.1 ' + str(status_code) + ' OK\r\n'
                headers += 'Content-Type: text/html\r\n'
                headers += 'Content-Length: ' + str(len(response.encode('utf-8'))) + '\r\n'
                headers += '\r\n'

                conn.sendall(headers.encode('utf-8'))
                conn.sendall(response.encode('utf-8'))

if __name__ == '__main__':
    run_server()

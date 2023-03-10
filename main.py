from http.server import BaseHTTPRequestHandler, HTTPServer
from httpHandler import HTTPRequestHandler


def run():
    print('Starting server...')
    server_address = ('192.168.1.8', 8080) # Change IP address and port number as needed
    httpd = HTTPServer(server_address, HTTPRequestHandler)
    print('Server started.')
    httpd.serve_forever()

if __name__ == '__main__':
    run()

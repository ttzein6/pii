from http.server import BaseHTTPRequestHandler, HTTPServer
class HTTPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        # Handle GET requests here
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        with open('getRecieved.html', 'rb') as file:
            self.wfile.write(file.read())
        
        # self.wfile.write(b'<html><body><h1>GET request received!</h1></body></html>')

    def do_POST(self):
        # Handle POST requests here
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        with open('postRecieved.html', 'rb') as file:
            self.wfile.write(file.read())
        # self.wfile.write(b'<html><body><h1>POST request received!</h1></body></html>')

    def do_PUT(self):
        # Handle PUT requests here
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(b'<html><body><h1>PUT request received!</h1></body></html>')

    def do_DELETE(self):
        # Handle DELETE requests here
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(b'<html><body><h1>DELETE request received!</h1></body></html>')

    def do_PATCH(self):
        # Handle PATCH requests here
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(b'<html><body><h1>PATCH request received!</h1></body></html>')
#!/usr/bin/env python3

import http.server

class Handler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        if (self.path == "/"):
            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"Hello, this is a simple API!")
        elif (self.path == "/data"):
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            self.wfile.write(b'{"name": "John", "age": 30, "city": "New York"}')
        elif (self.path == "/info"):
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            self.wfile.write(b'{"version": "1.0", "description": "A simple API built with http.server"}')
        elif (self.path == "/status"):
            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"OK")
        else:
            self.send_response(404)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"Endpoint not found")

if __name__ == "__main__":
    address = ("", 8000)
    httpd = http.server.HTTPServer(address, Handler)
    httpd.serve_forever()

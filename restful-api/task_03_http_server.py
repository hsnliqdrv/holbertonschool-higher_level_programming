#!/usr/bin/env python3

import http.server

class Handler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/plain")
        self.end_headers()
        self.wfile.write(b"Hello, this is a simple API!")

if __name__ == "__main__":
    address = ("", 8000)
    httpd = http.server.HTTPServer(address, Handler)
    httpd.serve_forever()

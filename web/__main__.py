from http.server import BaseHTTPRequestHandler, HTTPServer
from page import html

class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.send_header("X-Clacks-Overhead", "GNU Terry Pratchett")
        self.end_headers()
        self.wfile.write(html().encode("utf8"))

HTTPServer(("", 80), MyServer).serve_forever()

from http.server import BaseHTTPRequestHandler, HTTPServer

class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.send_header("X-Clacks-Overhead", "GNU Terry Pratchett")
        self.end_headers()
        self.wfile.write(bytes("Hello, world!", "utf8"))

HTTPServer(("", 80), MyServer).serve_forever()

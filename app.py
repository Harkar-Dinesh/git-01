from http.server import HTTPServer, BaseHTTPRequestHandler



PORT = 8084




class MyHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(2000)
        self.send_header("Content-type", "text/html")
        self.end_headers()

        self.wfile.write(b"<h1>Hello from Python Server</h1>")

server = HTTPServer(("0.0.0.0", PORT), MyHandler)

print(f"Server running on port {PORT}")

server.serve_forever()

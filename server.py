from http.server import HTTPServer, SimpleHTTPRequestHandler

class CustomHandler(SimpleHTTPRequestHandler):
    def do_POST(self):
        content_length = int(self.headers.get('Content-Length', 0))
        post_data = self.rfile.read(content_length).decode('utf-8')
        print(f"\n[+] Data POST Diterima di Server: {post_data}\n")

        self.send_response(200)
        self.send_header('Content-Type', 'text/html')
        self.end_headers()
        self.wfile.write(b"<h3>Data login berhasil terkirim via HTTP!</h3>")

if __name__ == '__main__':
    server_address = ('0.0.0.0', 8080)
    httpd = HTTPServer(server_address, CustomHandler)
    print("Server HTTP aktif di http://localhost:8080 ...")
    httpd.serve_forever()

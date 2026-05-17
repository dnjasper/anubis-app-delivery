import http.server
import socketserver

PORT = 8080

class MyHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "application/json")
        self.end_headers()
        # 🚀 This specific JSON payload proves your application is running natively inside EKS
        response = '{"status": "success", "message": "Anubis API is online and healthy inside EKS!", "version": "1.0.0"}'
        self.wfile.write(bytes(response, "utf8"))

with socketserver.TCPServer(("", PORT), MyHandler) as httpd:
    print(f"Server executing on port {PORT}")
    httpd.serve_forever()


# Python 3 server
from http.server import BaseHTTPRequestHandler, HTTPServer
import json

hostName = "0.0.0.0"
serverPort = 8080


class MyServer(BaseHTTPRequestHandler):

    def load_binary(self, filename):
        with open(filename, 'rb') as file_handle:
            return file_handle.read()

    def response_image(self):
        self.send_response(200)
        self.send_header("Content-type", "image/png")
        self.end_headers()
        file_read = self.load_binary('../images/flag_glarus.png')
        self.wfile.write(file_read)

    def response_json(self):
        data = {
            'lorem': 'ipsum',
            'dolores': 12
        }

        self.send_response(200)
        self.send_header("Content-type", "application/json")
        self.end_headers()
        self.wfile.write(json.dumps(data).encode('utf-8'))

    def do_GET(self):
        if self.path == '/image':
            self.response_image()

        elif self.path == '/json':
            self.response_json()

        else:
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(bytes("<html><head><title>https://pythonbasics.org</title></head>", "utf-8"))
            self.wfile.write(bytes("<p>Request: %s</p>" % self.path, "utf-8"))
            self.wfile.write(bytes("<body>", "utf-8"))
            self.wfile.write(bytes("<p>This is an example web server.</p>", "utf-8"))
            self.wfile.write(bytes("</body></html>", "utf-8"))


if __name__ == "__main__":
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print("Server started http://%s:%s" % (hostName, serverPort))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")
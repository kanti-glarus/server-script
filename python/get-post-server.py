# Python 3 server
from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse
import cgi

hostName = "0.0.0.0"
serverPort = 8080


class EinfacherServer(BaseHTTPRequestHandler):

    def get_path(self):
        return urlparse(self.path).path

    def get_parameters(self):
        parameter_string = urlparse(self.path).query
        parameters = dict(qc.split("=") for qc in parameter_string.split("&"))
        return parameters

    def post_parameters(self):
        form = cgi.FieldStorage(
            fp=self.rfile,
            headers=self.headers,
            environ={'REQUEST_METHOD': 'POST'}
        )
        return form

    def do_POST(self):
        path = self.get_path()
        title = ''

        if path == '/post':
            parameters = self.post_parameters()
            name = parameters.getvalue('username')
            title = 'POST: hello ' + str(name)

        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(bytes("<html><head><title>POST REQUEST</title></head>", "utf-8"))
        self.wfile.write(bytes("<body>", "utf-8"))
        self.wfile.write(bytes("<h1>%s</h1>" % title, "utf-8"))
        self.wfile.write(bytes("</body></html>", "utf-8"))

    def do_GET(self):
        title = 'no title'
        path = self.get_path()

        if path == '/get':
            parameters = self.get_parameters()
            name = parameters['name']
            title = 'GET: hello ' + name

        if path == '/form':
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(bytes("<form action='/post' method='POST'>", "utf-8"))
            self.wfile.write(bytes("<input type='text' name='username'>", "utf-8"))
            self.wfile.write(bytes("<input type='submit' name='senden'>", "utf-8"))
            self.wfile.write(bytes("</form>", "utf-8"))
            return

        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(bytes("<html><head><title>GET REQUEST</title></head>", "utf-8"))
        self.wfile.write(bytes("<body>", "utf-8"))
        self.wfile.write(bytes("<h1>%s</h1>" % title, "utf-8"))
        self.wfile.write(bytes("<p>This is an example web server.</p>", "utf-8"))
        self.wfile.write(bytes("</body></html>", "utf-8"))


if __name__ == "__main__":
    webServer = HTTPServer((hostName, serverPort), EinfacherServer)
    print("Server started http://%s:%s" % (hostName, serverPort))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")

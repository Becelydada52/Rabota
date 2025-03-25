from http.server import HTTPServer, SimpleHTTPRequestHandler
import os
from urllib.parse import parse_qs, urlparse

class RequestHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        
        if self.path.startswith('/static/') or \
           self.path.endswith('.css') or \
           self.path.endswith('.js') or \
           self.path.endswith('.jpg') or \
           self.path.endswith('.png'):
            super().do_GET()
            return

        # Обработка основных страниц
        if self.path == '/' or self.path == '/main':
            self.send_response(200)
            self.send_header('Content-type', 'text/html; charset=utf-8')
            self.end_headers()
            with open('main.html', 'rb') as f:
                self.wfile.write(f.read())
        elif self.path == '/price':
            self.send_response(200)
            self.send_header('Content-type', 'text/html; charset=utf-8')
            self.end_headers()
            with open('Price.html', 'rb') as f:
                self.wfile.write(f.read())
        else:
            self.send_response(404)
            self.send_header('Content-type', 'text/html; charset=utf-8')
            self.end_headers()
            self.wfile.write(b'404 Not Found')

if __name__ == '__main__':
    # Проверка директории
    web_dir = os.path.join(os.path.dirname(__file__))
    os.chdir(web_dir)
    
    server_address = ('', 8000)
    httpd = HTTPServer(server_address, RequestHandler)
    print('Сервер запущен на http://localhost:8000')
    print('Нажмите Ctrl+C для остановки сервера')
    httpd.serve_forever()

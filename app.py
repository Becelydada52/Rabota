from http.server import HTTPServer, SimpleHTTPRequestHandler
import json
import os
from urllib.parse import parse_qs

class NewsHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
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
            super().do_GET()

    def do_POST(self):
        if self.path == '/save-news':
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)
            news_data = json.loads(post_data.decode('utf-8'))
            
            try:
                # Проверяем существование файла
                if not os.path.exists('news.json'):
                    with open('news.json', 'w', encoding='utf-8') as f:
                        json.dump({"news": []}, f, ensure_ascii=False, indent=4)

                # Сохраняем JSON
                with open('news.json', 'w', encoding='utf-8') as f:
                    json.dump(news_data, f, ensure_ascii=False, indent=4)
                
                self.send_response(200)
                self.send_header('Content-type', 'application/json')
                self.end_headers()
                self.wfile.write(json.dumps({"status": "success"}).encode())
            
            except Exception as e:
                self.send_response(500)
                self.send_header('Content-type', 'application/json')
                self.end_headers()
                self.wfile.write(json.dumps({"error": str(e)}).encode())
        else:
            super().do_POST()

if __name__ == '__main__':
    server_address = ('', 8000)
    httpd = HTTPServer(server_address, NewsHandler)
    print('Сервер запущен на порту 8000...')
    httpd.serve_forever()
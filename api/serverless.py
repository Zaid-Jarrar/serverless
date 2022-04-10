from http.server import BaseHTTPRequestHandler
from datetime import datetime

class handler(BaseHTTPRequestHandler):

  def do_GET(self):
    self.send_response(200)
    self.send_header('Content-type', 'text/plain')
    self.end_headers()
    question = input("Enter a number: ")
    self.wfile.write(bytes(question, "utf-8"))
    multi = int(question) ** 2
    self.wfile.write(bytes(str(multi), "utf-8"))
    self.wfile.write(str(datetime.now().strftime('%Y-%m-%d %H:%M:%S')).encode())
    return

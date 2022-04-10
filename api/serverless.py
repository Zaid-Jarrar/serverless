from http.server import BaseHTTPRequestHandler
from datetime import datetime

class handler(BaseHTTPRequestHandler):

  def do_GET(self):
    self.send_response(200)
    self.send_header('Content-type', 'text/plain')
    self.end_headers()
    self.path = 'large_m12Yz5uRK2DL5UCAZMbeB3ArNNg.jpg'
    with open(self.path, 'rb') as f:
      self.wfile.write(f.read())
    self.wfile.write(str(datetime.now().strftime('%Y-%m-%d %H:%M:%S')).encode())
    return

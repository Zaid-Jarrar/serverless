import math

from http.server import BaseHTTPRequestHandler
from datetime import datetime

class handler(BaseHTTPRequestHandler):

  def do_GET(self):
    self.send_response(200)
    self.send_header('Content-type', 'text/plain')
    self.end_headers()
    sqr = math.sqrt(int(self.path[1:]))
    self.wfile.write(sqr.encode())
    self.wfile.write(str(datetime.now('GMT+3').strftime('%Y-%m-%d %H:%M:%S')).encode())

    return
    


from http.server import BaseHTTPRequestHandler
from datetime import datetime
from urllib.parse import urlparse

class handler(BaseHTTPRequestHandler):

  def do_GET(self):
    self.send_response(200)
    self.send_header('Content-type', 'text/plain')
    self.end_headers()
    # self.path = 'large_m12Yz5uRK2DL5UCAZMbeB3ArNNg.jpg'
    # with open(self.path, 'rb') as f:
    #   self.wfile.write(f.read())
    url= urlparse('https://serverless-eight-tawny.vercel.app/api/serverless')
    self.wfile.write(str(datetime.now().strftime('%Y-%m-%d-%W %H:%M:%S')).encode())
    url.path
    return


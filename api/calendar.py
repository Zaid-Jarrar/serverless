from http.server import BaseHTTPRequestHandler
from datetime import datetime
import calendar
# from urllib.parse import urlparse
import urllib.parse

class handler(BaseHTTPRequestHandler):

  def do_GET(self):
    self.send_response(200)
    self.send_header('Content-type', 'text/plain')
    self.end_headers()
    # self.path = 'large_m12Yz5uRK2DL5UCAZMbeB3ArNNg.jpg'
    # with open(self.path, 'rb') as f:
    #   self.wfile.write(f.read())
    url= 'https://serverless-eight-tawny.vercel.app/api/calendar'
    result = urllib.parse.urlparse(url)
    self.wfile.write(result)
    self.wfile.write('Scheme : ' + result.scheme)
    self.wfile.write('HostName : ' + result.hostname)
    self.wfile.write('Query : ' + result.query)


    

    message1 = 'This is the datetime Year/Month/Day/Number of Week/Hour/Minute/Second: ' +'\n'
    message2 = 'This is the Calendar for year 2022: ' +'\n\n'

    self.wfile.write(message1.encode())
    self.wfile.write(str(datetime.now().strftime('%Y-%m-%d/%W/ %H:%M:%S \n')).encode())
    self.wfile.write(message2.encode())
    self.wfile.write(calendar.calendar(2022, 2, 1, 6).encode())
    url.params
    self.wfile.write(url.query.encode())
    return


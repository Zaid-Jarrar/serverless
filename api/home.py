from http.server import BaseHTTPRequestHandler
from datetime import datetime
from urllib import parse
import platform
import calendar

class handler(BaseHTTPRequestHandler):

  def do_GET(self):
    self.send_response(200)
    self.send_header('Content-type', 'text/plain')
    self.end_headers()

    path= self.path
    url_components = parse.urlparse(path)
    query_string = parse.parse_qsl(url_components.query)
    dic=dict(query_string)
    name= dic.get('name')
    if name:
      message = f'Hello, {name}!\n'
    else:
      message = 'Hello, Stranger!\n' 

    message += f"\n Greetings from Python Version {platform.python_version()} at {datetime.now().strftime('%Y-%m-%d %H:%M:%S \n\n')}"
    self.wfile.write(message.encode())
    self.wfile.write(calendar.calendar(2022, 2, 1, 6).encode())


    return


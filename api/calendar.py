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
    self.wfile.write(result.encode())
    self.wfile.write('Scheme : ' + result.scheme.encode())
    self.wfile.write('HostName : ' + result.hostname.encode())
    self.wfile.write('Query : ' + result.query.encode())


    

    message1 = 'This is the datetime Year/Month/Day/Number of Week/Hour/Minute/Second: ' +'\n'
    message2 = 'This is the Calendar for year 2022: ' +'\n\n'

    self.wfile.write(message1.encode())
    self.wfile.write(str(datetime.now().strftime('%Y-%m-%d/%W/ %H:%M:%S \n')).encode())
    self.wfile.write(message2.encode())
    self.wfile.write(calendar.calendar(2022, 2, 1, 6).encode())
    url.params
    self.wfile.write(url.query.encode())
    return

'''import urllib.parse
sample_url = "http://example.com:8080/example.html?val1=1&val2=Hello"
# Parse URL with urlparse()
result = urllib.parse.urlparse(sample_url)
print(result)
# Output
# ParseResult(scheme='http', netloc='example.com:8080', path='/example.html', params='', query='val1=1&val2=Hello', fragment='')
print("Scheme : " + result.scheme)
print("HostName : " + result.hostname)
print("Path : " + result.path)
# Output
# Scheme : http
# HostName : example.com
# Path : /example.html
print(result.geturl())
# Output
# http://example.com:8080/example.html?val1=1&val2=Hello
result = urllib.parse.urlsplit(sample_url)
print(result)
# Output
# SplitResult(scheme='http', netloc='example.com:8080', path='/example.html', query='val1=1&val2=Hello', fragment='')
urljoin() construct a absolute URL by combining a base URL with another URL. It uses addressing scheme, the network location to provide missing components in the relative URL. For example:

import urllib.parse
# Join URL with urljoin()
print(urllib.parse.urljoin('http://example.com:8080/example.html', 'FAQ.html'))
# Output
# http://example.com:8080/FAQ.html
Quoting URL
URL quoting module provides functions to make program data safe for use as URL components by quoting special characters and appropriately encoding non-ASCII text. It also support reversing these operations to recreate the original data from the contents of a URL component.

quote() function replace special characters in string using the %xx escape. It is intended for quoting the path section of URL. quote_plus() is similar to quote(), but it replace spaces by plus signs. Plus signs in the original string are escaped unless they are included in safe. To get back the URL from the quoted url, use unquote(). It %xx escapes by their single-character equivalent. unquote_plus() is similar to unquote(), but also replace plus signs by spaces, as required for unquoting HTML form values. Syntax of above functions

quote(string, safe='/', encoding=None, errors=None)
quote_plus(string, safe='', encoding=None, errors=None)
unquote(string, encoding='utf-8', errors='replace')
unquote_plus(string, encoding='utf-8', errors='replace')
Following example demonstrate quoting of program data, so that they can be used as component of URL.

import urllib.parse
sample_string = "Hello El Niño"
# Replaces special characters for use in URLs
quoteStr = urllib.parse.quote(sample_string)
print(quoteStr)
# Output
# Hello%20El%20Ni%C3%B1o
# Replaces special characters for use in URLs
quotePlusStr = urllib.parse.quote_plus(sample_string)
print(quotePlusStr)
# Output
# Hello+El+Ni%C3%B1o
# Get back actual string from quoted string
print(urllib.parse.unquote(quoteStr))
# Output
# Hello El Niño
print(urllib.parse.unquote_plus(quotePlusStr))
# Output
# Hello El Niño
Manipulating Query Parameter
urlencode() convert a mapping object or a sequence of two-element tuples to a percent-encoded ASCII text string. It returns string containing series of key=value pairs separated by ‘&’ characters, where both key and value are quoted. The order of parameters in the encoded string will match the order of parameter tuples in the sequence. To reverse encoding process, use parse_qs() and parse_qsl() to parse query strings into Python data structures. Syntax of the function are

urllib.parse.urlencode(query, doseq=False, safe='', encoding=None, errors=None, quote_via=quote_plus)
urllib.parse.parse_qs(qs, keep_blank_values=False, strict_parsing=False, encoding='utf-8', errors='replace', max_num_fields=None)
urllib.parse.parse_qsl(qs, keep_blank_values=False, strict_parsing=False, encoding='utf-8', errors='replace', max_num_fields=None)
parse_qs() parse a query string given as a string argument and returns a dictionary. Dictionary keys are the unique query variable names and the values are lists of values for each name. parse_qsl() parse a query string given as a string argument and returs as a list of name, value pairs.

import urllib.parse
# Use urlencode() to convert maps to parameter strings
query_data = {
    'name': "Mango",
    "type": "Fruit",
    "price": 37
}
result = urllib.parse.urlencode(query_data)
print(result)
# Output
# name=Mango&type=Fruit&price=37
print(urllib.parse.parse_qs(result))
# Output
# {'name': ['Mango'], 'type': ['Fruit'], 'price': ['37']}
print(urllib.parse.parse_qsl(result))
# Output
# [('name', 'Mango'), ('type', 'Fruit'), ('price', '37')]
Related Posts
Opening URLs in Python
Reading and Writing JSON in Python
Working with Temporary Files in Python
String Representation of Class Object in Python
Generate Universally Unique Identifiers in Python

 
Categories: Programming|Tags: PYTHON
Sharing is Caring !
Facebook
Twitter
Reddit
LinkedIn
WhatsApp
Tumblr
Pinterest
Email
 Subscribe 
guest
300


{}[+]
0 COMMENTS

 

 
© 2018 - 2022 mymusing
FacebookTwitterInstagramPinterest
Go to Top
'''
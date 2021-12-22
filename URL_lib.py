'''
U = Uniform
R = Resource
L = Locator

Protocol: http, https, ftp, ...
Host
Port: http=80, https=443
Path
Querystring: key=value&life=42
Fragment


urllib

5 modules:
request
response
error
parse
robotparser

'''

from urllib import request

resp = request.urlopen("https://www.ottburg.de")
# print(type(resp))
# print(resp.code)
# print(resp.length)
# print(resp.peek())

data = resp.read()
print(type(data))
print(len(data))
html = data.decode("UTF-8")
print(type(html))
print(html)


from urllib import request
from urllib import parse

# resp = request.urlopen("https://www.google.com/search?q=socratica")
params = {"v": "EuC-yVzHhmI", "t": "5m56s"}
querystring = parse.urlencode(params)
print(querystring)
url = "https://www.youtube.com" + "?" + querystring
resp = request.urlopen(url)
print(resp.isclosed())
print(resp.code)
html = resp.read().decode("utf-8")
print(html[:500])
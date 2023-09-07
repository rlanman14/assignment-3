import urllib.request

url = 'https://s3.amazonaws.com/tcmg476/http_access_log'
filename = 'log.txt'

urllib.request.urlretrieve(url, filename)
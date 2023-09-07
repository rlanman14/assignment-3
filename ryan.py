import urllib.request
#import request module (on PSL)

url = 'https://s3.amazonaws.com/tcmg476/http_access_log'
#specify url
filename = 'log.txt'
#name dowloaded file

#download file
urllib.request.urlretrieve(url, filename)

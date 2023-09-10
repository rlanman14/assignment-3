import urllib.request
#import request module (on PSL)

url = 'https://s3.amazonaws.com/tcmg476/http_access_log'
#specify url
filename = 'log.txt'
#name dowloaded file

#download file
urllib.request.urlretrieve(url, filename)

#check if the file exists locally
try:
    with open(filename, 'r') as file:
        print(f"Local copy '{filename}' already exists. Skipping download.")
except FileNotFoundError:
    # If the file doesn't exist locally, download it
    urllib.request.urlretrieve(url, filename)
    print(f"Downloaded '{filename}' from the internet.")
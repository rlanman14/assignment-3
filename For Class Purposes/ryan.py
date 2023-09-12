# Step one, checking if code is existant and downloaded if not
import urllib.request
import os

url = 'https://s3.amazonaws.com/tcmg476/http_access_log'
filename = 'log.txt'

# Check if the file already exists
if os.path.exists(filename):
    print(f"The file '{filename}' already exists.")
else:
    print(f"Downloading '{filename}'...")
    urllib.request.urlretrieve(url, filename)
    print(f"'{filename}' has been downloaded.")

# rest of the code will go after this
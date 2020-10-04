import requests
import hashlib
import re

url="http://docker.hackthebox.eu:30512/"

req = requests.session()
out= req.get(url)
out=re.search("<h3 align='center'>+.*?</h3>",out.text)
out=re.search("'>.*<",out[0])
out=re.search("[^|'|>|<]...................",out[0])

out=hashlib.md5(out[0].encode('utf-8')).hexdigest()

print("sending md5 :-{}".format(out))

data={'hash': out}
out = req.post(url = url, data = data)

print(out.text)
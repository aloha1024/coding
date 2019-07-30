import requests
import base64
url='http://ctf5.shiyanbar.com/web/10/10.php'
r=requests.get(url)
flag=base64.b64decode(r.headers['flag']).split(':')[1]
val={'key':flag}
u=requests.post(url=url,data=val)
print u.text
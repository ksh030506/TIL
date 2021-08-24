import requests
import json

url = "https://kauth.kakao.com/oauth/token"

data = {
    "grant_type": "authorization_code",
    "client_id": "475eeac2ef5afa6af598830e6720ecc6",
    "redirect_uri": "https://localhost.com",
    "code": ""

}
response = requests.post(url, data=data)

tokens = response.json()

print(tokens)

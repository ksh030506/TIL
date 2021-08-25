import requests
import json

url = "https://kauth.kakao.com/oauth/token"

data = {
    "grant_type": "authorization_code",
    "client_id": "475eeac2ef5afa6af598830e6720ecc6",
    "redirect_uri": "https://localhost.com",
    "code": "aNiJfi0wijzqTxBEWW3CwmCvAmbwsDJ_NnRQrfSGoQTzZxz2VqEirlsJouzd4uKOFyD02Ao9c00AAAF7escZWA"

}
response = requests.post(url, data=data)

tokens = response.json()

print(tokens)

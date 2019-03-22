import requests
from bs4 import BeautifulSoup

BASE_LOGIN_URL = "http://172.16.2.1:1000"
HEADER_KEY = "41665a725d5a5fb0"

login_url = BASE_LOGIN_URL + "/login?" + HEADER_KEY
response = requests.get(login_url)
soup = BeautifulSoup(response.text, "html.parser")
authenticate = soup.find("input", {"name":"magic"})

login_data = {"4Tredir":  login_url,
              "magic":    authenticate["value"],
              "username": "17bcs1752",
              "password": "geez :)"}

response = requests.post(BASE_LOGIN_URL, data=login_data)
print(response.text)

import requests
from bs4 import BeautifulSoup

BASE_LOGIN_URL = "http://172.16.2.1:1000"

response = requests.get("http://detectportal.firefox.com/success.txt")
soup = BeautifulSoup(response.text, "html.parser")
authenticate = soup.find("input", {"name":"magic"})
login_url = BASE_LOGIN_URL + "/login?" + authenticate["value"]
print(login_url)

login_data = {"4Tredir":  "http://172.16.2.1:1000/login?423cd10a8af91a52",
              "magic":    "453ad60181fe2d2a",
              "username": "17bcs1752",
              "password": "geez :)"}

response = requests.post(BASE_LOGIN_URL, data=login_data)
print(response.text)

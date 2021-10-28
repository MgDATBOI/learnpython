import requests  # pip3 install requests

url = "https://www.google.com"

print(requests.get(url).text.split("href=")[1])
print(requests.get(url).text.split("href=")[1].split(">")[0])

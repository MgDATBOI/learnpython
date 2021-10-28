from bs4 import BeautifulSoup
import requests

url = "https://weather.com/weather/today/l/94087"
html = requests.get(url).text
soup = BeautifulSoup(html, "html.parser")

temp = soup.find_all("span", {"class": "CurrentConditions--tempValue--1RYJJ"})[0]
# print(temp.text)
print(f"The current temperature for {url.split('/')[-1]} is {temp.text}")

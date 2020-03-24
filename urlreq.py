import requests
from bs4 import BeautifulSoup

r = requests.get("https://www.otempo.pt/porto.html", {"User-agent": "XY"})
content = r.content
soup = BeautifulSoup(content, "html.parser")

all = soup.find_all("span", {"class": "m_table_weather_day_max_temp"})
today_temp = all[0].find_all("span")[0].text
today = ''.join(e for e in today_temp if e.isalnum())
f = open("todaysTemMax.txt", "w+")
f.write(today)
f.close()

# print(all)

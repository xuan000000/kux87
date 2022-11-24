import requests
from bs4 import BeautifulSoup
url = "https://www1.pu.edu.tw/~tcyang/course.html"
Data = requests.get(url)
#print(Data.text)
sp = BeautifulSoup(Data.text, "html.parser")
result=sp.select("a")
#print(result)
info = ""
for item in result:
	info += item.text + "\n\n"
print(info)

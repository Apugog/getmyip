import requests
import bs4

res = requests.get('https://ipinfo.info/html/ip_checker.php')
soup=bs4.BeautifulSoup(res.text, 'lxml')
k=soup.find_all('b')
print(k[0].text)
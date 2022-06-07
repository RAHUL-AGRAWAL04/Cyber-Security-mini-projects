import requests
import random,time
from bs4 import BeautifulSoup as bs

def get_free_proxies():
    url = "https://free-proxy-list.net/"
    soup = bs(requests.get(url).content, "html.parser")
    proxies = []
    for row in soup.find("table", attrs={"id": "proxylisttable"}).find_all("tr")[1:]:
        tds = row.find_all("td")
        try:
            ip = tds[0].text.strip()
            port = tds[1].text.strip()
            host = f"{ip}:{port}"
            proxies.append(host)
        except IndexError:
            continue
    return proxies

proxies = get_free_proxies()
#proxies = ['127.0.0.1:8080'] #add proxies to this list if you have list of live proxies
#print(proxies)

def get_session(proxies):
    # construct an HTTP session
    session = requests.Session()
    # choose one random proxy
    proxy = random.choice(proxies)
    session.max_redirects = 60
    session.proxies = {"http": 'http://'+proxy, "https": 'http://'+proxy}
    return session

while True:
    s = get_session(proxies)
    try:
        print("Request page with IP:", s.get("http://www.chegg.com/", timeout=15).text)
    except Exception as e:
        continue
    time.sleep(random.randint(1,5))
    

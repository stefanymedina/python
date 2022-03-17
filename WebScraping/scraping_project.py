import requests
from bs4 import BeautifulSoup

all_q = []
response = requests.get("http://quotes.toscrape.com")
soup = BeautifulSoup(response.text, "html.parser")
quotes = soup.find_all(class_="quote")
for q in quotes:
    all_q.append({
        'text': q.find(class_='text').get_text(),
        'author': q.find(class_='author').get_text(),
        'bio-link': q.find("a")["href"]
    })
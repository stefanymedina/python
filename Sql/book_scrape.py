import sqlite3
import requests
from bs4 import BeautifulSoup

# Request Url
def scrape_url(url):
    re = requests.get(url)
    soup = BeautifulSoup(re.text, "html.parser")
    books = soup.find_all("article")
    book_list = []
    for book in books:
        book_data = (get_title(book),get_price(book), get_rating(book))
        book_list.append(book_data)
    print(book_list)
    
def get_title(book):
    return book.find("h3").find("a")["title"]

def get_price(book):
    price = book.select(".price_color")[0].get_text()
    return float(price.replace("Â", "").replace("£", ""))

def get_rating(book):
    rating = {"Zero":0, "One":1, "Two":2,"Three":3, "Four":4, "Five":5 }
    par = book.select(".star-rating")[0]
    word = par.get_attribute_list("class")[1]
    return rating[word]
# Initializa Bs
# Extract Data we Want
# Save data to db 
url = "https://books.toscrape.com/catalogue/category/books/history_32/index.html"
scrape_url(url)


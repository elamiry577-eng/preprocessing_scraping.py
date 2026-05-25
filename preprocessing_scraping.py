import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://quotes.toscrape.com/"
response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")

quotes = []
authors = []

for quote in soup.find_all("div", class_="quote"):
    quotes.append(quote.find("span", class_="text").get_text())
    authors.append(quote.find("small").get_text())

df = pd.DataFrame({
    "Quote": quotes,
    "Author": authors
})

df.to_csv("cleaned_dataset.csv", index=False)

print(df.head())
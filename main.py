from bs4 import BeautifulSoup
import requests

# Access and return the source from a web page
page_to_scrape = requests.get("https://quotes.toscrape.com")

# Use BeautifulSoup's HTML parser to convert it into an object
soup = BeautifulSoup(page_to_scrape.text, "html.parser")

# Find all quotes on the web page based on HTML tag and ClASS
# Return them as tuples
quotes = soup.find_all("span",attrs={"class":"text"})
authors = soup.find_all("small",attrs={"class":"author"})

# Loop through the tuples in tandem using the zip function
# Present the data to the user 
for quotes, author in zip(quotes, authors):
    print(quotes.text + "\n" +"-"+author.text +"\n")


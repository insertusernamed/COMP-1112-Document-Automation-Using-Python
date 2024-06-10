import requests
from bs4 import BeautifulSoup

# URL of the web page we want to scrape
url = "https://example.com"

# Sending a GET request to the web page
response = requests.get(url)

# Checking if the request was successful
if response.status_code == 200:
    # Parsing the HTML content of the page
    soup = BeautifulSoup(response.content, "html.parser")

    # Extracting the data - example: in this case, extracting all headings
    headings = soup.find_all("h1")
    for heading in headings:
        print(heading.text)

    # Extracting the data - example: in this case, extracting all links
    links = soup.find_all("a")
    for link in links:
        print(link.get("href"))
else:
    print("Failed to retrieve the web page. Status code:", response.status_code)

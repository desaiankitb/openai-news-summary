import requests
from bs4 import BeautifulSoup

class NewsCMSParser:
    def __init__(self, url):
        self.url = url
        self.cleaned_url = self.clean_url()

    def clean_url(self):
        # Remove any query parameters from the URL
        cleaned_url = self.url.split('?')[0]
        return cleaned_url

    def extract_header(self, soup):
        header = soup.find('h1').text.strip()
        return header

    def extract_text(self, soup):
        text = ""
        paragraphs = soup.find_all('p')
        for p in paragraphs:
            text += p.text.strip() + " "
        return text.strip()

    def parse(self):
        # Send a GET request to the URL and retrieve the HTML content
        response = requests.get(self.cleaned_url)
        html_content = response.text

        # Create a BeautifulSoup object for parsing the HTML
        soup = BeautifulSoup(html_content, 'html.parser')

        # Extract the header and text
        header = self.extract_header(soup)
        text = self.extract_text(soup)

        return header, text

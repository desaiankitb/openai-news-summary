import os
import argparse
from src.news.news_cms_parser import NewsCMSParser

def parseUrl(url):
    # Create an instance of the NewsCMSParser class
    parser = NewsCMSParser(url)

    # Parse the URL and retrieve the header and text
    header, text = parser.parse()

    return header, text

if __name__ == '__main__':
    # Parse command-line arguments
    parser = argparse.ArgumentParser(description='News CMS Parser')
    parser.add_argument('--url', required=True, help='URL to parse')
    args = parser.parse_args()

    # Get the URL from command-line arguments
    url = args.url

    # Call the main function
    header, text = parseUrl(url)

    # Print the results
    print("Header:", header)
    print("Text:", text)


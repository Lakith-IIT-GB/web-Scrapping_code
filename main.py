import requests
import pdfkit
from bs4 import BeautifulSoup
from weasyprint import HTML, CSS

def scrape_and_convert_to_pdf(url):
    """
    Scrapes a website from the given URL and converts the content to a PDF file.
    
    Parameters:
    url (str): The URL of the website to scrape.
    """
    # Fetch the webpage content
    response = requests.get(url)
    html_content = response.content

    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(html_content, 'html.parser')

    # Extract the relevant content from the webpage
    content = soup.find('div', {'class': 'main-content'})

    # Convert the HTML content to a PDF using WeasyPrint
    HTML(string=str(content)).write_pdf('output.pdf')
    pdfkit.from_string(str(content), 'output.pdf')

    print('PDF file "output.pdf" created successfully.')

def main():
    url = input("Enter the website URL: ")
    scrape_and_convert_to_pdf(url)

if __name__ == "__main__":
    main()
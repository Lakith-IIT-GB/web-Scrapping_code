import requests
from bs4 import BeautifulSoup
from weasyprint import HTML, CSS

def scrape_and_convert_to_pdf(url):
    try:
        # Fetch webpage with timeout
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        
        # Parse HTML
        soup = BeautifulSoup(response.content, 'html.parser')
        
    
        # Find content
        content = soup.find('div', {'class': 'main-content'})
        if not content:
            raise ValueError("Could not find main-content div")
            
        # Generate PDF
        HTML(string=str(content)).write_pdf('output.pdf')
        print('PDF file "output.pdf" created successfully.')
        
    except requests.RequestException as e:
        print(f"Error fetching URL: {e}")
    except ValueError as e:
        print(f"Error extracting content: {e}")
    except Exception as e:
        print(f"Error creating PDF: {e}")

def main():
    url = input("Enter the website URL: ")
    scrape_and_convert_to_pdf(url)

if __name__ == "__main__":
    main()
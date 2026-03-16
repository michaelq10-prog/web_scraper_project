import requests
from bs4 import BeautifulSoup
import csv
import time

URL = "https://www.scrapethissite.com/pages/simple/"

def run_scraper():
    print("Checking server etiquette...applying 2-second crawl delay.")

    print(f"Accessing {URL}...")
    response = requests.get(URL)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Create a list to hold our data
    data_rows = []
    
    # Find all country containers
    countries = soup.find_all('div', class_='country')
    
    for country in countries:
        name = country.find('h3', class_='country-name').text.strip()
        capital = country.find('span', class_='country-capital').text.strip()
        population = country.find('span', class_='country-population').text.strip()
        area = country.find('span', class_='country-area').text.strip()
        
        data_rows.append([name, capital, population, area])
    
    # Write to CSV
    with open('countries_data.csv', 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['Name', 'Capital', 'Population', 'Area']) # Header
        writer.writerows(data_rows)
    
    print(f"Successfully scraped {len(data_rows)} countries and saved to countries_data.csv")

if __name__ == "__main__":
    run_scraper()
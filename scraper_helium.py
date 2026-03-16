from helium import *
import csv
import time

# URL that requires JavaScript to load table data
URL = "https://www.scrapethissite.com/pages/ajax-javascript/"

def run_dynamic_scraper():
    print(f"Launching browser to {URL}...")
    
    # 1. Start Chrome (Headed mode so you can see it work)
    start_chrome(URL, headless=False)
    
    # 2. Wait for the '2015' link to appear (proves JS loaded)
    print("Waiting for dynamic content...")
    wait_until(Link('2015').exists)
    
    # 3. Click the year 2015
    click('2015')
    
    # 4. Wait for the table to populate with film data
    wait_until(S('.table').exists)
    time.sleep(1) # Brief pause for smooth rendering
    
    # 5. Extract movie titles using Helium's selector find
    print("Extracting dynamic data...")
    titles = [item.web_element.text for item in find_all(S('.film-title'))]
    
    # 6. Save results to a separate CSV
    with open('dynamic_helium_data.csv', 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['Film Title'])
        for title in titles:
            writer.writerow([title])
            
    print(f"Success. Scraped {len(titles)} entries.")
    kill_browser()

if __name__ == "__main__":
    run_dynamic_scraper()
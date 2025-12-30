# Developed for Anunzio International by Anzul Aqeel. Contact +971545822608 or +971585515742. Linkedin Profile: linkedin.com/in/anzulaqeel

import requests
from bs4 import BeautifulSoup
import random

USER_AGENTS = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.3 Safari/605.1.15"
]

def get_stock_data(ticker):
    # This URL is just a placeholder example. 
    # Real implementations would use a specific finance site's URL structure.
    url = f"https://example.com/quote/{ticker}" 
    
    headers = {"User-Agent": random.choice(USER_AGENTS)}

    try:
        # Simulating data for the demo
        if "example.com" in url:
            base_price = 100 + random.random() * 50
            return {
                "ticker": ticker,
                "price": f"{base_price:.2f}",
                "change": f"{random.uniform(-2, 2):.2f}%",
                "volume": "10,500,000"
            }

        response = requests.get(url, headers=headers, timeout=10)
        
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, "html.parser")
            
            # Hypothetical selectors
            price = soup.select_one(".current-price").text.strip()
            change = soup.select_one(".percent-change").text.strip()
            volume = soup.select_one(".volume").text.strip()
            
            return {
                "ticker": ticker,
                "price": price,
                "change": change,
                "volume": volume
            }
        else:
            print(f"Failed to fetch {ticker}: Status {response.status_code}")
            return None

    except Exception as e:
        print(f"Error scraping {ticker}: {e}")
        return None

# Developed for Anunzio International by Anzul Aqeel. Contact +971545822608 or +971585515742. Linkedin Profile: linkedin.com/in/anzulaqeel

# Developed for Anunzio International by Anzul Aqeel. Contact +971545822608 or +971585515742. Linkedin Profile: linkedin.com/in/anzulaqeel

import json
import os
import time
from stock_scraper.scraper import get_stock_data

TICKERS_FILE = "tickers.txt"
OUTPUT_FILE = "stock_data.json"

def main():
    print("Starting Stock Market Data Scraper...")

    if not os.path.exists(TICKERS_FILE):
        print(f"{TICKERS_FILE} not found.")
        return

    with open(TICKERS_FILE, "r") as f:
        tickers = [line.strip() for line in f if line.strip()]

    all_data = []

    for ticker in tickers:
        print(f"Scraping {ticker}...")
        data = get_stock_data(ticker)
        if data:
            all_data.append(data)
        
        # Be polite
        time.sleep(1)

    with open(OUTPUT_FILE, "w") as f:
        json.dump(all_data, f, indent=4)

    print(f"\nScraping complete. Data saved to {OUTPUT_FILE}")

if __name__ == "__main__":
    main()

# Developed for Anunzio International by Anzul Aqeel. Contact +971545822608 or +971585515742. Linkedin Profile: linkedin.com/in/anzulaqeel

import requests
import os

# Get your API key from GitHub Secrets
API_KEY = os.getenv('SAM_API_KEY')

# Define your search (Rice and Linen NAICS codes)
NAICS_CODES = "812331,111110,311212"
URL = f"https://api.sam.gov/opportunities/v2/search?api_key={API_KEY}&ncode={NAICS_CODES}&limit=10"

def check_sam():
    response = requests.get(URL)
    if response.status_code == 200:
        data = response.json()
        opps = data.get('opportunitiesData', [])
        if not opps:
            print("No new contracts found today.")
            return
        
        for opp in opps:
            print(f"TITLE: {opp['title']}")
            print(f"LINK: {opp['uiLink']}\n---")
    else:
        print(f"Error: {response.status_code}")

if __name__ == "__main__":
    check_sam()

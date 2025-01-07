import os
from dotenv import load_dotenv
import requests

load_dotenv()

url = "https://api.parcllabs.com/v1/market_metrics/5380879/housing_event_prices"
API_KEY=os.getenv('PARCL_LABS_API_KEY')

headers = {
    "accept": "application/json",
    "Authorization": "EKQ1MfyollOze1iG6lULB2k8bxSlO4Xo9zpoZ8tCFms"
}

response = requests.get(url, headers=headers)

try:
    with open("data.json", "w") as f:
        f.write(response.text)
except Exception:
    print('Could not write data to file')
finally:
    print(response.json)
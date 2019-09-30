import requests
from bs4 import BeautifulSoup

# Set header
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36'} 
result = requests.get("https://www.recreation.gov/camping/campgrounds/232449/availability", headers=headers)

print(result.status_code)

import requests
from bs4 import BeautifulSoup
import lxml

URL = 'https://www.amazon.com/dp/B01NBKTPTS?ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6&th=1'
headers = {
    'Accept-Language': 'en-US,en;q=0.5',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
}

response = requests.get(url=URL, headers=headers)
response.raise_for_status()

soup = BeautifulSoup(response.text, 'lxml')

print(soup.find('span', class_='a-offscreen').text)

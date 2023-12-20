import requests
from bs4 import BeautifulSoup
import lxml
import smtplib

my_fake_email = 'chungus3535@gmail.com'
password = 'abcd1357)('

my_other_fake_email = 'bungus6446@gmail.com'

URL = 'https://www.amazon.com/dp/B01NBKTPTS?ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6&th=1'

headers = {
    'Accept-Language': YOUR_ACCEPT_LANGUAGE,
    'User-Agent': YOUR_USER_AGENT
}

response = requests.get(url=URL, headers=headers)
response.raise_for_status()

soup = BeautifulSoup(response.text, 'lxml')

visual_price = soup.find('span', class_='a-offscreen').text

final_price = float(visual_price.split('$')[1])

SUBJECT = 'Amazon Price Alert!'

TEXT = f"Instant Pot Duo Plus 9-in-1 Electric Pressure Cooker, Slow Cooker, Rice Cooker, Steamer, Sauté, " \
       f"Yogurt Maker, Warmer & Sterilizer, Includes App With Over 800 Recipes, Stainless Steel, 6 Quart is now " \
       f"{visual_price.split('$')[1]}"

message = 'Subject: {}\n\n{}'.format(SUBJECT, TEXT)

if final_price <= 100.00:

    with smtplib.SMTP('smtp.gmail.com') as connection:
        connection.starttls()
        connection.login(user=my_fake_email, password=password)
        connection.sendmail(from_addr=my_fake_email, to_addrs=my_other_fake_email,
                            msg=f"Instant Pot Duo Plus 9-in-1 Electric Pressure Cooker, Slow Cooker, Rice Cooker, "
                                f"Steamer, Sauté, Yogurt Maker, Warmer & Sterilizer, Includes App With Over 800 Recipes,"
                                f" Stainless Steel, 6 Quart is now {visual_price.split('$')[1]}")

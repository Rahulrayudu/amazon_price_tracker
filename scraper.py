import requests
from lxml import html
import smtplib, ssl
import getpass
import time
def check_price():
    URL = "https://www.amazon.in/Noise-Wireless-Bluetooth-30-Hours-Instacharge/dp/B09Y5MK1KB/ref=sr_" \
          "1_5?keywords=noise+vs104&qid=1656651961&sprefix=noise+vs%2Caps%2C223&sr=8-5"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.53 Safari/537.36',
        'Accept-Encoding':  None
    }
    page = requests.get(URL,headers=headers)
    tree = html.fromstring(page.content)
    price = tree.xpath('//span[@class="a-price-whole"]/text()')[0]
    return int(float(price.replace(',','')))

def email_price(price):
    # add the mail and password
    smtp_server = "smtp.gmail.com"
    port = 587  # For starttls
    sender_email = "rahulsandireddy03@gmail.com"
    password = "nzpmwmugscsbfian"

    # Create a secure SSL context
    context = ssl.create_default_context()

    # Try to log in to server and send email
    try:
        server = smtplib.SMTP(smtp_server, port)
        server.ehlo()  # Can be omitted
        server.starttls(context=context)  # Secure the connection
        server.ehlo()  # Can be omitted
        server.login(sender_email, password)
        message= f'price is now {price}'
        server.sendmail(sender_email,sender_email,message)

    except Exception as e:
        # Print any error messages to stdout
        print(e)
    finally:
        server.quit()

if __name__ == "__main__":
    while(True):
        price = check_price()
        if (price) < 1200:
            email_price(price)
    time.sleep(86400)


import time
import requests
from bs4 import BeautifulSoup

url = 'https://www.amazon.com/gp/product/B07P4HBRMV/?smid=ATVPDKIKX0DER'
target_price = 20

headers = {
#'authority': ' www.amazon.com',
'method': 'GET',
#'path': ' /gp/product/B07P4HBRMV/?smid=ATVPDKIKX0DER',
'scheme': 'https',
'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
'accept-encoding': 'gzip, deflate, br, zstd',
'accept-language': 'en-US,en;q=0.9',
'cache-control': 'max-age=0',
#'cookie': ' aws-target-data=%7B%22support%22%3A%221%22%7D; aws-target-visitor-id=1733941953964-356576.44_0; aws-ubid-main=272-2565514-0875027; regStatus=registered; AMCV_7742037254C95E840A4C98A6%40AdobeOrg=1585540135%7CMCIDTS%7C20150%7CMCMID%7C16494387552182420352544178679129695783%7CMCAAMLH-1741538239%7C7%7CMCAAMB-1741538239%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1740940639s%7CNONE%7CMCAID%7CNONE%7CvVersion%7C4.4.0; aws-userInfo-signed=eyJ0eXAiOiJKV1MiLCJrZXlSZWdpb24iOiJ1cy1lYXN0LTEiLCJhbGciOiJFUzM4NCIsImtpZCI6ImU4M2RhYjg3LWIwOTItNGU3Yy04ODI3LWI3NDM4NzU4NDg3ZiJ9.eyJzdWIiOiIiLCJzaWduaW5UeXBlIjoiUFVCTElDIiwiaXNzIjoiaHR0cDpcL1wvc2lnbmluLmF3cy5hbWF6b24uY29tXC9zaWduaW4iLCJrZXliYXNlIjoidStZXC83XC9UT2VLS29yTEVDVWxTbEdjUFNHZVlCRlBLZHMraEJqYitrZTFRPSIsImFybiI6ImFybjphd3M6aWFtOjo2NzcyNzYxMjEyMjM6cm9vdCIsInVzZXJuYW1lIjoibWljaGFlbCJ9.ze3h_ZpN1IaSvBxsib6oStMh5Vy-RStCSDzqKR7IOLt6tmc6g-TpJSmZbZb98VmG5HBA2uiO9xCsIKr1Wfxena2W-40G1TV-RVWOBhiYgotcPJHNfYqh6LGlrsKkQ_C1; aws-userInfo=%7B%22arn%22%3A%22arn%3Aaws%3Aiam%3A%3A677276121223%3Aroot%22%2C%22alias%22%3A%22%22%2C%22username%22%3A%22michael%22%2C%22keybase%22%3A%22u%2BY%2F7%2FTOeKKorLECUlSlGcPSGeYBFPKds%2BhBjb%2Bke1Q%5Cu003d%22%2C%22issuer%22%3A%22http%3A%2F%2Fsignin.aws.amazon.com%2Fsignin%22%2C%22signinType%22%3A%22PUBLIC%22%7D; csm-sid=388-6614395-5593224; x-amz-captcha-1=1741913160190791; x-amz-captcha-2=DtHvSANLo7iKH2yrhHlNkQ==; session-id=136-2323893-2555123; session-id-time=2082787201l; i18n-prefs=USD; ubid-main=130-1845579-2702744; session-token=zEUk3uCwm5dA0QUtZJm0WPb9vv6diBYON/cxHucVIwam/N1XKOcqdk/ny6Ai57bb4yDSF+OqfzIueOcVTH/a55aq9a+aGCEYUZ8wcP9MdKSMY0wVYCPpG0W7myi3SC/N9cWl66hjOiJLuDU5HipXLwJ9sEgRhtivisrBP4mz+oBz8lVCVZAg3846qaih9Rq19/8WJx89wP9lvlqNhrEq8HWZwaJU5pnjngLz8Dhlu32FG3sDrU4P4QUH8FyhTWZr36tt2LSgvtQkM6VASvWsheOJn432P6eTiGPZgUgW49IEI/alXtCbdLfw+Bit4MWL9l2pbwp6nhh6b81sOH10i/fF1LOLc1XQ;','csm-hit=tb': '7PQJ0FT9PNVR5DD9JFZE+s-7PQJ0FT9PNVR5DD9JFZE|1741906588870&t:1741906588870&adb:adblk_no',
'device-memory': '8',
'downlink': '9.4 ',
'dpr': '1.125 ',
'ect': '4g',
'priority': 'u=0, i',
#'referer': ' https://www.amazon.com/gp/product/B07P4HBRMV/?smid=ATVPDKIKX0DER',
'rtt': '50',
'sec-ch-device-memory': '8',
'sec-ch-dpr': '1.125',
'sec-ch-ua': '"Chromium";v="134", "Not: A-Brand";v="24", "Google Chrome";v="134"',
'sec-ch-ua-mobile': '?1',
'sec-ch-ua-platform': '"Android"',
'sec-ch-ua-platform-version': '"6.0"',
'sec-ch-viewport-width': '199',
'sec-fetch-dest': 'document',
'sec-fetch-mode': 'navigate',
'sec-fetch-site': 'same-origin',
'sec-fetch-user': '?1',
'upgrade-insecure-requests': '1',
'User-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Mobile Safari/537.36',
'viewport-width': '199',}  # complete the headers to make `requests` work
def fetch_page():
    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.text, "html.parser")
    if r.status_code == 200:
        html_content = r.text
        with open("amazon.html", "w", encoding="utf-8") as file:
            file.write(html_content)
    else:
        print("retrieval failed Code:", r.status_code)
        exit()
def price_pull():

    try:
        with open("amazon.html", "r", encoding="utf-8") as file:
            soup = BeautifulSoup(file, "html.parser")
            whole = soup.select_one("span.a-price-whole")
            fraction = soup.select_one("span.a-price-fraction")
        whole_text = whole.text.strip().replace(",","")
        fraction_text = fraction.text.strip()
        if len(fraction_text) == 1:
            fraction_text += "0"
        if whole and fraction:
            price_text = f"{whole_text}{fraction_text}"
            return float(price_text)
        else:
            print("Unable to find price! check HTML!")
            return None
    except Exception as e:
        print(f"Error extracting price from page: {e}")
        return None
def price_tracker(price_thresh=20.00, interval=10*60, days=7):
    total_num_of_checks = (days* 24 * 60) // 10

    for i in range(total_num_of_checks):
        fetch_page()
        price = price_pull()

        if price is not None:
            print(f"check {i+1}: Current Price - ${price}")

            if price <= price_thresh:
                print(f"Price has dropped to ${price} Buy while it is lower!")
                break
            else:
                print(f"Check {i+1}: Price not be found.")
            time.sleep(interval)

price_tracker()


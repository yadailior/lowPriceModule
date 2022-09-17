# -*- coding: utf-8 -*-
from googlesearch import search
from bs4 import BeautifulSoup
import ssl
import html2text
from urllib.request import Request, urlopen
import re

barcode = "OP-RD09-13430"

website_price = {}
counter = 0
for link in search(barcode, tld="co.in", num=7, stop=7, pause=2):
    if 'c-data' in link or "cms" in link or "visualdg" in link or "amtel" in link or "zap" in link:
        continue
    else:
        req = Request(link, headers={'User-Agent': ("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) " "AppleWebKit/537"
                                                    ".36 (KHTML, like Gecko) " "Chrome/35.0.1916.47")})
        try:
            web_page = urlopen(req, context=ssl._create_unverified_context()).read()
        except:
            continue
        soup = BeautifulSoup(web_page, "html.parser")
        option_tag_list = soup.find_all("option")
        numbers_option = []
        for option in option_tag_list:
            temp_number = re.findall('[0-9,]+', html2text.html2text(str(option)))
            for num in temp_number:
                if "," in num:
                    num = re.sub(',', '', num)
                    numbers_option.append(num)
                else:
                    numbers_option.append(num)

        html_text = html2text.html2text(str(soup))
        html_text1 = re.split("\n", html_text)
        clean_html = []
        for i in range(len(html_text1) - 1):
            if html_text1[i] == "" or html_text1[i] == " ":
                continue
            else:
                clean_html.append(html_text1[i])
        counter += 1
        res = True
        counter = 0
        while barcode not in clean_html[counter]:
            counter += 1
            if counter >= len(clean_html):
                res = False
                break
            else:
                continue
        if res:
            pass
        else:
            continue

        while "₪" not in clean_html[counter]:
            counter += 1
            if counter >= len(clean_html):
                res = False
                break
            continue

        while res:
            if "₪" in clean_html[counter]:
                pass
            else:
                counter += 1
                if counter >= len(clean_html):
                    res = False
                    break
                continue
            if len(option_tag_list) == 0:
                if len(re.findall('[0-9,]+', clean_html[counter])) > 0:
                    price = re.search('[0-9,]+', clean_html[counter]).group()
                    if "," in price:
                        price = re.sub(',', '', price)
                        website_price[link] = float(price)
                        break
                    else:
                        website_price[link] = float(price)
                        break

                else:
                    counter += 1
                    continue
            else:
                price = re.findall(r'\d{1,4}(?:[.,]\d{3})*(?:[.,]\d{2})?', clean_html[counter])
                clean_price = {}
                for p in price:
                    if len(p) < 3:
                        continue
                    if "," in p:
                        clean_price[p] = (re.sub(',', '', p))
                    else:
                        clean_price[p] = p
                for price in clean_price:
                    if clean_price[price] in numbers_option:
                        counter += 1
                        break
                    else:
                        website_price[link] = float(clean_price[price])
                        res = False
                        break

for url, price in website_price.items():
    if price == min(list(website_price.values())):
        print("*" * 80)
        print(barcode)
        print("*" * 80)
        print(f"{url}", f"price:{price}")
        print("-" * 80)


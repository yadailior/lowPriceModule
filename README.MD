
#Web Scraping For Low price.

## Installation
```bash
pip install googlesearch-python

pip install beautifulsoup4

pip install ssl

pip install html2text

pip install urllib3

pip install regex
```


##**Overview**

A Complete Module  To Reach The Lowest Price By Given Barcode.

1)Googlesearch library - usend to get links.

2)Bs4 library-used to convert html page into readable context.

3)Html2text library-used to convert html page into readable text.

4)Regex library-used to find specific symbol in line to find price.

The Module developed for Cdsoft company :https://www.cdsoft.co.il/index.php

###**Usage**
```python
# -*- coding: utf-8 -*-
from googlesearch import search
from bs4 import BeautifulSoup
import ssl
import html2text
from urllib.request import Request, urlopen
import re
```

###**How It Works:**

By insert specific barcode the Module get into Googlesearch and return,

The first 7 Urls, As you can see at the Module if the Url contain  words,

That are part of suppliers websites the Module ignore them because in these websites,

There prices are not given.

After that use Bs4 library to find all 'option' tags in html to ignore them later.

By using Html2text library to filter and set all the HTML text into list,

It made to go over each line in HTML text to find where the barcode appears,

Because after a little search the required price in most cases appears after barcode appears,

When the barcode is found the Module search for "¤" to seek for price,

If the number is not in "option_tag_list"-that contain all the prices that appear in "option" tags,

The number return as the price for the specific url.



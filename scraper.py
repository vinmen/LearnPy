import requests
import urllib.request
import time
from bs4 import BeautifulSoup

url1="https://"
response = requests.get(url1)
data = BeautifulSoup(response.content, "html.parser")
href_tags = data.find('table', id='registration-data-table').findAll('a', href=True)

url_file = open("url.txt", "w", encoding='utf-8')
out_file = open("out.txt", "w", encoding='utf-8')
error_file = open("error.txt", "w", encoding='utf-8')

for href in href_tags:
    url = href['href']
    try:
        
        response = requests.get(url)
        data = BeautifulSoup(response.content, "html.parser")
        
        p_tags = data.find('div', class_='registration-info').findAll('p')
        header = ''
        row = ''
        row_switch = False
        for p in p_tags:        
            if row_switch:
                row = row + p.get_text().replace("\r\n", ";").strip()  + ","
                row_switch = False
            else:
                header = header + p.get_text() + ","
                row_switch = True        
    
        out_file.write(header[:-1] + "\n")
        out_file.write(row[:-1] + "\n")

        url_file.write(url + "\n")
        time.sleep(1)        
    except:
        error_file.write(url + "\n")

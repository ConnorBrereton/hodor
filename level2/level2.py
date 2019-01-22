#!/usr/bin/python3
"""Module that executes HTTP POSt request"""

from bs4 import BeautifulSoup
import requests as rq

url = 'http://158.69.76.135/level2.php'
ua = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'

payload = {'id': '498', 'holdthedoor': 'Submit'}
header = {'Referer': url, 'User-Agent': ua}
cookies = {}

def vote():
    """Method that votes"""

    for i in range(1024):

        # check if server is up
        response = rq.get(url)
        if response != 200:
            print("HTTP response {}".format(response))

        # get the cookie from the header
        dom = BeautifulSoup(response.text, 'html.parser')
        cookie = dom.find('input', attrs={'name': 'key'})['value']
        print(cookie)

        # update cookies
        cookies.update({'HoldTheDoor': cookie})
        print(cookies)

        send = rq.post(url, data=payload, headers=header, cookies=cookies)
        print(send.text)
if __name__ == '__main__':
    vote()

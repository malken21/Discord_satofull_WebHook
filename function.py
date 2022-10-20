import urllib.request
import requests
import json


def setup_requests():
    opener = urllib.request.build_opener()
    opener.addheaders = [
        ('User-Agent', 'Mozilla/5.0'),
    ]
    urllib.request.install_opener(opener)


def getText(item):
    return item.text


def setCount(Config, value):
    Config['count'] = value
    file = open('Config.json', 'w')
    json.dump(Config, file, indent=4)


def sendDiscord(data, WebHook):
    requests.post(WebHook, json=data)

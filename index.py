from asyncio.windows_events import NULL
import urllib.request
from bs4 import BeautifulSoup
import json
import function
import main


Config = json.load(open('Config.json', 'r'))

function.setup_requests()
with urllib.request.urlopen(Config['url']) as res:
    html = res.read().decode('utf-8')
    html_parse = BeautifulSoup(html, 'html.parser')

    # コンテンツ取得
    content = list(map(function.getText, html_parse.find(
        'ul', class_='cf-DonationStatus__content').find_all('dd')))

    # Configのcountがint型だったら
    if (type(Config['count']) == int):
        # 合計人数取得 int型
        count = int(content[0].strip('人'))
        if (content[1] == '受付終了'):
            # 受付が終了したら実行
            main.send(html_parse, content, NULL, Config, count)
            function.setCount(Config, 'end')
        else:
            # 前回との合計人数の差を計算
            difference = count - Config['count']
            if (difference > 0):
                # 支援者が増えていたら実行
                main.send(html_parse, content, difference, Config, count)
                function.setCount(Config, count)

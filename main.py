import function


def send(html_parse, content, difference, Config, count):
    #------データ取得-----start#
    title = html_parse.find(
        'h1', class_='cf-Title3').text
    goal = html_parse.find(
        'dl', class_='cf-Article__summary__goal').find('dd').text
    total = html_parse.find(
        'dl', class_='cf-Article__summary__total').find('dd').text
    achievement = html_parse.find(
        'span', class_='cf-Meter__body').text
    #------データ取得-----end#

    print(title)
    print(goal)
    print(total)
    print(achievement)
    print(content[0])
    print(content[1])

    data = {}

    if (difference == None):
        data = {
            "embeds": [
                {
                    "title": "受付は終了しました",
                    "description": f"{total}/{goal}  ({achievement})  {count}人",
                    "color": 16753408
                }
            ],
            "username": title
        }
    else:
        print(f'追加: {difference}人')
        data = {
            "embeds": [
                {
                    "title": f"支援者が {difference}人 増えた!!",
                    "description": f"{total}/{goal}  ({achievement})  {count}人\n終了日: {content[1]}",
                    "color": 16753408
                }
            ],
            "username": title
        }

    [function.sendDiscord(data, WebHook) for WebHook in Config['Discord']]

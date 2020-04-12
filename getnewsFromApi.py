import datetime

import requests

from app import db
from models import News

URL = 'https://futurerussia.gov.ru/internal-api/api/pub/v1/components/materials?national_project_id=13&page=0'


def get_html(url):
    r = requests.get(url)

    return r


def main():
    newsJ = get_html(URL)
    if newsJ.ok:
        newsJ = newsJ.json()['content']['materials']
        for i in newsJ:
            if i['materialTypeTitle'] == 'Новость':

                date_pub = datetime.datetime.fromtimestamp(int(i['publish_date']))

                header = i['title']
                href = ('https://futurerussia.gov.ru/nacionalnye-proekty/{}').format(i['slug'])
                try:
                    news = News(pub_date=date_pub, news_header=header, news_href=href)
                    db.session.add(news)
                    db.session.commit()
                except:
                    print('Something wrong')


if __name__ == '__main__':
    main()

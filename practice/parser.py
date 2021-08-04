import requests
from bs4 import BeautifulSoup
#import json
import os

# 파이썬이 실행될때 DJANGO_SETTINGS_MODULE이라는 환경변수에
# 현재 프로젝트의 settings.py 파일 경로를 등록.
# websaver : 웹 보안관련 sw
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "websaver.settings")
# django를 import 해와서 parser.py를 장고와 연결.
import django
django.setup()
# jango의 모델(테이블)이나 다른 요소들의 import가 가능해진다.
# 모델 import
# from parsed_data.models import Data_By_Blog

# parser.py 파일의 위치를 jango에 등록.
BASE_DIR = os.path.dirname(os.path.abspath(__file__))



def parse_blog():
    req = requests.get('https://finance.naver.com/news/')
    html = req.text
    soup = BeautifulSoup(html, 'html.parser')
    titles = soup.select(
        '.main_news > ul >li >a'
        )
    data = {}
    # (i.text)

    for i in titles:
      data[i.text] = i.get('href')

    return data



    # for i in titles:
    #     data[i.text] = i.get('href')
    # return titles
print(parse_blog())
    # with open(os.path.join(BASE_DIR, 'result.json'), 'w') as json_file:
    #     json.dump(data, json_file)

# 인터프리터에서 직접 실행했을때 아래의 코드를 돌리라는 명령
# if __name__ =='__main__':
#     blog_data = parse_blog()
#     for i , j in blog_data.items():
#         Data_By_Blog(title=i, link=j).save()

import requests
import datetime
from bs4 import BeautifulSoup

def get_temperature():
    url = "https://weather.naver.com/"
    html = requests.get(url).text

    soup = BeautifulSoup(html, "html.parser")
    tags = soup.select(".current")
    tag = tags[0]
    return int(tag.text[-3:-1])

T = datetime.datetime.today()  # 한국 표준 시간
Koera_time = T.strftime('%c')    # 표준 시간을 원하는 포맷으로 문자열로 변환
f = open('temperature_record.txt',"a", encoding='utf-8')
f.write(Koera_time + " : " + str(get_temperature())+'\n')     # 각 날짜의 온도 저장
f.close()

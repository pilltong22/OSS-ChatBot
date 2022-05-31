import requests
from bs4 import BeautifulSoup

url = "http://www.sejong.ac.kr/unilife/institution_06.html"
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml")

title = "학생회관 학식 정보입니다.\n"
operatingTime_semester = "<학기중 운영시간>\n"
operatingTime_vacation = "<방학중 운영시간>\n"
menu = "<메뉴 구성>\n"
amount = "<금액>\n"

operating_semester = soup.select("#content > div.table_wrap > table > tbody > tr:nth-child(2) > td:nth-child(2) > ul > li")
for n in operating_semester:
    operatingTime_semester += n.text
    operatingTime_semester += "\n"

operating_vacation = soup.select("#content > div.table_wrap > table > tbody > tr:nth-child(2) > td:nth-child(3) > ul > li")
for n in operating_semester:
    operatingTime_vacation += n.text
    operatingTime_vacation += "\n"

menus = soup.select("#content > div.table_wrap > table > tbody > tr:nth-child(2) > td:nth-child(4) > ul > dt")
for n in menus:
    menu += n.text
    menu += "\n"

amount_txt = soup.select_one("#content > div.table_wrap > table > tbody > tr:nth-child(2) > td.last")
amount += amount_txt.text

response = {
    "version": "2.0",
    "template": {
        "outputs": [
            {
                "simpleText": {
                    "text": title + "\n" + operatingTime_semester + "\n" + operatingTime_vacation + "\n" + menu + "\n" + amount
                }
            }
        ]
    }   
}
import requests
from bs4 import BeautifulSoup

url = "http://board.sejong.ac.kr/boardlist.do?bbsConfigFK=335"
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml")

notices = soup.find_all("td", attrs={"class" : "subject"})

ans_txt = []
ans_link = []

for notice in notices:
    txt = notice.a.get_text()
    txt = txt.replace("\t","")
    txt = txt.replace("\n","")
    link = "http://board.sejong.ac.kr" + notice.a["href"]
    ans_txt.append(txt)
    ans_link.append(link)

response = {
    "version": "2.0",
    "template": {
        "outputs": [
  {
    "listCard": {
      "header": {
        "title": "세종대학교 학사공지입니다."
      },
      "items": [
        {
          "title": ans_txt[0],
          "link": {
            "web": ans_link[0]
          }
        },
        {
          "title": ans_txt[1],
          "link": {
            "web": ans_link[1]
          }
        },
          {
          "title": ans_txt[2],
          "link": {
            "web": ans_link[2]
          }
        }
      ],
        "buttons": [
        {
          "label": "더보기",
          "action": "webLink",
          "webLinkUrl": "http://board.sejong.ac.kr/boardlist.do?bbsConfigFK=335"
        }
      ]
    }
  }
]
}
}
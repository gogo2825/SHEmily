# -*- coding: utf-8 -*-

#----------------------
# chatbot
#----------------------

import os
from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route('/keyboard')
def Keyboard():

    dataSend = {
        "type" : "buttons",
        "buttons" : ["2캠퍼스"]
    }
    return jsonify(dataSend)


@app.route('/message', methods=['POST'])
def Message():

    dataReceive = request.get_json()
    content = dataReceive['content']

    if content == u"2캠퍼스":
        dataSend = {
            "message": {
                "text": "2캠퍼스 정보입니다."
            }
        }

    elif content == u"편의점":
        dataSend = {
            "message": {
                "text": "편의점은 본관 지하1층과 브니엘관 1층에 있습니다."
            }
        }
    elif content == u"도서관":
        dataSend = {
            "message": {
                "text": "도서관은 본관 3층에 있습니다."
            }
        }

    elif content == u"학식":
        dataSend = {
            "message": {
                "text": "학생식당은 본관 지하1층에 있습니다."
            }
        }

    elif content == u"학생식당":
        dataSend = {
            "message": {
                "text": "학생식당은 본관 지하1층에 있습니다."
            }
        }

    elif u"학식" and u"메뉴" in content:
        dataSend = {
            "message": {
                "text": "추후 추가 예정입니다."
            }
        }

    elif u"학생식당" and u"메뉴" in content:
        dataSend = {
            "message": {
                "text": "추후 추가 예정입니다."
            }
        }

    elif content == u"2학기":
        dataSend = {
            "message": {
                "text": "2017년 2학기는 9월 1일에 개강입니다."
            }
        }

    elif u"2학기" and u"개강" in content:
        dataSend = {
            "message": {
                "text": "2017년 2학기는 9월 1일에 개강입니다."
            }
        }

    elif content == u"전시회":
        dataSend = {
            "message": {
                "text": "2017년 범골제는 10월 26일 입니다."
            }
        }

    elif content == u"범골제":
        dataSend = {
            "message": {
                "text": "2017년 범골제는 10월 26일 입니다."
            }
        }

    elif u"전시회" and u"일정" in content:
        dataSend = {
            "message": {
                "text": "2017년 범골제는 10월 26일 입니다."
            }
        }

    elif u"범골제" and u"일정" in content:
        dataSend = {
            "message": {
                "text": "2017년 범골제는 10월 26일 입니다."
            }
        }


    elif content == u"기말고사":
        dataSend = {
            "message": {
                "text": "2017년 2학기 기말고사는 12월 15일~ 입니다."
            }
        }


    elif u"기말고사" and u"일정" in content:
        dataSend = {
            "message": {
                "text": "2017년 2학기 기말고사는 12월 15일~ 입니다."
            }
        }

    elif content == u"버스":
        dataSend = {
            "message": {
                "text": "버스 정보는 '셔틀탈래'앱을 이용해주세요. https://play.google.com/store/apps/details?id=ac.shinhan.ssb"
            }
        }


    elif u"버스" and u"시간" in content:
        dataSend = {
            "message": {
                "text": "버스 정보는 '셔틀탈래'앱을 이용해주세요. https://play.google.com/store/apps/details?id=ac.shinhan.ssb"
            }
        }

    else:
        dataSend = {
            "message": {
                "text": "내용 준비중입니다..."
            }
        }

    return jsonify(dataSend)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port = 5000)



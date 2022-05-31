import requests
from bs4 import BeautifulSoup
from flask import Flask, jsonify
import sys
import notices, foods
import cafe, bar, restaurant

application = Flask(__name__)

@application.route("/notice", methods=["GET", "POST"])
def notice():
    return jsonify(notices.response)

@application.route("/food_func", methods=["GET", "POST"]) #여기가 food_func
def food_func():
    return jsonify(foods.response)

@application.route("/kkagdug", methods=["GET", "POST"])
def kkagdug():
    return jsonify(restaurant.kkagdug)

@application.route("/hansot", methods=["GET", "POST"])
def hansot():
    return jsonify(restaurant.hansot)

@application.route("/eunhye", methods=["GET", "POST"])
def eunhye():
    return jsonify(restaurant.eunhye)

@application.route("/saebyeogjib", methods=["GET", "POST"])
def saebyeogjib():
    return jsonify(restaurant.saebyeogjib)

@application.route("/madangjogbal", methods=["GET", "POST"])
def madangjogbal():
    return jsonify(restaurant.madangjogbal)

@application.route("/boseunghoegwan", methods=["GET", "POST"])
def boseunghoegwan():
    return jsonify(restaurant.boseunghoegwan)

@application.route("/beune", methods=["GET", "POST"])
def beune():
    return jsonify(restaurant.beune)

@application.route("/algo", methods=["GET", "POST"])
def algo():
    return jsonify(restaurant.algo)

@application.route("/C156", methods=["GET", "POST"])
def C156():
    return jsonify(restaurant.C156)

@application.route("/rabbitHall", methods=["GET", "POST"])
def rabbitHall():
    return jsonify(restaurant.rabbitHall)

@application.route("/pizzaCompany", methods=["GET", "POST"])
def pizzaCompany():
    return jsonify(restaurant.pizzaCompany)

@application.route("/ingleside", methods=["GET", "POST"])
def ingleside():
    return jsonify(restaurant.ingleside)

@application.route("/haotsu", methods=["GET", "POST"])
def haotsu():
    return jsonify(restaurant.haotsu)

@application.route("/misig", methods=["GET", "POST"])
def misig():
    return jsonify(restaurant.misig)

@application.route("/honda", methods=["GET", "POST"])
def honda():
    return jsonify(restaurant.honda)

@application.route("/sushiBoom", methods=["GET", "POST"])
def sushiBoom():
    return jsonify(restaurant.sushiBoom)

@application.route("/happyBowl", methods=["GET", "POST"])
def happyBowl():
    return jsonify(restaurant.happyBowl)

@application.route("/chunmiHyang", methods=["GET", "POST"])
def chunmiHyang():
    return jsonify(restaurant.chunmiHyang)

@application.route("/romgok", methods=["GET", "POST"])
def romgok():
    return jsonify(cafe.romgok)

@application.route("/twosome", methods=["GET", "POST"])
def twosome():
    return jsonify(cafe.twosome)

@application.route("/bellong", methods=["GET", "POST"])
def bellong():
    return jsonify(cafe.bellong)

@application.route("/cafeHit", methods=["GET", "POST"])
def cafeHit():
    return jsonify(cafe.cafeHit)

@application.route("/bbackCoffee", methods=["GET", "POST"])
def bbackCoffee():
    return jsonify(cafe.bbackCoffee)

@application.route("/starbucks", methods=["GET", "POST"])
def starbucks():
    return jsonify(cafe.starbucks)

@application.route("/cafelong", methods=["GET", "POST"])
def cafelong():
    return jsonify(cafe.cafelong)

@application.route("/coffeeOnly", methods=["GET", "POST"])
def coffeeOnly():
    return jsonify(cafe.coffeeOnly)

@application.route("/gongcha", methods=["GET", "POST"])
def gongcha():
    return jsonify(cafe.gongcha)

@application.route("/jaksim", methods=["GET", "POST"])
def jaksim():
    return jsonify(cafe.jaksim)

@application.route("/blueMoon", methods=["GET", "POST"])
def blueMoon():
    return jsonify(cafe.blueMoon)

@application.route("/lang", methods=["GET", "POST"])
def lang():
    return jsonify(cafe.lang)

@application.route("/sailor", methods=["GET", "POST"])
def sailor():
    return jsonify(bar.sailor)

@application.route("/hwayangPocha", methods=["GET", "POST"])
def hwayangPocha():
    return jsonify(bar.hwayangPocha)

@application.route("/onggijonggi", methods=["GET", "POST"])
def onggijonggi():
    return jsonify(bar.onggijonggi)

@application.route("/hwasim", methods=["GET", "POST"])
def hwasim():
    return jsonify(bar.hwasim)

@application.route("/jejuolle", methods=["GET", "POST"])
def jejuolle():
    return jsonify(bar.jejuolle)

@application.route("/jinmag", methods=["GET", "POST"])
def jinmag():
    return jsonify(bar.jinmag)

@application.route("/jazzlounge", methods=["GET", "POST"])
def jazzlounge():
    return jsonify(bar.jazzlounge)

@application.route("/pomfritz", methods=["GET", "POST"])
def pomfritz():
    return jsonify(bar.pomfritz)

@application.route("/hansabari", methods=["GET", "POST"])
def hansabari():
    return jsonify(bar.hansabari)

@application.route("/zigzag", methods=["GET", "POST"])
def zigzag():
    return jsonify(bar.zigzag)

@application.route("/hongkong", methods=["GET", "POST"])
def hongkong():
    return jsonify(bar.hongkong)

@application.route("/jazz", methods=["GET", "POST"])
def jazz():
    return jsonify(bar.jazz)

if __name__ == "__main__":
    application.run(host='0.0.0.0', port=int(sys.argv[1]), debug=True)

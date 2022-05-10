import random
from Trade import Trade
from datetime import datetime


def tradeGenerator(assets, quantity):
    for i in range(quantity):
        asset = random.choice(assets)
        price = random.uniform(1.0, 100.0)
        date = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        trade = Trade()
        trade.asset = asset
        trade.price = price
        trade.date = date
        trade.save()

def listAllTradesOfAsset(asset):
    print(Trade.objects(asset=asset).to_json())

def tradesBiggerValue(price):
    return Trade.objects(price__gt=price).to_json()

def tradesBiggerValueOfAsset(asset, price):
    return Trade.objects(asset=asset, price__gt=price).to_json()

def tradesSmallerValue(price):
    return Trade.objects(price__lt=price).to_json()

def tradesSmallerValueOfAsset(asset, price):
    return Trade.objects(asset=asset, price__lt=price).to_json()

def lastTradeOfAssest(asset):
    return Trade.objects(asset=asset).order_by("-_id").first().to_json()

def lastTrade():
    return Trade.objects().order_by("-_id").first().to_json()

def averagePriceOfAsset(asset):
    sum = 0
    cont = 0
    for i in Trade.objects(asset=asset):
        sum += i.price
        cont += 1

    if cont == 0:
        return 0

    return round(sum / cont, 2)

def allTrades():
    return Trade.objects().to_json()

def totalTrades():
    return len(Trade.objects())
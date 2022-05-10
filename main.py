from util import *
from mongoengine import *


conection = connect(host = "mongodb://localhost:27017/db")
stockCodes = []
quantTrades = 0

print("\n\nInforme a lista de ativos que você deseja realizar os trades, informe 0 quanto todos os ativos forem informados: ")
while(True) :
    asset = input().upper()
    if asset == '0':
        break
    else:
        stockCodes.append(asset)

print("Informe a quantidade de trades que serão realizados: ")
quantity = int(input())
tradeGenerator(stockCodes, quantity)
print("Trades gerados\n\n")

while(True):
    print("Informe o dado que deseja obter:")
    print("Digite 0 para para sair do programa: ")
    print("Digite 1 para listar todos os trades de um determinado ativo:")
    print("Digite 2 para listar todos os trades com um preço de execução maior que algum valor passado:")
    print("Digite 3 para listar todos os trades de um determinado ativo com um preço de execução maior que algum valor passado:")
    print("Digite 4 para listar todos os trades com um preço de execução menor que algum valor passado:")
    print("Digite 5 para listar todos os trades de um determinado ativo com um preço de execução menor que algum valor passado:")
    print("Digite 6 para listar o Trade mais recente de um ativo específico:")
    print("Digite 7 para listar o Trade mais recente entre todos os Trades gerados:")
    print("Digite 8 para ver a média de preços dos trades de um determinado ativo:")
    print("Digite 9 para ver todas as operações realizadas:")
    print("Digite 10 para ver o total de operações realizadas:")
    value = int(input())


    if value == 0:
        break

    elif value == 1:
        print("Informe o ativo desejado: ")
        asset = input().upper()
        print("Trades realizados em:", asset)
        print(listAllTradesOfAsset(asset))
        print("\n\n")

    elif value == 2:
        print("Informe o valor desejado: ")
        price = input()
        print("Trades realizados com valor maior que", price)
        print(tradesBiggerValue(price))
        print("\n\n")

    elif value == 3:
        print("Informe o valor desejado: ")
        price = input()
        print("Informe o ativo desejado: ")
        asset = input().upper()
        print("Trades realizados com valor maior que", price, "no ativo:", asset)
        print(tradesBiggerValueOfAsset(asset, price))
        print("\n\n")

    elif value == 4:
        print("Informe o valor desejado: ")
        price = input()
        print("Trades realizados com valor menor que", price)
        print(tradesSmallerValue(price))
        print("\n\n")

    elif value == 5:
        print("Informe o valor desejado: ")
        price = input()
        print("Informe o ativo desejado: ")
        asset = input().upper()
        print("Trades realizados com valor menor que", price, "no ativo:", asset)
        print(tradesSmallerValueOfAsset(asset, price))
        print("\n\n")

    elif value == 6:
        print("Informe o ativo desejado: ")
        asset = input().upper()
        print("Trades mais recente no ativo:", asset)
        print(lastTradeOfAssest(asset))
        print("\n\n")

    elif value == 7:
        print("Trades mais recente")
        print(lastTrade())
        print("\n\n")

    elif value == 8:
        print("Informe o ativo desejado: ")
        asset = input().upper()
        print("Média de preços dos trades do ativo:", asset)
        print(averagePriceOfAsset(asset))
        print("\n\n")

    elif value == 9:
        print("Todas as operações realizadas:")
        print(allTrades())
        print(" ")
        print("Você tem um total de:", totalTrades(), "trades")
        print("\n\n")

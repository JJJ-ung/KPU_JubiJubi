import pyupbit
import requests
import json

class CoinInfo():
    data = requests.get("https://api.upbit.com/v1/market/all").json()

    accessKey = ""
    secretKey = ""
    acount

    def setKey(access, secret):
        print(access, secret)
        CoinInfo.accessKey = access
        CoinInfo.secretKey = secret
        acount = pyupbit.Upbit(CoinInfo.accessKey, CoinInfo.secretKey)
        if acount.get_balance() == None:
            acount = None
            print("Login Error")
        else:
            print("Login success")

    def SearchCoin(str):
        for coin in CoinInfo.data:
            if coin['market'].startswith("KRW"):
                if coin['market'].lower().endswith(str.lower()) or coin['korean_name'] == str or coin['english_name'].lower() == str.lower():
                    return coin

class Bitcoin():
    intervalTable = ["minute1", "minute3", "minute5", "minute10", "minute15", "minute30", "minute60", "minute240", "day", "week", "month"]

    def __init__(self, info):
        self.ticker = info['market']
        self.koreanName = info['korean_name']
        self.englishName = info['english_name']
        self.interval = "day"
        self.lstDailyData = list(pyupbit.get_ohlcv(self.ticker, count=6, interval=self.interval)['close']) # 날짜 오름차순
        self.lstDailyVolume = list(pyupbit.get_ohlcv(self.ticker, count=6, interval=self.interval)['volume'])
        self.chartData = list(pyupbit.get_ohlcv(self.ticker, interval=self.interval)['close'])
        self.graphData = pyupbit.get_ohlcv(self.ticker, count=100, interval="minute1")
        self.Low = list(self.graphData['low'])
        self.High = list(self.graphData['high'])
        self.Low.sort()
        self.High.sort(reverse = True)

    # 0.minute1, 1.minute3, 2.minute5, 3.minute10, 4.minute15, 5.minute30, 6.minute60, 7.minute240, 8.day, 9.week, 10.month
    def setInterval(self, cnt=8):
        self.interval = Bitcoin.intervalTable[cnt]
        self.chartData = list(pyupbit.get_ohlcv(self.ticker, interval=self.interval)['close'])

    def getPrice(self):
        return pyupbit.get_current_price(self.ticker)

    def getLow(self):
        return self.Low[0]

    def getHigh(self):
        return self.High[0]

    def getGraphData(self):
        return list(self.graphData['close'])
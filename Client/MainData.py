import Stock
import Bitcoin
import threading
from AppGUI import StatusFrame

class MainData(object):
    def __init__(self, UI):
        self.UI = UI   # 메인 UI 객체 담아둠
        self.CurrCoin = 0   # 현재 띄워진 비트코인
        self.CurrStock = 0  # 현재 띄워진 주식
        self.Favorites = [list(), list()]   # 즐겨찾기
        self.Compare = [list(), list()]  # 코인 비교목록
        self.BindUI()

    def BindUI(self):
        self.UI.StatusGUI.SearchButton.configure(command = lambda : self.Search(0))
        self.UI.StatusGUI.Searchbar.bind("<Return>", self.Search)

        self.CoinPage = self.UI.Pages['bitcoin']
        self.StockPage = self.UI.Pages['stock']


    # 실시간 업데이트
    def UpdateCoin(self):
        if self.CurrCoin != 0:
            self.UI.Pages['bitcoin'].UpdateCurr(self.CurrCoin)

    def UpdateStock(self):
        if self.CurrStock != 0:
            self.UI.Pages['stock'].UpdateCurr(self.CurrStock)

    def UpdateCompare(self):
        self.UI.Pages['bitcoin'].UpdateCompare()

    def UpdateNews(self):
        if self.UI.Get_CurrFrame() != 'news':
            self.UI.Pages['news'].Rest()
        else:
            self.UI.Pages['news'].Work()

    # 검색기능
    def Search(self, event):
        type = self.UI.Get_CurrFrame()
        name = self.UI.StatusGUI.Searchbar.get() # 검색창에 입력한 이름

        if type == 'bitcoin':
            print('비트코인 확인')
            result = Bitcoin.CoinInfo.SearchCoin(name)
            if result is not None:
                if self.CurrCoin != 0:
                    del self.CurrCoin
                self.CurrCoin = Bitcoin.Bitcoin(result)
                self.UI.Pages[type].SetCurr(self.CurrCoin)
                self.UI.StatusGUI.Searchbar['fg'] = 'black'
            else :
                self.UI.StatusGUI.Searchbar['fg'] = 'red'

        if type == 'stock':
            if Stock.StockInfo.login == True:
                print('주식 확인')
                result = Stock.StockInfo.SearchStock(name)
                if result is not None:
                    if self.CurrStock != 0:
                        del self.CurrStock
                    self.CurrStock = Stock.Stock(result)
                    self.UI.Pages[type].SetCurr(self.CurrStock)
                    self.UI.StatusGUI.Searchbar['fg'] = 'black'
                else :
                    self.UI.StatusGUI.Searchbar['fg'] = 'red'

    def Search_Reset(self, event):
        self.UI.StatusGUI.Searchbar['fg'] = 'black'

    def Update_CoinUI(self, item):
        pass

    def Update_StockUI(self, item):
        pass

    def Update_FavUI(self, type, item):
        pass

    def Update_CompareUI(self, type, item):
        pass

from article import *
from stock_entry import StockEntry

class Stock:
    def __init__(self):
        self.entries = []

    def addArticleQuantity(self, article, quantity):
        entry = StockEntry(article, quantity)
        self.entries.append(entry)

    def addStockEntry(self, entry):
        self.entries.append(entry)

    def print(self):
        print('************************')
        totalPrice = 0
        for entry in self.entries:
            print(entry.toString())
            totalPrice += entry.price()
        print('Total stock : {}€'.format(totalPrice))
        print('************************')

    def addArticle(self):
        article = Article.createArticle() # recupere mon article - method de class avec A pour faire ref à la classe
        quantity = int(input("quantité de l'article: "))
        self.addArticleQuantity(article, quantity)

stock = Stock()
stock.addArticleQuantity(article, 1)
stock.addArticleQuantity(article2, 10)
stock.addArticleQuantity(article3, 20)
stock.print()
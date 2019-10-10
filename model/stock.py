from model.article import *
from model.stock_entry import StockEntry
from application import db
# stock = list de stock entry
# - 1 seul stock
# - on le met pas comme bdd mais on l'utilise comme objet

class Stock:
    #def __init__(self):
    #    self.entries = []
    def entries(self):                            #   pour recuperer les StockEntry
        return StockEntry.query.all()

    def addStockEntry(self, entry):
                                                  #  self.entries.append(entry)
        db.session.add(entry)
        db.session.commit()
    #def addArticleQuantity(self, article, quantity):
    #    entry = StockEntry(article, quantity)
    #    self.entries.append(entry)
    def addArticle(self):
        article = Article.createArticle()         # recupere mon article - method de class avec A pour faire ref à la classe
        quantity = int(input("quantité de l'article: "))
        self.addArticleQuantity(article, quantity)

    def addArticleQuantity(self, article, quantity):
        entry = StockEntry(article=article, quantity=quantity)
        db.session.add(entry)
        db.session.commit()

    def deleteArticleById(self, article_id):
        entry = StockEntry.query.filter_by(article_id=article_id).first()
        article = Article.query.filter_by(id=article_id).first()
        db.session.delete(entry)
        db.session.delete(article)
        db.session.commit()
    #def addStockEntry(self, entry):
    #    self.entries.append(entry)
    def print(self):
        print('************************')
        totalPrice = 0
        for entry in self.entries():              #  appelle la methode entries
            print(entry.toString())
            totalPrice += entry.price()
        print('Total stock : {}€'.format(totalPrice))
        print('************************')

stock = Stock()
#stock.addArticleQuantity(article, 1)
#stock.addArticleQuantity(article2, 10)
#stock.addArticleQuantity(article3, 20)
#stock.print()
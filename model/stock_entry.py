from model.article import Article
from application import db

# on fait les relations entre article avec (db.Model) - creer un foreign key pour faire la relation
class StockEntry(db.Model):

    article_id = db.Column(db.Integer, db.ForeignKey('article.id'), primary_key=True, nullable=False)
    article = db.relationship('Article') # article = db.relationship('Article',backref=db.backref('entries')) si relation manytomany

    quantity = db.Column(db.Integer, default=0)

    #def __init__(self, article, quantity):
    #    self.article = article
    #    self.quantity = quantity

    def price(self):
        return self.article.price * self.article.quantity

    def toString(self):
        return '{} x {}'.format(self.article.toString(), self.article.quantity)
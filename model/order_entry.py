from application import db

class OrderEntry(db.Model):

    article_id = db.Column(db.Integer, db.ForeignKey('article.id', ondelete='CASCADE'), primary_key=True)
    article = db.relationship('Article')

    order_id = db.Column(db.Integer, db.ForeignKey('article.id', ondelete='CASCADE'), primary_key=True)
    order = db.relationship('Order', backref=db.backref('entries'))

#    Si un order_entry est supprimer il sera suprimer
#    si un artciel est supprimer il sera supprimer sur order_entry

    quantity = db.Column(db.Integer, default=0)

    def price(self):
        return self.article.price * self.article.quantity

    def toString(self):
        return '{} x {}'.format(self.article.toString(), self.article.quantity)


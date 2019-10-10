from application import db # import de notre bdd

class Article(db.Model): # heritage de notre objet article du model de base de sqlmychemy - plus besoin du currentID

    # currentId = 0 - plus besoin du currentID
    # on va declarer des method de class en associant des variables de classe pour l'orm
    id = db.Column(db.Integer, primary_key=True) #cree une colonne pour l'id - premier element se met en auto-increment - ce n'est pas foreignkey
    name = db.Column(db.String(80), nullable=False) #cree une colonne pour name
    description = db.Column(db.String(120), nullable=False) #cree une colonne pour description
    price = db.Column(db.Integer, nullable=False) #cree une colonne pour price
#    entry = StockEntry.query.filter_by(article_id=).first()
#    article = Article.query.filter_by(id=).first()

    # sqla va nous creer un contructeur automatique et il faudra juste renseigner les champs ligne 33

    # A enlever
    #def __init__(self, name, description, price):
        #Article.currentId += 1
        #self.id = Article.currentId
        #self.name = name
        #self.description = description
        #self.price = price

    def print(self):
        print('[{}] Article {} - {}€ : \n{}'.format(self.id, self.name, self.price, self.description))

    def toString(self):
        return '{} - {}€'.format(self.name, self.price)

    @classmethod
    def createArticle(cls):
        name = input("nom: ")
        description = input("Description: ")
        price = int(input("Prix: "))

        # sqla va nous creer un contructeur automatique et il faudra juste renseigner les champs ligne 33
        article = Article(name=name, description=description, price=price)
        return article

    def update(self, values):
        self.name = values['name']
        self.description = values['description']
        self.price = values['price']
        db.session.commit()

# on enleve les articles creer en dur

#article = Article('Macbook', 'Ordinateur Apple', 1500)
#article.print()

#article2 = Article('Article2', 'Description2', 300)
#article2.print()

#article3 = Article('Article3', 'Description 3', 100)
#article3.print()
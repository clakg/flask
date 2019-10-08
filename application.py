from flask import Flask
from flask import render_template #Jinja2
app = Flask(__name__) # on instancie l'application

@app.route('/hello') # routing url - la route hello dans la fonction hello_world
def hello_world():
    return 'Hello, R1 !'

#flask a besoin de savoir avec quel fichier on lance la variable d'environnement

@app.route('/user/<username>/<int:other>') # routing avec une variable dans l'url
def show_username(username, other):
    return 'Hello, {}, {}'.format(username, other)

@app.route('/') # on donne une nouvelle route qui sera notre page d'accueil
def index():
    return render_template('index.html', liste=["l1","l2","l3"])
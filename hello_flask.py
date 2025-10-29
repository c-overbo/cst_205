from flask import Flask, render_template
from flask_bootstrap import Bootstrap5
app = Flask(__name__)
bootstrap = Bootstrap5(app)

@app.route('/')
def hello():
    return 'Hello world from Flask!'

@app.route('/welcome')
def wc():
    s1 = 'Welcome to my page! '
    s2 = 'Have a nice day!'
    return s1 + s2

@app.route('/class-info')
def ci():
    return (
    "<p>Devin : idk : easy answer</p>"
    "<p>Kaden : lol : it's funny</p>"
    "<p>Jehden : afaik : just cuz</p>"
    )

@app.route('/connor')
def t_test():
    return render_template('templates.html')

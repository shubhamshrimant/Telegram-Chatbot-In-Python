#from os import environ
from flask import Flask
import chatbot,telegram
app = Flask(__name__)
#app.run(environ.get('PORT'))

@app.route('/')
def hello():
    file = open(r'telegram1.py', 'r').read()
    return exec(file)

if __name__ == '__main__':
    app.run(threaded=True)

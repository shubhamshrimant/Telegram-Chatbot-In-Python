#from os import environ
from flask import Flask

app = Flask(__name__)
#app.run(environ.get('PORT'))
if __name__ == '__main__':
    app.run()

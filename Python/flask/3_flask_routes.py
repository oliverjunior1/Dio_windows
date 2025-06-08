from flask import Flask

app = Flask(__name__)

@app.route('/hello')

# after the adress put /hello
def hello_world():
    return 'Hello World!'
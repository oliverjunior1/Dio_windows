from flask import Flask

app = Flask(__name__)

@app.route('/hello')

# after the adress put /hello or what is unused down
def hello_world():
    return 'Hello World!'

# app.add_url_rule('/', 'hello', hello_world)
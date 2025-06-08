from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return ("<h1>Jesus How I love you</h1>"
            "<d>Jesus is the way, the trth and the life</d>"
            "<table><tr><th>Name</th><th>Age</th><th>Products</th></tr></table>")

if __name__=='__main':
    app.run(debug=True)
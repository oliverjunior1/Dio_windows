from flask import Flask

app = Flask(__name__)
app.run(debug=True)

@app.route("/")
def hello_world():
    return {"Message":"Jesus is the light of the World!", app:"Hello"}
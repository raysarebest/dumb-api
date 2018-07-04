from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "You need to tell me how dumb you want it"

@app.route("/<int:count>")
def normal(count):
    return "dumb" * count

@app.route("/<count>")
def special(count):
    count = int(count)
    return "dumb"[::int(abs(count) / count)] * abs(count)

app.run(debug=True)
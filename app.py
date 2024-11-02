from flask import Flask, render_template, json
import requests

app = Flask(__name__)

apiData = [
    {"penguin": "emperor penguin",
     "habitat": "ice",

    }
]

@app.route("/<name>/<day>")
def hello_world(name, day):
    return "Hello" + name + "today is" + day

@app.route("/<num>/")
def number(num):
    if int(num) > 10: 
        return num + " is greater than 10"
    return num + " is less than 10"

@app.route("/penguins")
def penguin():
    return apiData
    # penguin = requests.get("http://100.114.3.84:5000/11")
    # return "olivias api said: " + penguin.text

if __name__ == '__main__':
    app.run(debug=True, port=5001, host = '0.0.0.0')

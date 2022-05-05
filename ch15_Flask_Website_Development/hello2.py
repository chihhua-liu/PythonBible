from flask import Flask
app = Flask(__name__)

@app.route("/hello/<string:name>")
def hello(name):
    return '{},Welcome to Flask'.format(name)

if __name__ == '__main__':
    app.run()
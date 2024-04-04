from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "hello world, index"

@app.route('/scott')
def scott():
    return "hello world, scott"

if __name__ == '__main__':
    app.run(debug=True)
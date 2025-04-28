from flask import Flask
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def hello_datetime():
    now = datetime.now()
    formatted_datetime = now.strftime("%Y-%m-%d %H:%M:%S")
    return f"<h1>Hello from Flask!</h1><p>Current Date and Time: {formatted_datetime}</p>"

@app.route('/hello/<name>')
def hello_name(name):
    return f"<h1>Hello, {name}!</h1>"

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
from flask import Flask, render_template
import datetime

app = Flask(__name__)

@app.route('/')
def index():
    now = datetime.datetime.now()
    return render_template('index.html', time=now.strftime("%H:%M"), date=now.strftime("%A, %d %B %Y"))

if __name__ == '__main__':
    app.run(debug=True)



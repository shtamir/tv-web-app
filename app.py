from flask import Flask, render_template
import datetime
from google_sheets import get_sheet_data

app = Flask(__name__)

@app.route('/')
def index():
    now = datetime.datetime.now()
    time = now.strftime("%H:%M")
    date = now.strftime("%A, %d %B %Y")

    # Fetch team messages
    messages = get_sheet_data('Messages','A:A')  # Assuming messages are in 'Messages' sheet, column A
    messages = [msg[0] for msg in messages if msg]

    # Fetch to-do list
    todos = get_sheet_data('ToDo','A:A')  # Assuming to-dos are in 'ToDo' sheet, column A
    todos = [todo[0] for todo in todos if todo]

    return render_template('index.html', time=time, date=date, messages=messages, todos=todos)

if __name__ == '__main__':
    app.run(debug=True)



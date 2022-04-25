from flask import Flask, render_template
import pandas as p

app = Flask(__name__)


@app.route('/')
def index() -> str:
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)

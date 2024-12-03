
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')
@app.route('/home')
def home():
    return render_template('home.html')
@app.route('/category/<category>')
def category(category):
    return render_template(f'{category}.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port= 5050)

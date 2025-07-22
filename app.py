from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/add_users')
def addUsers():
    return render_template('add_users.html')

@app.route('/users')
def user():
    return render_template('users.html')

if __name__ == '__main__':
    app.run(debug=True)
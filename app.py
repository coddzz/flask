from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/user/<username>')
def show_user(username):
    return f"<h2> Hello, {username} </h2>"

from flask import request

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user = request.form['username']
        return f"Welcome, {user}"
    return '''
        <form method="post">
            Username: <input name="username">
            <input type="submit">
        </form>
    '''

@app.route('/add_users')
def addUsers():
    return render_template('add_users.html')

@app.route('/users')
def user():
    return render_template('users.html')

if __name__ == '__main__':
    app.run(debug=True)
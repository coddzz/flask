from flask import Flask, render_template, redirect, url_for, request
from forms import UserForm
from models import db, User

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecretkey'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


db.init_app(app)

@app.before_request
def create_tables():
    db.create_all()


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/add_user', methods=['GET', 'POST'])
def add_user():
    form = UserForm()
    if form.validate_on_submit():
        user = User(name=form.name.data, email=form.email.data)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('users'))
    return render_template('add_user.html', form=form)


@app.route('/show/<username>')
def show(username):
    return f" <h1> Hello, {username} </h1>"


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user = request.form['username']
        return f"""<h2> Welcome, {user} </h2>
        
        Its a simple function. No account have been created!
        """
    return render_template('login.html')


@app.route('/users')
def users():
    all_users = User.query.all()
    return render_template('users.html', users=all_users)


if __name__ == '__main__':
    app.run(debug=True)
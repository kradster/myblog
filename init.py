from flask import Flask, render_template,url_for,redirect,flash
from flask_sqlalchemy import SQLAlchemy
from forms import RegisterationForm,LoginForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'a3d8aa09d9834c6d6b9c3435a6ade709'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(20),unique=True,nullable=False)
    email = db.Column(db.String(120),unique=True,nullable=False)
    image_file = db.Column(db.String(60),nullable=False)

    def __repr__(self):
        return f"User('{self.username}','{self.email}','{self.image_file}')"

# class Post(db.Model):




posts = [
    {
        'author':'pedro carvalho',
        'title':'blog post 1',
        'content':'First blog content',
        'date_posted':'jan 1 2018'
    },
    {
        'author':'thor scholhern',
        'title':'blog post 2',
        'content':'Second blog content',
        'date_posted':'jan 2 2018'
    }
]

@app.route("/")
@app.route('/home')
def home():
    return render_template('home.html',posts=posts,title='Home')

@app.route('/about')
def about():
    return render_template('about.html',title='About')

@app.route('/login')
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data=='vinodkaradiya@gmail.com' and form.password.data=='vinod1234':
            flash('You have been logged in !','success')
            return redirect(url_for('home'))
        else:
            flash('Login unsuccessful. Please check username and password','danger')
    return render_template('login.html',title='Login',form=form)

@app.route('/signup',methods=['GET','POST'])
def signup():
    form = RegisterationForm()
    if form.validate_on_submit():
        flash(f'Account createde for {form.username.data}!','success')
        return redirect(url_for('home'))
    return render_template('signup.html',title='Signup',form=form)

if __name__ == '__main__':
    app.run(debug=True)
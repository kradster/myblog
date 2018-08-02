from flask import Flask, render_template
app = Flask(__name__)

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
def hello():
    return render_template('home.html',posts=posts,title='Home')

@app.route('/about')
def about():
    return render_template('about.html',title='About')

if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask, request, redirect, render_template
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://build-a-blog:build-a-blog@localhost:8889/build-a-blog'
app.config['SQLALCHEMY_ECHO'] = True
db = SQLAlchemy(app)


class Blog(db.Model):

    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(120))
    body = db.Column(db.String(480))
    complete = db.Column(db.Boolean)

    def __init__(self, title, body):
        self.title = title
        self.body = body




@app.route('/')
def index():
    return render_template('main_blog.html', title = "Build a blog")

@app.route('/blog')
def blogpage():
    return render_template('main_blog.html' ,title = "Build a blog")

@app.route('/newpost', methods = ['POST', 'GET'])
def newpost():
    if request.method == 'POST':
        title = request.form['blogtitle']
        body = request.form['blogtext']
    
        new_entry = Blog(title, body)
    
        db.session.add(new_entry)
        db.session.commit()

        blogs = Blog.query.all()
        return render_template('main_blog.html', title = 'Build a blog', blogs = blogs)
    else:
        return render_template('new_blog.html', title = 'New Blog Entry')




if __name__ == '__main__':
    app.run()

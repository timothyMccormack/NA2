# import the Flask class
from flask import Flask, url_for, render_template,jsonify



# use markupsafe so we can use variables in the url directories
from markupsafe import escape

# create an instance of a Flask
app = Flask(__name__)




# notify Flask what url triggers our function
@app.route('/')

# display this message in the user's browser
def hello_world():
    title = "Insta-cart Data Analysis"
    
    return render_template('test.html',title=title)

@app.route('/orders')
def data():
    title2 = "Insta-cart Orders"
    return render_template('orders.html', title2 = title2)

@app.route('/users')
def users():
    return render_template('users.html')

@app.route('/da')
def depA():
    return render_template('da.html')


@app.route('/pr')
def pr():
    return render_template('pr.html')
    

@app.route('/projects/')
def projects():
    return 'The project page'

@app.route('/about')
def about():
    return 'The about page'

# these functions use variables in the url
@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return 'User %s' % escape(username)

@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return 'Post %d' % post_id

@app.route('/path/<path:subpath>')
def show_subpath(subpath):
    # show the subpath after /path/
    return 'Subpath %s' % escape(subpath)




from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "this is the home page"

@app.route('/tuna')
def tuna():
    return '<h2>tuna is good</h2>'

@app.route('/profile/<username>') 
def profile(username):
    return "<h2>%s is A Real 1</h2>" % username

@app.route('/post/<int:post_id>') 
def showPost(post_id):
    return "<h2>%s ID AYYYYYYY</h2>" % post_id

if __name__ == "__main__":
    app.run(debug=True)
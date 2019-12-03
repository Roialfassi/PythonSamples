from flask import Flask ,request

app = Flask(__name__)

@app.route("/")
def index():
    return "Method used: %s" % request.method

@app.route("/ttyl" , methods=['GET' , 'POST'])
def tuna():
    if request.method == 'POST':
        return "You Are Using POST"
    else:
        return "You are not posting up"
# @app.route("/")
# def index():
#     return "HomePage"

if __name__ == "__main__":
    app.run()

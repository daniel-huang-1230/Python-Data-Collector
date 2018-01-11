from flask import Flask,render_template, request
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:1230@localhost/height_collector'
db = SQLAlchemy(app)

class Data(db.Model):
    __tablename__ = "data"
    id=db.Column(db.Integer, primary_key=True)
    email_=db.Column(db.String(120), unique=True)
    height_=db.Column(db.Integer)
    def __init__(self,email_,height_):
        self.email_ = email_
        self.height_= height_

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/success", methods=["POST"])
def success():
    if  request.method == "POST": #to make sure the user access this URL through a POST request
        email = request.form["email_name"] #grab the input value from email entry
        height = request.form["height_name"]
        print(height)
        return render_template("success.html")

if __name__ == "__main__": #meaning if the script is being executed, rather than being imported
    app.debug = True
    app.run(port=8000)

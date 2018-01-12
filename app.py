from flask import Flask,render_template, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func
from send_email import send_email
app = Flask(__name__)
#app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:******@localhost/height_collector'

#we need the database URI created heroku, instead of the local database I have on my machin
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://njvkpphqslvnds:9cf9615b08447af2526dc1f92d231257c35d702e4913ff13b273' \
                                        '081c62d21780@ec2-23-23-110-26.compute-1.amazonaws.com:5432/d5le9u75j686gc?sslmode=require'

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

        #first check if the email account already exists in the datagase
        if db.session.query(Data).filter(Data.email_ == email).count() == 0:
            #SQLAlchemy requires fewer lines than psycopg2
            data = Data(email, height)  #create the object from our model blueprint
            db.session.add(data)
            db.session.commit()
            #now we can calculate the average height from our data stored in the database
            average_height = db.session.query(func.avg(Data.height_)).scalar()
            average_height = round(average_height, 1) #round up the avg to 1 decimal point
            count = db.session.query(Data.height_).count()
            send_email(email, height, average_height,count)
            return render_template("success.html")
        else:
            return render_template("index.html",
                                   text="email address already exists, try a new one")

if __name__ == "__main__": #meaning if the script is being executed, rather than being imported
    app.debug = True
    app.run(port=5000)

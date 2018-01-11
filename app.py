from flask import Flask,render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/success", methods=["POST"])
def success():
    if  request.method == "POST": #to make sure the user access this URL through a POST request
        email = request.form["email_name"] #grab the input value from email entry
        print(email)
        return render_template("success.html")

if __name__ == "__main__": #meaning if the script is being executed, rather than being imported
    app.debug = True
    app.run(port=8000)

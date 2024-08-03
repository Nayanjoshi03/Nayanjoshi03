from flask import  Flask,render_template ,request 

app= Flask(__name__)

@app.route('/')
def index():
    return render_template("login.html")

@app.route('/register',methods=["POST","GET"])
def regiser():
    name=request.form.get("name")
    return f"Hello "+str(name)

def hello():
    return "hello from server"

app.add_url_rule("/hello/server","",hello)

if __name__=='__main__':
    app.run(debug=True)
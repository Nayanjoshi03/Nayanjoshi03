from flask import Flask ,render_template,url_for,request

app=Flask(__name__)
users={"nayan":["Nayan","123"]}

@app.get("/login")
def login():
    return render_template("login_as.html")

@app.post("/login")
def login_post():
    if request.method!="POST":
        return "Bad request",500
    uname=request.form.get("username")
    passwd=request.form.get("password")
    if uname in users and users[uname][1]==passwd:
        return "Login Successfull",200
    else:
        return f"username or password is incorrect" 
        

@app.get("/signup")
def signup():
    return render_template("signup.html")

@app.post("/signup")
def signup_post():
    if request.method!="POST":
        return "Bad request",500
    uname=request.form.get("username")
    passwd=request.form.get("password")
    name=request.form.get("name").lower()
    lst=[]
    lst.append(name)
    lst.append(passwd)
    users[uname]=lst
    return render_template("login_as.html")

if __name__ =="__main__":
    app.run(debug=True)
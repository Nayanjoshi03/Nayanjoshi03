from flask import Flask , render_template,request,make_response

app=Flask(__name__)

@app.route("/form/",methods=["GET","POST"])
def form():
    if request.method =="POST":
        name=request.form.get("name")
        number=request.form.get("number")
        res=make_response("cookies is set")
        res.set_cookie("name",name)
        #file=request.files.get("file")
        #request.set_cookies("name",name)
        #file.save("static")
        return f"hello {name} your number is  {number}",res
    else:
        # if request.cookies("name")!="":
        #     print("hello",request.cookies("name"))
            
        return render_template("form.html.jinja")
        
if __name__=="__main__":
    app.run(debug=True)
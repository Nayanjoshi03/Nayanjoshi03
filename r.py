from flask import Flask as fk   

app=fk("Flask.app1")
#print(__name__)
@app.route("/")
def h():
    return"hello"

app.run(debug=True)
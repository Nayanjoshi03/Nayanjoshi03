from flask import Flask

app=Flask(__name__)

@app.route("/home/<string Text>")
def home(Text):
    return "Hello you entered {text} in url"

if __name__=="__main__":
    app.run(debug=True)
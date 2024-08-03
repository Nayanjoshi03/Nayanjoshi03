from flask import Flask ,render_template

app=Flask(__name__)
app.jinja_env.line_statement_prefix = '#'


posts=[
	{
    "title":"The Black sun",
    "author":"Nayan",
   "content":"this book is all about a sab story af a person",
  },
	{
    "title":"The Black star",
    "author":"Ram",
   "content":"this book is all about a sab story af a person",
  },
	{
    "title":"The Black Rock",
    "author":"sham",
   "content":"this book is all about a sab story af a person",
  },
	{
    "title":"The sun",
    "author":"Nayan Joshi",
   "content":"this book is all about a sab story af a person",
  }
]

@app.route("/")
def home():
    return render_template("home.html.jinja", posts = posts,title="hello")

if __name__=="__main__":
    app.run(debug=True)
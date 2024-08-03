from flask import Flask 

app = Flask(__name__)
ideas ={
    1:{"idea_id":1,
       "idea_name":"Idea 1",
       "idea_description":"This is idea 1",
       "idea_status":"Active",
       },
    2:{"idea_id":2,
       "idea_name":"Idea 2",
       "idea_description":"This is idea 2",
       "idea_status":"Active",
       }
    }

@app.route('/ideas')
def index():
    return ideas

if __name__=="__main__":
    app.run(debug=True)

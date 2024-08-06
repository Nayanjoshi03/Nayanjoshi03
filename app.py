from flask import Flask , request

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

@app.get('/ideas')
def index():
    return ideas
@app.post('/ideas')
def post_ideas():
    new_idea = request.get_json()
    try:
        if new_idea["idea_id"] in ideas :
            return "id already exist",400
        ideas[new_idea["idea_id"]]=new_idea
        return "idea added successfully"
        
    except e as Exceprion :
        return {"error": str(e)}, 400

if __name__=="__main__":
    app.run(debug=True)

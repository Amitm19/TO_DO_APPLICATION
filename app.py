import os
from flask import Flask,request,render_template
from datetime import datetime
import pymongo
from dotenv import load_dotenv

load_dotenv()

MONGO_URI = os.getenv("MONGO_URI")
clint= pymongo.MongoClient(MONGO_URI)
db=clint.todo_list
collection=db['list']

app =Flask(__name__)

@app.route('/')
def home():
    day_of_week = datetime.today().strftime('%A')
    current_time = datetime.now().strftime('%H:%M:%S')
    return render_template('index.html', day_of_week=day_of_week, current_time=current_time)




@app.route('/submit', methods=['POST'])
def submit():
    form_data = dict(request.form)

    print(form_data)

    collection.insert_one(form_data)

    return "Data submitted successfully"

@app.route('/submittodoitem')
def view():
    data = collection.find()
    data = list(data)
    for item in data:
        del item['_id']
    
    data={
        "data": data
    }
    return data
if __name__== '__main__':
    app.run(debug=True)
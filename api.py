from flask import Flask,request,redirect,session,render_template,jsonify
from ram import read_db,ram
import json
app=Flask(__name__)

 #route for input the parameter 
@app.route('/')
def show_ram_record():
    
    return render_template('count.html')
#show the api    
@app.route('/api' , methods=['post'])
def show_api():
    number=request.form.get('number',None)
    ram()
    record=read_db(number)
    record_js=json.dumps(record)
    
    
    return f"it is your wanted:   {record_js}"


app.run()

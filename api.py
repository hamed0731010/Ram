from flask import Flask,request,redirect,session,render_template,jsonify
from ram import read_db,conv_list_json
import json
app=Flask(__name__)

@app.route('/')
def show_ram():
    
    return render_template('api.html')
@app.route('/api' , methods=['post'])
def show_api():
    number=request.form.get('number',None)
    rows=read_db(number)
    row=json.dumps(rows)
    
    
    return f"it is your wanted:   {row}"


app.run()
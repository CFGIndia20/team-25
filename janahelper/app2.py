from googletrans import Translator
#from classification.categorize import pred
from flask import Flask, render_template,request, redirect, url_for,jsonify
from flask_sqlalchemy import SQLAlchemy
from Model.models import Complaint
translator = Translator()

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db = SQLAlchemy(app)

@app.route('/api/complaint', methods=['POST'])
def push_data():
    if request.method == 'GET':
        return 
    elif request.method == 'POST':
        try:
            complaints_json = request.get_jason()
            text=complaints_json['complaint_text']

            text = translator.translate(str(text), dest='en').text
            latitude = complaints_json['location']['lat']
            longitude = complaints_json['location']['long']
            google_maps_location = "http://maps.google.com/maps?q=%s,%s",str(latitude), str(longitude)
            #categories = pred(text)
            name=complaints_json['user']['name']
            complaint1=Complaint(username=name,category=text,location=google_maps_location, text=text)
            db.session.add(complaint1)
            db.session.commit()
            return_body = dict(complaints_json)
            del return_body["complaint_text"]
            return_body["location"] = google_maps_location
            return_body["complaint"] = {
                "category": categories,
                "text": text
            }
            return jsonify(return_body), 200
        except:
            return redirect(url_for('get_data'))
            

@app.route('/api/complaints/<user_name>', methods=['GET'])
def get_complaints_by_user():
    if request.method == 'GET':
        complaints = Complaint.get_by_name(user_name)


@app.errorhandler(404)  
def not_found(e):
    return redirect(url_for('get_data'))

if __name__ == '__main__':
    app.run(debug=True)
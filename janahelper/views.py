from googletrans import Translator
from API.classification.categorize import pred
from flask import Flask, render_template, request, redirect, url_for, jsonify
from flask_sqlalchemy import SQLAlchemy
from config import PG_URI
from janahelper import app
from helper import push_complaint, get_complaints

translator = Translator()


@app.route('/api/complaint', methods=['POST'])
def push_data():
    if request.method == 'GET':
        return
    elif request.method == 'POST':

        complaints_json = request.get_json()
        text = complaints_json['complaint_text']

        text = translator.translate(str(text), dest='en').text
        latitude = complaints_json['location']['lat']
        longitude = complaints_json['location']['long']
        google_maps_location = "http://maps.google.com/maps?q=%s,%s" % (str(
            latitude), str(longitude))
        categories = pred(text)
        print(complaints_json)
        name = complaints_json['user']['username']
        push_complaint(username=name, userid=complaints_json["user"]["id"], category=categories, location=google_maps_location, text=text)
        return_body = dict(complaints_json)
        del return_body["complaint_text"]
        return_body["location"] = google_maps_location
        return_body["complaint"] = {
            "category": categories,
            "text": text
        }
        return jsonify(return_body), 200


@app.route('/api/complaints', methods=['GET'])
def get_complaints_by_user():
    if request.method == 'GET':
        user_name = request.args['user_name']
        complaints = get_complaints(user_name)
        if complaints:
            if isinstance(complaints, list):
                complaints_dict = []
                for complaint in complaints:
                    complaint_dict = {
                        "category": complaint.category,
                        "text": complaint.text,
                        "id": complaint.id,
                        "location": complaint.location,
                        "status": complaint.status
                    }
                    complaints_dict.append(complaint_dict)
            else:
                complaints_dict = [{
                    "category": complaints.category,
                    "text": complaints.text,
                    "id": complaints.id,
                    "location": complaints.location,
                    "status": complaints.status
                }]
            print(complaints_dict)
            return jsonify({"complaints": complaints_dict}), 200
        else:
            return jsonify({"error": "No records were found for the user"}), 404




if __name__ == '__main__':
    app.run(debug=True, port=8080)

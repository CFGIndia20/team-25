import json
from googletrans import Translator
from classification.categorize import pred
from flask import Flask, render_template,request, redirect, url_for
# from janahelper import app
app = Flask(__name__)
translator = Translator()

@app.route('/complaints', methods=['POST'])
def get_data():
    if request.method == 'POST':
        content = request.json
        text = content['complaint_text']
        if len(text) == 0:
            return json.dumps({"error": "Text field should not be left empty"})
        text = translator.translate(str(text), dest='en').text
        latitude = content['cdlat']
        longitude = content['cdlon']
        categories = pred(text)
        return json.dumps({'categories': categories, "location": {"latitude": latitude, "longitude": longitude}})
    else:
        return json.dumps({"error": "Try sending using POST request"})

@app.errorhandler(404)  
def not_found(e):
    return json.dumps({"error": "Endpoint not found"})

if __name__ == '__main__':
    app.run(debug=True, port=5000)
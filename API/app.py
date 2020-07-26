import json
from googletrans import Translator
from API.classification.categorize import pred
from flask import Flask, render_template,request, redirect, url_for
from janahelper import app

translator = Translator()

@app.route('/complaints', methods=['POST'])
def get_data():
    if request.method == 'POST':
        content = request.json
        print(content)
        text = content['complaint_text']
        text = translator.translate(str(text), dest='en').text
        latitude = content['cdlat']
        longitude = content['cdlon']
        categories = pred(text)
        return json.dumps({'categories': categories, "location": {"latitude": latitude, "longitude": longitude}})

if __name__ == '__main__':
    app.run(debug=True, port=8080)
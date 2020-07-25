from googletrans import Translator
from classification.categorize import pred
from flask import Flask, render_template,request, redirect, url_for
from flask_mysqldb import MySQL


app = Flask(__name__)
translator = Translator()

@app.route('/complaints', methods=['POST','GET'])
def get_data():
    if request.method == 'POST':
            content= request.get_json()
            print(content)
            username=content['name']
            text = content['complaint_text']
            text = translator.translate(str(text), dest='en').text
            latitude = content['cdlat']
            longitude = content['cdlon']
            categories=pred(text)
            return {'categories': categories, 'location': {"latitude": latitude, "longitude": longitude}}

@app.errorhandler(404)  
def not_found(e):
    return redirect(url_for('get_data'))

if __name__ == '__main__':
    app.run(debug=True)
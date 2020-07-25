from googletrans import Translator
from classification.categorize import pred
from flask import Flask, render_template,request, redirect, url_for

app = Flask(__name__)
translator = Translator()

@app.route('/complaints', methods=['POST','GET'])
def get_data():
    if request.method == 'GET':
        return render_template('input.html')
    elif request.method == 'POST':
        text = request.form['complaint']
        text = translator.translate(str(text), dest='en').text
        latitude = request.form['cdlat']
        longitude = request.form['cdlon']
        categories=pred(text)
        return {'categories': categories, 'location': {"latitude": latitude, "longitude": longitude}}


@app.errorhandler(404)  
def not_found(e):
    return redirect(url_for('get_data'))

if __name__ == '__main__':
    app.run(debug=True)
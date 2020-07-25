from googletrans import Translator
from classification.categorize import pred
from flask import Flask, render_template,request, redirect, url_for
translator = Translator()

app = Flask(__name__)

@app.route('/complaints', methods=['POST','GET'])
def get_data():
    if request.method == 'GET':
        return render_template('input.html')
    elif request.method == 'POST':
        try:
            text = request.form['complaint']
            text = translator.translate(str(text), dest='en').text
            latitude = request.form['cdlat']
            longitude = request.form['cdlon']
            categories = pred(text)
            return {'categories': categories, 'location': {"latittude": latitude, "longitude": longitude}}
        except:
            return redirect(url_for('get_data'))

@app.errorhandler(404)  
def not_found(e):
    return redirect(url_for('get_data'))

if __name__ == '__main__':
    app.run(debug=True)
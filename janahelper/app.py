
from flask_sqlalchemy import SQLAlchemy
from googletrans import Translator
from classification.categorize import pred
from flask import Flask, render_template,request, redirect, url_for
from Model.models import Complaint
translator = Translator()

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db = SQLAlchemy(app)


@app.route('/complaints', methods=['POST','GET'])
def get_data():
    if request.method == 'GET':
        return render_template('input.html')
    elif request.method == 'POST':
        # try:
            text = request.form['complaint']
            text = translator.translate(str(text), dest='en').text
            latitude = request.form['cdlat']
            longitude = request.form['cdlon']
            categories=pred(text)
            complaint1=Complaint(category=categories, loc_late=latitude, loc_long=longitude)
            db.session.add(complaint1)
            db.session.commit()
            return {'categories': categories, 'location': {"latitude": latitude, "longitude": longitude}}
        # except:
        #     return redirect(url_for('get_data'))


@app.errorhandler(404)  
def not_found(e):
    return redirect(url_for('get_data'))

if __name__ == '__main__':
    app.run(debug=True)
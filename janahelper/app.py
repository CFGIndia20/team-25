from googletrans import Translator
from classification.categorize import pred
from flask import Flask, render_template,request, redirect, url_for
from flask_mysqldb import MySQL


app = Flask(__name__)


app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = ''
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'complaintsdb'

mysql = MySQL(app)

translator = Translator()




@app.route('/complaints', methods=['POST','GET'])
def get_data():
    if request.method == 'GET':
        return render_template('input.html')
    elif request.method == 'POST':
            content= request.get_json()
            username=content['name']
            text = content['complaint_text']
            text = translator.translate(str(text), dest='en').text
            latitude = content['cdlat']
            longitude = content['cdlon']
            categories=pred(text)
            # cur.execute("INSERT INTO complaints(username, category, location,status) VALUES (%s, %s,%s, %s,)", (firstName, lastName))
            # mysql.connection.commit()
            # cur.close()
            return {'categories': categories, 'location': {"latitude": latitude, "longitude": longitude}}

@app.errorhandler(404)  
def not_found(e):
    return redirect(url_for('get_data'))

if __name__ == '__main__':
    app.run(debug=True)
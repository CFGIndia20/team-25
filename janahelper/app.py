import csv, json, os
from dotenv import load_dotenv
from classification.categorize import pred
from flask import Flask, render_template, request, url_for, redirect

load_dotenv()
print(os.getenv("API_KEY"))
app = Flask(__name__)

def get_categories(text):
    return {"hello": text}

@app.route('/complaints', methods=['POST','GET'])
def get_data():
    if request.method == 'GET':
        return render_template('input.html')
    elif request.method == 'POST':
        try:
            text = request.form['complaint']
            latitude = request.form['latitude']
            longitude = request.form['longitude']
            categories = pred(text)
            return {'categories': categories, 'location': {"latittude": latitude, "longitude": longitude}}
        except:
            return redirect(url_for('get_data'))

@app.errorhandler(404)  
def not_found(e):
    return redirect(url_for('get_data'))

if __name__ == '__main__':
    app.run(debug=True, port="8000")
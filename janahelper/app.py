from flask import Flask, render_template, request
import csv, json
app = Flask(__name__)


def get_categories(text):
    return {"hello": text}

def get_location(text):
    return {text: "world"}

@app.route('/complaints', methods=['POST','GET'])
def get_data():
    if request.method == 'GET':
        return render_template('input.html')
    elif request.method == 'POST':
        text = request.form['complaint']
        categories = get_categories(text)
        location = get_location(text)
        return {'categories': categories, 'location': location}

if __name__ == '__main__':
    app.run(debug=True, port="8000")
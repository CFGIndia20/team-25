from flask import Flask, render_template
import csv, json
app = Flask(__name__)

with open('file.csv', 'r') as file:
    my_reader = csv.reader(file, delimiter=',')
    for row in my_reader:
        print(row)


def category_by_hand(text):
    pass

def location_by_hand(text):
    pass


def get_categories(text):
    pass

def get_location():
    pass

@app.route('/complaints', methods=['POST','GET'])
def get_data():
    if request.method == 'GET':
        return render_template('input.html')
    elif request.method == 'POST':
        text = request.form['complaint']
        categories = get_categories(text)
        location = get_location(text)
        return json.dump({'categories': categories, 'location': location})



if __name__ == '__main__':
    app.run(debug=True, )
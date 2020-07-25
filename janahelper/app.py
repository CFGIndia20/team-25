from janahelper.classification.categorize import pred
from flask import Flask, render_template,request

app = Flask(__name__)

@app.route('/complaints', methods=['POST','GET'])
def get_data():
    if request.method == 'GET':
        return render_template('input.html')
    elif request.method == 'POST':
<<<<<<< HEAD
        text = request.form['complaint']
        lat= request.form['cdlat']
        lon= request.form['cdlon']
        print(lat)
        categories = get_categories(text)
        location = get_location()
        return {'categories': text, 'latitude': lat , 'longitude':lon}


=======
        try:
            text = request.form['complaint']
            latitude = request.form['cdlat']
            longitude = request.form['cdlon']
            categories = pred(text)
            return {'categories': categories, 'location': {"latittude": latitude, "longitude": longitude}}
        except:
            return redirect(url_for('get_data'))

@app.errorhandler(404)  
def not_found(e):
    return redirect(url_for('get_data'))
>>>>>>> 996878ccce5b6a35438e82f2a1a220c6f528f848

if __name__ == '__main__':
    app.run(debug=True, )
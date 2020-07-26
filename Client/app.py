import requests, json
from flask import Flask, render_template,request, redirect, url_for, flash

app = Flask(__name__)
app.config['SECRET_KEY'] = 'Janahelper'


@app.route("/", methods=['GET', 'POST'])
def main():
    
    """ Main endpoint for our client takes get and post request, if a get request is there it render the
    input form and if post request is made it takes in text and location data and request for recomendation
    from the backend API and display the json result if successfull and an error message if request failed"""

    if request.method == 'GET':
        return render_template('input.html')
    elif request.method == 'POST':
        complaint = request.form['complaint_text']
        latitude = request.form['cdlat']
        longitude = request.form['cdlon']
        json_object = {"complaint_text": complaint, "cdlat": latitude, "cdlon": longitude}
        try:
            res = requests.post('http://localhost:5000/complaints', json=json_object)
            if res.status_code == 200:
                response = json.loads(res.content)
                flash(response ,"success")
            else:
                raise Exception()
        except:
            flash("There has been some fault", "error")
        
    return redirect(url_for("main"))

@app.errorhandler(404)  
def not_found(e):

    """A basic error handler if any other endpoint is tried to accessed"""

    flash("Wrong Path!", "error")
    return redirect(url_for('main'))

if __name__ == '__main__':
    app.run(debug=True, port="8080")

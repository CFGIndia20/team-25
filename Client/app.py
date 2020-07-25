import requests
from flask import Flask, render_template,request, redirect, url_for, flash

app = Flask(__name__)
app.config['SECRET_KEY'] = '_5#y2L"F4Q8z\n\xec]/'


@app.route("/", methods=['GET', 'POST'])
def main():
    if request.method == 'GET':
        return render_template('input.html')
    elif request.method == 'POST':
        print(request.form.keys())
        complaint = request.form['complaint_text']
        latitude = request.form['cdlat']
        longitude = request.form['cdlon']
        json_object = {"complaint": complaint, "location": {"latitude": latitude, "longitude": longitude}}
        try:
            print(json_object)
            res = requests.post('http://localhost:5000/complaint', json=json_object)
            if res.status_code == 200:
                flash(res.json,"success")
            else:
                raise Exception()
        except:
            flash("There has been some fault", "error")
        
    return redirect(url_for("main"))

@app.errorhandler(404)  
def not_found(e):
    flash("Wrong Path!", "error")
    return redirect(url_for('main'))

if __name__ == '__main__':
    app.run(debug=True, port="8080")
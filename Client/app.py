import requests, json
from flask import Flask, render_template,request, redirect, url_for, flash
from janahelper import app
app.config['SECRET_KEY'] = '_5#y2L"F4Q8z\n\xec]/'


@app.route("/", methods=['GET', 'POST'])
def main():
    if request.method == 'GET':
        return render_template('input.html')
    elif request.method == 'POST':
        complaint = request.form['complaint_text']
        latitude = request.form['cdlat']
        longitude = request.form['cdlon']
        json_object = {"complaint_text": complaint, "cdlat": latitude, "cdlon": longitude}
        try:
            res = requests.post('http://localhost:8080/complaints', json=json_object)
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
    flash("Wrong Path!", "error")
    return redirect(url_for('main'))

if __name__ == '__main__':
    app.run(debug=True, port="8080")

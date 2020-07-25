from flask import Flask
app = Flask(__name__)





@app.route('/complaints', methods=['POST','GET'])
def get_data():
    if(request.method == 'POST'):
        pass
    else:
        return render_template('hello.html')

   pass

if __name__ == '__main__':
    app.run()
from flask_sqlalchemy import SQLAlchemy 


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db = SQLAlchemy(app)

class Complaint(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username=db.Column(db.String(250),primary_key=True)
    category = db.Column(db.String(40),nullable=False)
    location=db.column(db.string(200),nullable=True)
    status = db.Column(db.String(30), nullable=False)

    @staticmethod    
    def get_by_name(name):    
        return Complaint.query.filter_by(username=name).all()

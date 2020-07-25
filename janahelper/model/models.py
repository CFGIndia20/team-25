class Complaint(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    category = db.Column(db.Integer,nullable=False)
    loc_lat = db.Column(db.String(10), nullable=False)
    loc_log = db.Column(db.String(10), nullable=False)
    status = db.Column(db.String(30), nullable=False)


from janahelper import db


class Complaint(db.Model):

    __tablename__ = "complaints"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255), nullable=False)
    user_id = db.Column(db.String(255), nullable=False)
    category = db.Column(db.String(255), nullable=False)
    location = db.Column(db.String(200), nullable=True)
    text = db.Column(db.String(500))
    status = db.Column(db.String(30), nullable=False)

    def __init__(self, username, user_id, category, text, location, status="Created"):
        self.username = username
        self.user_id = user_id
        self.category = category
        self.text = text
        self.location = location
        self.status = status


    @staticmethod
    def get_by_name(name):
        return Complaint.query.filter_by(username=name).all()

    def __repr__(self):
        text = "id: %s\nusername:%s\ncategory:%s"%(self.id, self.username, self.category)
        return text

if __name__ == '__main__':
    db.create_all()
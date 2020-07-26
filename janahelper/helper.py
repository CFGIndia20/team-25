from models import Complaint
from janahelper import db


def push_complaint(username,userid,  category, location, text):
    complaint1 = Complaint(
        username=username, user_id=userid, category=category, location=location, text=text)
    db.session.add(complaint1)
    db.session.commit()


def get_complaints(username):
    complaints = Complaint.get_by_name(username)
    return complaints

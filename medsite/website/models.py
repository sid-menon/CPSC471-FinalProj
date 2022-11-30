# database models
# where we define the schemas for our database
from . import db 
from flask_login import UserMixin
from sqlalchemy.sql import func

class Note(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    data = db.Column(db.String(10000))
    date = db.Column(db.DateTime(timezone = True), default=func.now())
    # how do we associate the notes with different users? foreign keys
    user_id = db.Column(db.Integer, db.ForeignKey('user.id')) # 1 user has many notes allows us to have this foreign key

class Patient(db.Model):
    healthcare = db.Column(db.String(10), primary_key=True)
    first_name = db.Column(db.String(50))
    last_name = db.Column(db.String(50))
    dob = db.Column(db.String(20))
    # sex = db.Column(db.String(15))
    # height = db.Column(db.Integer)
    # weight = db.Column(db.Integer)
    # medications = db.Column(db.String(1000))
    # doctor_id = db.Column(db.Integer, db.ForeignKey('doctor.id'))

class Doctor(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key = True)
    lastName = db.Column(db.String)
    specialization = db.Column(db.String)
    office = db.Column(db.Integer)
    #patients = db.relationship()

class Appointment(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    date = db.Column(db.String)
    time = db.Column(db.String)
    patientHealthCare = db.Column(db.Integer, db.ForeignKey('patient.healthcare'))
    patientFirstName = db.Column(db.Integer, db.ForeignKey('patient.first_name'))
    patientLastName = db.Column(db.Integer, db.ForeignKey('patient.last_name'))
    doctorLastName = db.Column(db.String, db.ForeignKey('doctor.lastName'))

# anytime want to add an object need
# to do it the way below 
# user has to inherit from UserMixin 
class User(db.Model, UserMixin):
    #define columns/schema
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique = True)   #Strings need max length, no users can have same email
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
    accessLevel = db.Column(db.String(150))
    notes = db.relationship('Note')


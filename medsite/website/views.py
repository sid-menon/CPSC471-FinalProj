from flask import Blueprint, render_template, request, flash
from flask_login import login_required, current_user
from .models import Note, Patient, Appointment
from . import db 
import random

id = 0000

views = Blueprint('views', __name__)

# define root or view
# hatever is inside or home is gonna run at root
# homepage 
@views.route('/', methods=['GET', 'POST'])
@login_required 
def home():
    if(current_user.accessLevel == "Admin"):
        return render_template("home.html", user=current_user)
    # if request.method == 'POST':
    
    #     date = request.form.get('date')
    #     time = request.form.get('time')
    #     patientHealthCare = request.form.get('patientHealtCare')
    #     patientFirstName = request.form.get('patientFirstName')
    #     patientLastName = request.form.get('patientLastName')

    #     patients = Patient.query.filter_by(healthcare=patientHealthCare).first()
    #     if patients:
    #         new_appointment = Appointment(date=date, time=time, patientHealthCare=patientHealthCare, patientFirstName=patientFirstName, patientLastName=patientLastName)
    #         db.session.add(new_appointment)
    #         db.session.commit
    #     else:
    #         flash('Patient not registered, please register them before making appointment', category='error')


        #note = request.form.get('note')

        # if len(note) < 1:
        #     flash('Note is too short!', catergory = 'error')
        # else:
        #     new_note= Note(data=note, user_id = current_user.id)
        #     db.session.add(new_note)
        #     db.session.commit()
        #     flash('Note added!', category='success')

# @views.route('/', methods=['GET', 'POST'])
# @login_required 
# def admin():
#     if(current_user.accessLevel == "Admin"):

@views.route('/addPatient', methods=['GET','POST'])
@login_required 
def addPatient():
    if request.method == 'POST':
        healthcare = request.form.get('healthcare')
        first_name = request.form.get('first_name')
        last_name = request.form.get('last_name')
        dob = request.form.get('dob')
        new_patient = Patient(healthcare=healthcare, first_name=first_name, last_name=last_name, dob=dob)
        patient = Patient.query.filter_by(healthcare=healthcare).first()
        if patient:
            flash('Patient with provided healthcare number already exists', category='error')
        else:
            db.session.add(new_patient)
            db.session.commit()
            flash('Patient successfully added', category='success')

    return render_template("addPatient.html", user=current_user)

@views.route('/makeAppointment', methods=['GET', 'POST'])
@login_required
def makeAppointment():
    if request.method == 'POST':
        date = request.form.get('date')
        time = request.form.get('time')
        healthcare = request.form.get('patientHealthCare')
        patientFirstName = request.form.get('patientFirstName')
        patientLastName = request.form.get('patientLastName')
        doctorLastName = request.form.get('doctorLastName')
        global id
        id +=1
        if id == 9999:
             id = 0000
    
        new_appointment = Appointment(id = random.randint(0,10000000), date=date, time=time, patientHealthCare=healthcare, patientFirstName=patientFirstName, patientLastName=patientLastName, doctorLastName=doctorLastName )
        patient = Patient.query.filter_by(healthcare=healthcare).first()
        if patient:
            db.session.add(new_appointment)
            db.session.commit()
            flash('Appointment successfully added', category='success')
        else:
            flash('Patient not found. Please add them before creating appointment', category = 'error')
          # need to add a check to ensure the doctor exists in the database 
          # could possible change to a toggle so that user can only select certain times with that doctor 
    return render_template("makeAppointment.html", user=current_user)

# would be cool if implemented a search functionality here! 
@views.route('/viewAppointments', methods=['GET', 'POST'])
@login_required
def viewAppointments():
    Fnames = []
    Lnames = []
    id = []
    date = []
    time = []
    healthcare = []
    doctor = []
    appointments = Appointment.query.all()
    data = []
    for appointment in appointments:
        data.append((appointment.id, appointment.patientFirstName, appointment.patientLastName, appointment.date, appointment.time, appointment.patientHealthCare, appointment.doctorLastName))
        Fnames.append(appointment.patientFirstName)
        Lnames.append(appointment.patientLastName)
        id.append(appointment.id)
        date.append(appointment.date)
        time.append(appointment.time)
        healthcare.append(appointment.patientHealthCare)
        doctor.append(appointment.doctorLastName)
    return render_template("viewAppointments.html", user=current_user,data=data)

    







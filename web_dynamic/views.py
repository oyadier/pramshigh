from flask import Flask, render_template, Blueprint, request, flash, redirect, url_for

import json
import models
from models.engine.storages import FileStorage
from models.user import User
from web_dynamic.database import session
from werkzeug.security import generate_password_hash, check_password_hash
views = Blueprint('views', __name__)

store = FileStorage()
@views.route("/home/")
@views.route('/coding/index/')
def pramshigh():
       
       #main app leading to the homepage of the app
       return render_template('index.html')

# @views.teardown_app_request
# def shutdown_session(exception=None):
#     session.remove()
@views.route('/delete_user', methods=['GET','POST'])
def delete_user():
     
     if request.method=='POST':
          
          data = request.get_json()
          inputValue = data['value']
          print(inputValue)
          store.deletes(inputValue)
           
     return render_template('form.html')

@views.route("/home/fisher/")
@views.route("/fisher/")
def fisher():
      return render_template('fisher.html')

@views.route("/home/courses/")
def courses():
     courses= ['Business', 'Scince', 'Home Econs (1)', 'Christian Religious Service']
     le = len(courses)
     return render_template('courses.html', courses=courses, lens=le)

@views.route("/navigation/")
def navigation():
     return render_template('navigation.html')

@views.route('/timetable/')
def timetable():
     return render_template('timetable_f1.html')



@views.route("/form", methods=['GET','POST'])
def form():
     #If the request is a POST. THIS is checked because
     
     # this same method will perform GET request too
     if request.method=='POST':
          
          data = request.form
          fName = data.get('first_name')
          sName = data.get('last_name')
          pwd = data.get('password')
          new_obj = User(fName,sName,pwd)
     
          new = store.save(new_obj)
             
       #   return redirect(url_for('views.pramshigh'))

     return render_template('form.html')

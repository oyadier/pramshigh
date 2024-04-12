from flask import Flask, render_template, Blueprint, request, flash

views = Blueprint('views', __name__)


@views.route("/home/")
@views.route('/coding/index/')
def pramshigh():
       
       #main app leading to the homepage of the app
       return render_template('index.html')


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

@views.route("/home/form/", methods=['GET','POST'])
def form():
     #If the request is a POST. THIS is checked because
     # this same method will perform GET request too
     if request.method =='POST':
          data = request.form
          fName = data.get('first_name')
          sName = data.get('last_name')
          pwd = data.get('password')
          
          if (len(fName) < 5):
               flash('Data is not enough', category="error")
          else:
               flash("Login successfully", category='success')

     return render_template('form.html')
from flask import Flask, render_template

import os
app = Flask(__name__)

@app.route("/pramshigh/")
@app.route('/coding/index/')
def pramshigh():
    #    main app leading to the homepage of the app
       return render_template('index.html')
    

@app.route("/pramshigh/fisher/")
@app.route("/fisher/")
def fisher():
      return render_template('fisher.html')

@app.route("/pramshigh/courses/")
def courses():
     courses= ['Business', 'Scince', 'Home Econs (1)', 'Christian Religious Service']
     le = len(courses)
     return render_template('courses.html', courses=courses, lens=le)

@app.route("/navigation/")
def navigation():
     return render_template('navigation.html')

@app.route('/timetable/')
def timetable():
     return render_template('timetable_f1.html')

@app.route("/pramshigh/form/")
def form():

     return render_template('form.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)

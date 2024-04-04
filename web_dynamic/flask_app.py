from flask import Flask, render_template
import os
app = Flask(__name__)

@app.route("/pramshigh/")
@app.route('/coding/index/')
def pramshigh():
    #    main app leading to the homepage of the app
       return render_template('index.html')
    

@app.route("/home/fisher/")
@app.route("/fisher/")
def fisher():
      return render_template('fisher.html')

@app.route("/courses/")
def courses():
     return render_template('courses.html')

@app.route("/navigation/")
def navigation():
     return render_template('navigation.html')

@app.route('/timetable/')
def timetable():
     return render_template('f1_va_timetable.html')

@app.route('/form/')
def form():
     return render_template('form.html')

if __name__ == "__main__":
    app.run(debug=True)

from flask import Flask, render_template
import os
app = Flask(__name__)

@app.route("/home/")
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

@app.route("/base/")
def base_url():
     return render_template('base.html')

@app.route('/coding/')
def forms():
     return render_template('coding.html')

if __name__ == "__main__":
    app.run(debug=True)

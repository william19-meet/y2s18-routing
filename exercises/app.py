from databases import *
from flask import Flask, render_template, url_for
app = Flask(__name__)

@app.route('/')
def home_route():
    return render_template('home.html')
@app.route('/students/<int:id>')
def student(id):
    return render_template("student.html", name = 'william', student_id = id)
app.run(debug=True)

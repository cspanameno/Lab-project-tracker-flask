from flask import Flask, request, render_template

import hackbright

app = Flask(__name__)

@app.route('/')
def index():
    """Home page for project tracker"""

    student_list = hackbright.get_list_of_students()
    project_list = hackbright.get_project_list()

    return render_template('index.html', student_list=student_list, project_list=project_list)

@app.route("/student")
def get_student():
    """Show information about a student."""

    github = request.args.get('github','jhacks')
    first, last, github = hackbright.get_student_by_github(github)
    student_grades = hackbright.get_grades_by_github(github)
    html = render_template("student_info.html", first=first, last=last, github=github, student_grades=student_grades)
    
    return html

@app.route("/student_search")
def get_student_form():
    """Show form for searching for a student."""

    return render_template("student_search.html")

@app.route('/student_add')
def student_add():
    """Add a record for a new student"""

    return render_template('student_add.html')

@app.route('/student_add_confirmation', methods=['POST'])
def student_add_confirmation():
    """Show confirmation page after new student form submitted"""

    fname = request.form.get('fname')
    lname = request.form.get('lname')
    github = request.form.get('github')
    hackbright.make_new_student(fname, lname, github)
    
    return render_template('student_add_confirmation.html', fname=fname, lname=lname, github=github)

@app.route('/project', methods=['GET'])
def project():

    title = request.args.get('title')
    project_info = hackbright.get_project_by_title(title)
    grade_info = hackbright.get_grades_by_title(title) 


    return render_template('project_info.html', project_info=project_info, grade_info=grade_info)

if __name__ == "__main__":
    hackbright.connect_to_db(app)
    app.run(debug=True)

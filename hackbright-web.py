from flask import Flask, request, render_template

import hackbright

app = Flask(__name__)


@app.route("/student")
def get_student():
    """Show information about a student."""

    github = request.args.get('github','jhacks')
    first, last, github = hackbright.get_student_by_github(github)
    html = render_template("student_info.html", first=first, last=last, github=github)
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

if __name__ == "__main__":
    hackbright.connect_to_db(app)
    app.run(debug=True)

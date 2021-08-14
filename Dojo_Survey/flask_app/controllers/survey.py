from flask_app import app
from flask import render_template, request, redirect, session
from flask_app.models.survey import Survey
# from flask_app.models.survey import Survey


@app.route('/')
def index():
    return render_template("index.html")

    
@app.route('/results/validate', methods=['POST'])
def validate():
    if not Survey.validate_survey(request.form):
        return redirect('/')

    Survey.save_information(request.form)
    return render_template('show.html', survey_data = request.form)

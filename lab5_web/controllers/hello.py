import constants
from app import app
from flask import render_template, request

@app.route('/', methods=['GET', 'POST'])
def hello():
    name = ""
    gender = ""
    program_id = 0
    subject_id = []

    if request.method == 'POST':
        submit_button_value = request.form.get('submit')
        clear_button_value = request.form.get('clean')

        if submit_button_value:
            name = request.form.get('username')
            gender = request.form.get('gender')
            program_id = int(request.form.get('program'))
            subject_id = request.form.getlist('subject[]')

        elif clear_button_value:
            name = ""
            gender = ""
            program_id = 0
            subject_id = []

    subjects_select = [constants.subjects[int(i)] for i in subject_id]

    html = render_template(
        'hello.html',
        name=name,
        gender=gender,
        program=constants.programs[program_id],
        program_list=constants.programs,
        len=len,
        subjects_select=subjects_select,
        subject_list=constants.subjects
    )

    return html

import constants
from app import app
from flask import render_template, request

@app.route('/', methods=['GET', 'POST'])
def index():

    if request.method == 'POST':
        input_type = request.form.get('input_type')
        if request.form.get('clean'):
            input_type = None

        if request.form.get('show') or request.form.get('clean'):
            side_a = 1
            side_b = 1
            height = 1
            height_b = 1
            angle = 1
            calc_id = []

        else:
            side_a = request.form.get('side_a')
            side_b = request.form.get('side_b')
            height = request.form.get('height')
            height_b = request.form.get('height_b')
            angle = request.form.get('angle')
            calc_id = request.form.getlist('calc[]')

        if side_a and (input_type == 'first' or input_type == 'second'):
            side_a = int(side_a)

        if side_b and input_type == 'second':
            side_b = int(side_b)

        if height and input_type == 'second':
            height = int(height)

        if height_b and input_type == 'first':
            height_b = int(height_b)

        if angle and input_type == 'first':
            angle = int(angle)

        calculation_select = [constants.calculations[int(i)] for i in calc_id]
        result = {}
        if request.form.get('submit'):
            if 'Площадь параллелограмма' in calculation_select:
                if input_type == 'first' and side_a > 0 and height_b > 0 and angle > 0:
                    result['Площадь параллелограмма'] = constants.calculate_area_case1(side_a, height_b, angle)
                if input_type == 'second' and side_a > 0 and side_b > 0 and height > 0:
                    result['Площадь параллелограмма'] = constants.calculate_area_case2(side_a, side_b, height)

            if 'Диагонали параллелограмма' in calculation_select:
                if input_type == 'first' and side_a > 0 and height_b > 0 and angle > 0:
                    result['Диагонали параллелограмма'] = constants.calculate_diagonals_case1(side_a, height_b, angle)
                if input_type == 'second' and side_a > 0 and side_b > 0 and height > 0:
                    result['Диагонали параллелограмма'] = constants.calculate_diagonals_case2(side_a, side_b, height)

            if 'Угол между диагоналями' in calculation_select:
                if input_type == 'first' and side_a > 0 and height_b > 0 and angle > 0:
                    result['Угол между диагоналями'] = constants.calculate_angle_between_diagonals_case1(side_a, height_b, angle)
                if input_type == 'second' and side_a > 0 and side_b > 0 and height > 0:
                    result['Угол между диагоналями'] = constants.calculate_angle_between_diagonals_case2(side_a, side_b, height)

        return render_template('index.html',
                               result=result,
                               input_type=input_type,
                               side_a=side_a,
                               side_b=side_b,
                               height_b=height_b,
                               height=height,
                               calc_select = calculation_select,
                               calculation_list = constants.calculations,
                               angle=angle,
                               len=len)

    return render_template('index.html')


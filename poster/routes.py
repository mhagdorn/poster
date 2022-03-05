from flask import render_template
from flask import session
from flask import redirect, url_for

from .application import app
from .forms import DataForm


@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    form = DataForm()

    if form.validate_on_submit():
        session['start_year'] = form.start_year.data
        session['income'] = form.income.data

        return redirect(url_for('result'))

    return render_template('index.html', form=form,
                           title="Edinburgh Pay Modeller")


@app.route('/result')
def result():
    for field in ['start_year', 'income']:
        if field not in session:
            print(f'error {field}')
            return redirect(url_for('index'))
    return render_template(
        'result.html',
        years=session['start_year'],
        income=session['income'])

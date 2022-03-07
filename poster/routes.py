from flask import render_template
from flask import session
from flask import redirect, url_for

from .application import app
from .forms import DataForm, EmailForm
from .compound import pay_loss, cummulative
from .worker import producePoster


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


@app.route('/result', methods=['GET', 'POST'])
def result():
    for field in ['start_year', 'income']:
        if field not in session:
            print(f'error {field}')
            return redirect(url_for('index'))

    data = {
        'start_year': session['start_year'],
        'pay_loss': pay_loss,
        'salary_diff': (1 + pay_loss / 100) * session['income'],
        'total_loss': cummulative(session['start_year'], session['income'])}

    form = EmailForm()
    if form.validate_on_submit():
        producePoster.delay(form.email.data, data)
    return render_template(
        'result.html', form=form, **data)


@app.route('/poster')
def poster():
    for field in ['start_year', 'income']:
        if field not in session:
            print(f'error {field}')
            return redirect(url_for('index'))

    return render_template(
        'poster/uoe.svg',
        start_year=session['start_year'],
        pay_loss=pay_loss,
        salary_diff=(1 + pay_loss / 100) * session['income'],
        total_loss=cummulative(session['start_year'], session['income']))

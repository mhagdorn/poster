from flask import render_template

from .application import app
from .forms import DataForm


@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    form = DataForm()

    if form.validate_on_submit():
        print(form.spinalPoint.data)

    return render_template('index.html', form=form)

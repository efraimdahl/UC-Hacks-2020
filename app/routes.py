from flask import render_template, flash, redirect
from app import app
from app.forms import TextEntry

@app.route('/')
@app.route('/index', methods=['GET', 'POST'])
def index():
    form = TextEntry()
    if form.validate_on_submit():
        flash('Entered {}'.format(
            form.food.data))
        return redirect('/index')
    return render_template('index.html', title='Enter Food', form=form)
@app.route('/about')
def about():
    return render_template('about.html')

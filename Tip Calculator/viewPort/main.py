from viewPort import app 
from flask import redirect, render_template,url_for
from datetime import datetime

@app.route('/')
def root():
    date = datetime.today()
    return render_template('main.html',date = date)
from pages import app
from flask import Flask, render_template,url_for

@app.route('/')
def root():
    return render_template('main.html')
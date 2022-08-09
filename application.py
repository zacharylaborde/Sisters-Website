""" Sample module docstring """
from flask import Flask, render_template

application = Flask(__name__)


@application.route('/')
@application.route('/home')
def home():
    """ Sample function docstring """
    return render_template("home.html")


@application.route('/services')
def services():
    """ Sample function docstring """
    return "<h1>Services</h1>"


@application.route('/contact')
def contact():
    """ Sample function docstring """
    return "<h1>Contact Me</h1>"


@application.route('/faq')
def faq():
    """ Sample function docstring """
    return "<h1>FAQ</h1>"


if __name__ == '__main__':
    application.run()

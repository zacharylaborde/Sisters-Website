""" Sample module docstring """
from flask import Flask, render_template
from forms import SendEmail

application = Flask(__name__)

application.config['SECRET_KEY'] = '19k1u25gggre1d8iwIUDddfa1'

service_list = [
    {
        'name': 'Service 1',
        'price': '$$$',
        'duration': 'xHr & xxMin'
    },
    {
        'name': 'Service 2',
        'price': '$$$',
        'duration': 'xHr & xxMin'
    },
    {
        'name': 'Service 3',
        'price': '$$$',
        'duration': 'xHr & xxMin'
    },
    {
        'name': 'Service 4',
        'price': '$$$',
        'duration': 'xHr & xxMin'
    }
]


@application.route('/')
@application.route('/home')
def home():
    """ Sample function docstring """
    return render_template("home.html")


@application.route('/services')
def services():
    """ Sample function docstring """
    return render_template("services.html", services=service_list)


@application.route('/contact')
def contact():
    """ Sample function docstring """
    form = SendEmail()
    return render_template("contact.html", form=form)


@application.route('/faq')
def faq():
    """ Sample function docstring """
    return render_template("faq.html")


if __name__ == '__main__':
    application.run()

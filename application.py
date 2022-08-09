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

faqs = [
    {
        'question': 'Question 1?',
        'answer': 'Answer to question 1.'
    },
    {
        'question': 'Question 2?',
        'answer': 'Answer to question 2.'
    },
    {
        'question': 'Question 3?',
        'answer': 'Answer to question 3.'
    },
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
    return render_template("faq.html", faqs=faqs)


if __name__ == '__main__':
    application.run()

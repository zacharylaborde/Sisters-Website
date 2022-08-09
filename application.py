""" Sample module docstring """
from flask import Flask, render_template
from forms import SendEmail

application = Flask(__name__)

application.config['SECRET_KEY'] = '19k1u25gggre1d8iwIUDddfa1'

service_list = [
    {
        'name': 'Complimentary Consultation (Required for Balayage, Fantasy Colors, '
                'Color Correction, Ect.)',
        'price': 'FREE',
        'duration': '15m'
    },
    {
        'name': 'Wash Cut & Blowdry',
        'price': '$50-$60',
        'duration': '1h 30m'
    },
    {
        'name': 'Blowdry',
        'price': '$40-$50',
        'duration': '1h'
    },
    {
        'name': '+ EXTRA LONG HAIR (past mid back)',
        'price': '$10',
        'duration': '5m'
    },
    {
        'name': '+ Flat/Curling Iron',
        'price': '$10-$20',
        'duration': '20m'
    },
    {
        'name': '+ K Recovery Reconstruction Treatment',
        'price': '$25',
        'duration': '15m'
    },
    {
        'name': '+ Silk Degrees Treatment',
        'price': '$20',
        'duration': '20m'
    },
    {
        'name': 'Mens Cut',
        'price': '$25',
        'duration': '30m'
    },
    {
        'name': 'Wet HairCut (No Blowdry)',
        'price': '$25',
        'duration': '45m'
    },
    {
        'name': 'Child Wash & Cut (under 12)',
        'price': '$20',
        'duration': '30m'
    },
    {
        'name': 'Child Wash Cut & Blowdry (under 12)',
        'price': '$35-45',
        'duration': '1h'
    },
    {
        'name': 'Full Color',
        'price': '$70-90',
        'duration': '1h 20m'
    },
    {
        'name': 'Root touch up',
        'price': '$55-$65',
        'duration': '1h'
    },
    {
        'name': 'Toner/Glaze',
        'price': '$25-$35',
        'duration': '30m'
    },
    {
        'name': 'Partial Hightlight',
        'price': '$85-$100',
        'duration': '2h 30m'
    },
    {
        'name': 'Full Highlight',
        'price': '$110-$165',
        'duration': '3h 30m'
    },
    {
        'name': 'Eyebrow Waxing',
        'price': '$15',
        'duration': '15m'
    },
    {
        'name': 'Lip Waxing',
        'price': '$10',
        'duration': '15m'
    },
    {
        'name': 'Chin Waxing',
        'price': '$10',
        'duration': '15m'
    },
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

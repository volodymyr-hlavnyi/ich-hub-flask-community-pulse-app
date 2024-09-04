from flask import Blueprint

response_bp = Blueprint('responses', __name__, url_prefix= '/responses')


@response_bp.route('/')
def get_all_responses():
    return "ALL RESPONSES"


@response_bp.route('/add', methods = ['POST'])
def add_new_responses():
    return "RESPONSE IS ADDED"
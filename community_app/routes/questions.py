from flask import Blueprint

question_bp = Blueprint('questions', __name__, url_prefix= '/questions')


@question_bp.route('/')  # url/questions/
def get_all_questions():
    return "ALL QUESTIONS"


@question_bp.route('/add', methods = ['POST'])
def add_new_question():
    return "QUESTION IS ADDED"
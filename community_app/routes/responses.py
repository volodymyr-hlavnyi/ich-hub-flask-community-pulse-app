from flask import Blueprint, make_response, jsonify
from community_app.models.questions import Statistics

response_bp = Blueprint('responses', __name__, url_prefix='/responses')


@response_bp.route('/', methods=['GET'])
def get_all_responses():
    statistic = Statistics.query.all()
    statistic_data = [
        {
            'question_id': stat.question_id,
            'agree_count': stat.agree_count,
            'disagree_count': stat.disagree_count
        }
        for stat in statistic
    ]

    response = make_response(jsonify(statistic_data), 200)
    return response


@response_bp.route('/add', methods=['POST'])
def add_new_responses():
    return "RESPONSE IS ADDED"

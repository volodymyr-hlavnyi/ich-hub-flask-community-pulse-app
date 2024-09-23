from flask import Blueprint, make_response, jsonify
from community_app.models.questions import Statistics

response_bp = Blueprint('responses', __name__, url_prefix='/responses')


@response_bp.route('/', methods=['GET'])
def get_responses():
    statistics = Statistics.query.all()
    results = [
        {
            "question_id": stat.question_id,
            "agree_count": stat.agree_count,
            "disagree_count": stat.disagree_count
        }
        for stat in statistics
    ]

    response = make_response(jsonify(results), 200)
    return response


@response_bp.route('/', methods=['POST'])
def add_responses():
    return "RESPONSE IS ADDED"

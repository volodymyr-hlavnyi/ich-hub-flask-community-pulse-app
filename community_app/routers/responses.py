from flask import Blueprint, make_response, jsonify, request

from community_app import db
from community_app.models.questions import Statistics, Questions
from community_app.models.responses import Responses  # Import your custom Responses model

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
def add_response():
    data = request.get_json()
    if not data or 'question_id' not in data or 'is_agree' not in data:
        return jsonify({'message': "Некорректные данные"}), 400

    is_agree = data['is_agree'].lower() == 'true'

    question = Questions.query.get(data['question_id'])
    if not question:
        return jsonify({'message': "Вопрос не найден"}), 404

    response = Responses(
        question_id=question.id,
        is_agree=is_agree
    )

    db.session.add(response)
    # Обновление статистики
    statistic = Statistics.query.filter_by(question_id=question.id).first()
    if not statistic:
        statistic = Statistics(question_id=question.id, agree_count=0, disagree_count=0)

    db.session.add(statistic)
    if is_agree:
        statistic.agree_count += 1
    else:
        statistic.disagree_count += 1
    db.session.commit()

    return jsonify({'message': f"Ответ на вопрос {question.id} добавлен"}), 201

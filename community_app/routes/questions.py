from flask import Blueprint, jsonify, make_response, request
from community_app.models.questions import Questions
from community_app import db

question_bp = Blueprint('questions', __name__, url_prefix='/questions')


@question_bp.route('/', methods=['GET'])  # url/questions/
def get_all_questions():
    questions: list[Questions] = Questions.query.all()

    questions_data: list[dict] = [
        {"id": question.id,
         "text": question.text,
         "created_at": question.created_at
         }
        for question in questions]

    response = make_response(jsonify(questions_data), 200)
    response.headers["Custom-Header"] = "our custom header"

    return response


@question_bp.route('/add', methods=['POST'])
def add_new_question():
    data = request.get_json()

    if not data or 'text' not in data:
        return jsonify({
            'message': "NO DATA Provided"
        }, 400)
    question: Questions = Questions(text=data['text'])

    db.session.add(question)
    db.session.commit()

    return jsonify({"message": "NEW QUESTION ADDED",
                    "question_id": question.id}), 201


@question_bp.route('/update/<int:question_id>', methods=['PUT'])
def update_question(question_id):
    question: Questions = Questions.query.get(question_id)

    if not question:
        return make_response(jsonify({
            "message": "NOT FOUND"
        }), 404)
    request_data = request.get_json()
    if request_data['text']:
        question.text = request_data['text']
        db.session.commit()
        return make_response(jsonify({
            "message": "FILE UPDATED",
            "NEW_TEXT": question.text
        }), 200)
    else:
        return make_response(jsonify({
            "message": "NO DATA PROVIDED"
        }), 204)

from crypt import methods
from unicodedata import category

from flask import Blueprint, jsonify, make_response, request
from community_app.models.questions import Questions
from community_app import db

question_bp = Blueprint('questions', __name__, url_prefix='/questions')


@question_bp.route('/<int:question_id>', methods=['GET'])
def get_question(question_id):
    question: Questions = Questions.query.get(question_id)

    if not question:
        return make_response(jsonify({
            "message": "NOT FOUND"
        }), 404)

    question_data = {
        "id": question.id,
        "text": question.text,
        "created_at": question.created_at
    }

    return jsonify(question_data), 200


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


@question_bp.route('/', methods=['POST'])
def create_question():
    """Создание нового вопроса."""
    data = request.get_json()  # Получаем данные из запроса в формате JSON
    if not data or 'text' not in data:
        # Проверяем, что текст вопроса присутствует в данных
        return jsonify({'error': 'No question text provided'}), 400

    # Создаем экземпляр вопроса
    question = Questions(text=data['text'], category_id=data['category_id'])
    db.session.add(question)  # Добавляем вопрос в сессию для записи
    db.session.commit()  # Фиксируем изменения в базе данных
    return jsonify({'message': 'Вопрос создан', 'id': question.id}), 201


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


@question_bp.route('/<int:id>', methods=['DELETE'])
def delete_question(id):
    question: Questions = Questions.query.get(id)

    if not question:
        return make_response(jsonify({
            "message": "NOT FOUND"
        }), 404)

    db.session.delete(question)
    db.session.commit()

    return make_response(jsonify({
        "message": "DELETED with ID: " + str(id)
    }), 200)

# community_app/routers/categories.py
from flask import Blueprint, jsonify, request, make_response
from community_app import db
from community_app.models.categories import Categories
from community_app.schemas.question import CategoryBase
from pydantic import ValidationError

category_bp = Blueprint('categories', __name__, url_prefix='/categories')


@category_bp.route('/', methods=['POST'])
def create_categories():
    data = request.get_json()
    try:
        category_data = CategoryBase(**data)
    except ValidationError as e:
        return jsonify({'message': 'Validation error', 'errors': e.errors()}), 400

    category = Categories(name=category_data.name)
    db.session.add(category)
    db.session.commit()
    return jsonify({'message': 'Category created', 'id': category.id}), 201


@category_bp.route('/', methods=['GET'])
def get_categories():
    categories = Categories.query.all()
    results = [CategoryBase.from_orm(category).dict() for category in categories]
    return jsonify(results), 200


@category_bp.route('/<int:id>', methods=['PUT'])
def update_categories(id):
    category = Categories.query.get(id)
    if not category:
        return make_response(jsonify({'message': 'Category not found'}), 404)

    data = request.get_json()
    try:
        category_data = CategoryBase(**data)
    except ValidationError as e:
        return jsonify({'message': 'Validation error', 'errors': e.errors()}), 400

    category.name = category_data.name
    db.session.commit()
    return jsonify({'message': 'Category updated', 'id': category.id}), 200


@category_bp.route('/<int:id>', methods=['DELETE'])
def delete_categories(id):
    category = Categories.query.get(id)
    if not category:
        return make_response(jsonify({'message': 'Category not found'}), 404)

    db.session.delete(category)
    db.session.commit()
    return jsonify({'message': 'Category deleted', 'id': id}), 200

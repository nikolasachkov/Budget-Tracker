from flask import request, jsonify
from app import app, db
from app.models.models import Transaction
from app.services.services import create_transaction, delete_transaction, update_transaction
from sqlalchemy.exc import IntegrityError, SQLAlchemyError
from werkzeug.exceptions import HTTPException, BadRequest

@app.route('/')
def index():
    return jsonify({'message': 'Welcome to the Budget Tracker API!'}), 200

@app.route('/transactions', methods=['POST'])
def add_transaction():
    try:
        data = request.get_json()
        if not data:
            raise BadRequest('No input data provided')
        transaction = create_transaction(data)
        return jsonify(transaction.as_dict()), 201
    except IntegrityError:
        db.session.rollback()
        return jsonify({'message': 'Could not create the transaction due to integrity error'}), 400
    except BadRequest as e:
        return jsonify({'message': str(e)}), 400

@app.route('/transactions', methods=['GET'])
def get_all_transactions():
    transactions = Transaction.query.all()
    transactions_data = [transaction.as_dict() for transaction in transactions]
    return jsonify(transactions_data), 200

@app.route('/transactions/<int:transaction_id>', methods=['PUT'])
def update_transaction_route(transaction_id):
    data = request.get_json()
    transaction = update_transaction(transaction_id, data)
    if transaction:
        return jsonify(transaction), 200
    else:
        return jsonify({"message": "Transaction not found"}), 404

@app.route('/transactions/<int:transaction_id>', methods=['DELETE'])
def delete_transaction_route(transaction_id):
    result = delete_transaction(transaction_id)
    if result:
        return jsonify({"message": "Transaction deleted"}), 200
    else:
        return jsonify({"message": "Transaction not found"}), 404
    

@app.errorhandler(404)
def resource_not_found(e):
    return jsonify({'message': 'Resource not found'}), 404

@app.errorhandler(500)
def internal_server_error(e):
    return jsonify({'message': 'Internal server error'}), 500

def handle_http_exception(e):
    response = e.get_response()
    response.data = jsonify({
        "code": e.code,
        "name": e.name,
        "description": e.description,
    })
    response.content_type = "application/json"
    return response


@app.errorhandler(SQLAlchemyError)
def handle_sqlalchemy_error(e):
    db.session.rollback()
    return jsonify({'message': 'Database error occurred', 'error': str(e)}), 500



@app.errorhandler(Exception)
def handle_exception(e):
    return jsonify({'message': 'An unexpected error occurred', 'error': str(e)}), 500
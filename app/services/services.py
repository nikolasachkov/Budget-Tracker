from app import db
from app.models.models import Transaction
from datetime import datetime

def create_transaction(data):
    new_transaction = Transaction(
        title=data['title'],
        amount=data['amount'],
        date=datetime.strptime(data['date'], '%Y-%m-%d')
    )
    db.session.add(new_transaction)
    db.session.commit()
    return new_transaction

def update_transaction(transaction_id, data):
    transaction = Transaction.query.get(transaction_id)
    if transaction:
        transaction.title = data.get('title', transaction.title)
        transaction.amount = data.get('amount', transaction.amount)
        # Update the date only if it's provided
        if 'date' in data:
            transaction.date = datetime.strptime(data['date'], '%Y-%m-%d')
        db.session.commit()
        return transaction
    else:
        return None

def delete_transaction(transaction_id):
    transaction = Transaction.query.get(transaction_id)
    if transaction:
        db.session.delete(transaction)
        db.session.commit()
        return True
    else:
        return False

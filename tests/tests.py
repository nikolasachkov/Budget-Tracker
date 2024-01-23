import unittest
from app import app, db
from app.models.models import Transaction
from datetime import datetime

class BudgetTrackTestCase(unittest.TestCase):

    def setUp(self):
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
        app.config['TESTING'] = True
        self.app = app.test_client()

        with app.app_context():
            db.create_all()

    def tearDown(self):
        with app.app_context():
            db.session.remove()
            db.drop_all()

    def test_add_transaction(self):
        response = self.app.post('/transactions', json={
            'title': 'Test Transaction',
            'amount': 100.00,
            'date': '2021-01-01'
        })
        self.assertEqual(response.status_code, 201)
        self.assertIn('Test Transaction', str(response.data))


if __name__ == '__main__':
    unittest.main()
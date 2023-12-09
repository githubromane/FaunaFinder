import unittest
from flask import Flask
from app import app, db  

class TestAppFunctionality(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'  # Use an in-memory database for testing
        self.app = app.test_client()
        with app.app_context():
            db.create_all()

    def tearDown(self):
        with app.app_context():
            db.drop_all()

    def test_index_page(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)

    
if __name__ == '__main__':
    unittest.main()

import unittest
from flask_testing import TestCase
from app import app, db, Todo

#------------TO RUN -----------
#python -m unittest test_app.py

class TestApp(TestCase):
    def create_app(self):
        app.config['TESTING'] = True
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test_.db'  # Utiliser une base de données distincte pour les tests
        return app

    def setUp(self):
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_index_route(self):
        response = self.client.get('/')
        self.assert200(response)
        self.assert_template_used('index.html')

    def test_add_task(self):
        initial_tasks_count = Todo.query.count()

        response = self.client.post('/', data={'content': 'Test Task'})
        self.assertRedirects(response, '/')

        new_tasks_count = Todo.query.count()
        self.assertEqual(new_tasks_count, initial_tasks_count + 1)

    def test_delete_task(self):
        task = Todo(content='Test Task')
        db.session.add(task)
        db.session.commit()
        initial_tasks_count = Todo.query.count()

        response = self.client.get(f'/delete/{task.id}')
        self.assertRedirects(response, '/')

        new_tasks_count = Todo.query.count()
        self.assertEqual(new_tasks_count, initial_tasks_count - 1)

    def test_update_task(self):
        task = Todo(content='Test Task')
        db.session.add(task)
        db.session.commit()
        updated_content = 'Updated Task'

        response = self.client.post(f'/update/{task.id}', data={'content': updated_content})
        self.assertRedirects(response, '/')

        updated_task = Todo.query.get(task.id)
        self.assertEqual(updated_task.content, updated_content)

if __name__ == '__main__':
    unittest.main()


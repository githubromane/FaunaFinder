from flask import url_for
from app import app, db 
import pytest

@pytest.fixture
def client():
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
    client = app.test_client()

    with app.app_context():
        db.create_all()

    yield client

    with app.app_context():
        db.drop_all()


def test_index_page(client):
    response = client.get(url_for('index'))
    assert response.status_code == 200


def test_add_gift(client):
    response = client.post(url_for('index'), data={'content': 'Test Gift'})
    assert response.status_code == 302 
    assert 'Test Gift' in response.get_data(as_text=True)


def test_update_gift(client):
    task_id = 1
    response = client.post(url_for('update', id=task_id), data={'content': 'Updated Gift'})
    assert response.status_code == 302  
    
    response = client.get(url_for('index'))
    assert 'Updated Gift' in response.get_data(as_text=True)


def test_delete_gift(client):
    task_id = 1
    response = client.get(url_for('delete', id=task_id))
    assert response.status_code == 302  

    response = client.get(url_for('index'))
    assert 'Updated Gift' not in response.get_data(as_text=True)

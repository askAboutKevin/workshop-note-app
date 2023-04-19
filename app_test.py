import pytest
from app import app

notes = [
    {
        "id": 1,
        "title": "New note",
        "content": "This is a new note"
    }
]


# Use the pytest-flask plugin to create a test client for the Flask app
@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client


def test_get_notes(client):
    response = client.get('/notes')
    assert response.status_code == 200


def test_create_note(client):
    new_note = {'id': 1, 'title': 'New note', 'content': 'This is a new note'}
    response = client.post('/notes', json=new_note)
    assert response.status_code == 201


def test_update_note(client):
    update_note = {'title': 'Updated note', 'content': 'This note has been updated'}
    response = client.put('/notes/1', json=update_note)
    assert response.status_code == 200


def test_delete_note(client):
    response = client.delete('/notes/1')
    assert response.status_code == 204

from app import app

def test_hello_world():
    assert True

def test_chatgpt():
    app.chatgpt()
    assert True
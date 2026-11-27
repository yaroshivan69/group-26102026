from app.main import add, multiply, greet
def test_numbers_result():
    assert add(2, 3) == {'result': 5, 'status': 'success'}
    assert multiply(2, 3, 4) == {'result': 24, 'status': 'success'}

def test_string_result():
    assert greet("Оля") == {'result': 'Привіт, Оля!', 'status': 'success'}
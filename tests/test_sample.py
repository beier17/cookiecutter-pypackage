# tests/test_sample.py

def test_addition():
    assert 2 + 3 == 5

def test_string():
    text = "hello"
    assert text.upper() == "HELLO"

def test_list_length():
    items = [1, 2, 3]
    assert len(items) == 3
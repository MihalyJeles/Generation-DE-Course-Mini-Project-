from unittest.mock import patch
# from src.app import input_int_expect

def input_int_expect():
    while True:
        try:
            input_int = int(input('\nPlease enter a number from the available options: '))
            return input_int
        except (OverflowError,ValueError,NameError,IndexError):
            input_int = 1000
            return input_int


@patch('builtins.input')
def test_input_valid_int(mock_input):
    mock_input.return_value = 1
    expected = 1

    result = input_int_expect()

    assert result == expected
    assert mock_input.call_count == 1

@patch('builtins.input')
def test_input_string(mock_input):
    mock_input.return_value = 'one'
    expected = 1000

    result = input_int_expect()

    assert result == expected
    assert mock_input.call_count == 1

@patch('builtins.input')
def test_input_empty(mock_input):
    mock_input.return_value = ''
    expected = 1000

    result = input_int_expect()

    assert result == expected
    assert mock_input.call_count == 1

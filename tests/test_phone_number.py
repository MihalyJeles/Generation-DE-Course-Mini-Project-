from unittest.mock import patch
import re


def input_phone_expect():
        try:
            input_str = input("Please type in customer's phone number: ")
            if not re.match("^[0-9,+]*$", input_str):
                return "Error! Only numbers 0-9 and  '+' allowed!"
            elif len(input_str) >= 11 and len(input_str) <= 13:
                return input_str
            else:
                return "Error! Only 11-13 characters allowed!"
        except (OverflowError,ValueError,NameError,IndexError):
            return"Invalid value!"


@patch('builtins.input')
def test_input_phone_normal(mock_input):
    mock_input.return_value = '+447448968776'
    expected = '+447448968776'

    result = input_phone_expect()

    assert result == expected
    assert mock_input.call_count == 1

@patch('builtins.input')
def test_input_phone_too_long(mock_input):
    mock_input.return_value = '074489687764567845345'
    expected = "Error! Only 11-13 characters allowed!"

    result = input_phone_expect()

    assert result == expected
    assert mock_input.call_count == 1

@patch('builtins.input')
def test_input_phone_too_short(mock_input):
    mock_input.return_value = '073454'
    expected = "Error! Only 11-13 characters allowed!"

    result = input_phone_expect()

    assert result == expected
    assert mock_input.call_count == 1

@patch('builtins.input')
def test_input_phone_invalid_characters(mock_input):
    mock_input.return_value = 'rr?073454345'
    expected = "Error! Only numbers 0-9 and  '+' allowed!"

    result = input_phone_expect()

    assert result == expected
    assert mock_input.call_count == 1


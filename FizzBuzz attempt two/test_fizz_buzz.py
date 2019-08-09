from app import main


def test_main_returns_value_when_it_is_zero():
    # Act
    fizzbuzz_input = 0

    # Assert
    result = main(fizzbuzz_input)

    # Arrange
    assert result == fizzbuzz_input


def test_main_returns_fizz():
    # Act
    fizzbuzz_input = 21

    # Assert
    result = main(fizzbuzz_input)

    # Arrange
    assert result == 'fizz'


def test_main_returns_value_when_not_fizz_or_buzz():
    # Act
    fizzbuzz_input = 2

    # Arrange
    result = main(fizzbuzz_input)

    # Assert
    assert result == fizzbuzz_input


def test_returns_buzz():
    # Arrange
    fizzbuzz_input = 25

    # Act
    result = main(fizzbuzz_input)

    # Arrange
    assert result == 'buzz'


def test_returns_fizzbuzz():
    # Act
    fizzbuzz_input = 15

    # Arrange
    result = main(fizzbuzz_input)

    # Assert
    assert result == 'fizzbuzz'

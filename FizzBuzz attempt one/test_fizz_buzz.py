from app import is_input_fizz, is_input_buzz, is_input_fizzbuzz, main


def test_main_returns_fizzbuzz():
    # Act
    fizzbuzz_input = 30

    # Arrange
    result = main(fizzbuzz_input)

    # Assert
    assert result == 'fizzbuzz'


def test_main_returns_buzz():
    # Act
    fizzbuzz_input = 20

    # Arrange
    result = main(fizzbuzz_input)

    # Assert
    assert result == 'buzz'


def test_main_returns_fizz():
    # Act
    fizzbuzz_input = 21

    # Assert
    result = main(fizzbuzz_input)

    # Arrange
    assert result == 'fizz'


def test_main_returns_value_when_it_is_zero():
    # Act
    fizzbuzz_input = 0

    # Assert
    result = main(fizzbuzz_input)

    # Arrange
    assert result == fizzbuzz_input


def test_main_returns_value_when_not_fizz_or_buzz():
    # Act
    fizzbuzz_input = 2

    # Arrange
    result = main(fizzbuzz_input)

    # Assert
    assert result == fizzbuzz_input


def test_returns_fizzbuzz():
    # Act
    fizzbuzz_input = 15

    # Arrange
    result = is_input_fizzbuzz(fizzbuzz_input)

    # Assert
    assert result == 'fizzbuzz'


def test_returns_value_when_not_fizzbuzz():
    # Act
    fizzbuzz_input = 14

    # Assert
    result = is_input_fizzbuzz(fizzbuzz_input)

    # Assert
    assert result == fizzbuzz_input


def test_returns_buzz_with_five():
    # Arrange
    fizzbuzz_input = 25

    # Act
    result = is_input_buzz(fizzbuzz_input)

    # Arrange
    assert result == 'buzz'


def test_returns_input_when_not_buzz():
    # Arrange
    fizzbuzz_input = 4

    # Act
    result = is_input_buzz(fizzbuzz_input)

    # Arrange
    assert result == fizzbuzz_input


def test_returns_fizz_with_three():
    # Arrange
    fizzbuzz_input = 12

    # Act
    result = is_input_fizz(fizzbuzz_input)

    # Assert
    assert result == 'fizz'


def test_returns_value_when_not_fizz():
    # Arrange
    fizzbuzz_input = 17

    # Act
    result = is_input_fizz(fizzbuzz_input)

    # Assert
    assert result == fizzbuzz_input

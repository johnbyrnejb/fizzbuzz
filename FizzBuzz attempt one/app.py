from random import randint

fizzbuzz_input = randint(-100, 100)


def is_input_fizz(fizzbuzz_input):
    if int(fizzbuzz_input) % 3 == 0:
        return 'fizz'
    else:
        return fizzbuzz_input


def is_input_buzz(fizzbuzz_input):
    if int(fizzbuzz_input) % 5 == 0:
        return 'buzz'
    else:
        return fizzbuzz_input


def is_input_fizzbuzz(fizzbuzz_input):
    if (int(fizzbuzz_input) % 3 == 0) and (int(fizzbuzz_input) % 5 == 0):
        return 'fizzbuzz'
    else:
        return fizzbuzz_input


def main(fizzbuzz_input):
    print(f'This is the random number: {fizzbuzz_input}')

    if fizzbuzz_input == 0:
        print(fizzbuzz_input)
        return fizzbuzz_input
    elif is_input_fizzbuzz(fizzbuzz_input) == 'fizzbuzz':
        print('Wow, that is a fizzbuzz')
        return 'fizzbuzz'
    elif is_input_fizz(fizzbuzz_input) == 'fizz':
        print('That is a Fizz')
        return 'fizz'
    elif is_input_buzz(fizzbuzz_input) == 'buzz':
        print('That is a Buzz')
        return 'buzz'
    else:
        print(fizzbuzz_input)
        return fizzbuzz_input


if __name__ == '__main__':
    main(fizzbuzz_input)

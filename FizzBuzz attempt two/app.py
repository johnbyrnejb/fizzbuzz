from random import randint

fizzbuzz_import = randint(-100, 100)


def main(fizzbuzz_input):
    if fizzbuzz_input == 0:
        print(fizzbuzz_input)
        return fizzbuzz_input
    elif (int(fizzbuzz_input) % 3 == 0) and (int(fizzbuzz_input) % 5 == 0):
        print('This is a Fizz Buzz')
        return 'fizzbuzz'
    elif int(fizzbuzz_input) % 3 == 0:
        print('That is a Fizz')
        return 'fizz'
    elif int(fizzbuzz_input) % 5 == 0:
        print('That is a Buzz')
        return 'buzz'
    else:
        return fizzbuzz_input

import random
import prime_test

def find_big_prime(digits):
    rand_min = 10**(digits-1)
    rand_max = 10**(digits)
    guess = random.randint(rand_min, rand_max)

    while not prime_test.is_it_prime(guess):
        print(guess)
        guess = random.randint(rand_min, rand_max)

    return guess
    
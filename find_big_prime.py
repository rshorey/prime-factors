import random
import prime_test

#usage:
#find_big_prime(10)
#finds a prime number with 10 digits.


def find_big_prime(digits):
    #tries random numbers until it finds a prime
    #fast enough to deal with primes up to about 100 digits
    #larger than that, depends how long you're willing to wait
    rand_min = 10**(digits-1)
    rand_max = 10**(digits)
    guess = random.randint(rand_min, rand_max)
    while not prime_test.is_it_prime(guess, 20):
        guess = random.randint(rand_min, rand_max)

    return guess
    
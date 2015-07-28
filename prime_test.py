###implements the Miller-Rabin Primality test
###note that this test is randomized so it could fail
###there is no fast, deterministic primality test
###thus, there is no warranty on prime numbers.
#we are not responsible for death, dismemberment,
#mockery, cryptographic insecurity, divorce,
#writer's block, tendinitis, hardware failure,
#math test failure, or failure of any kind not
#listed here that may result from the use
#of this random algorithm.

import random

def is_it_prime(num, k=5):
    #num is the number we want to test
    #k is the number of Miller-Rabin iterations
    #we're willing to run

    #deal with the easy cases:
    if num < 2:
        return False
    if num in [2, 3, 5]:
        return True
    if num % 2 == 0:
        return False

    s,d = decompose(num-1)

    for i in range(0,k):
        r = random.randint(3, num-2)
        x = (r**d) % num #too slow, need to fix
        if x in [1,num-1]:
            continue
        else:
            for j in range(0,s-1):
                x = (x**2) % num
                if x == 1:
                    return False
                if x == num-1:
                    break
            if x != num-1:
                return False
    return True

def decompose(num):
    s = 0
    while num % 2 == 0:
        s += 1
        num = num/2
    return (s, num)

from find_big_prime import *

with open('list_of_primes2.csv', 'w') as f:
    f.writelines('prime\n')
    for i in range(0,50):
        f.write(str(find_big_prime(37))+'\n')
number = 600851475143
prime_factor = 1
list_of_primes_factors = []

while prime_factor <= number**0.5:
    prime_factor += 1
    if number % prime_factor == 0:
        list_of_primes_factors.append(prime_factor)


print(list_of_primes_factors)



def get_sieve_of_eratosthenes(n):
    if n < 2:pass
    prime = [2];add_prime = prime.append;limit = int(n**0.5);data = [i + 1 for i in range(2, n, 2)]
    while True:
        p = data[0]
        if limit <= p:
            return prime + data
        add_prime(p);data = [e for e in data if e % p != 0]

test_data = 50

data = get_sieve_of_eratosthenes(test_data)
print(data)
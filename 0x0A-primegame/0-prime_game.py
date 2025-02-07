#!/usr/bin/python3

def isWinner(x, nums):
    """Determine the winner of the Prime Game."""
    if not nums or x <= 0:
        return None
    
    def sieve(n):
        """Return a list where index i is True if i is prime."""
        primes = [True] * (n + 1)
        primes[0] = primes[1] = False  # 0 and 1 are not prime
        for i in range(2, int(n ** 0.5) + 1):
            if primes[i]:
                for j in range(i * i, n + 1, i):
                    primes[j] = False
        return primes
    
    max_n = max(nums)
    prime_list = sieve(max_n)

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        primes_left = prime_list[:n + 1]  # Subset up to `n`
        moves = 0
        while True:
            # Find the smallest prime
            try:
                prime = primes_left.index(True)
            except ValueError:
                break  # No more primes left, game over

            # Remove this prime and its multiples
            for i in range(prime, n + 1, prime):
                primes_left[i] = False
            moves += 1

        # Maria plays first, so odd moves = Maria wins
        if moves % 2 == 1:
            maria_wins += 1
        else:
            ben_wins += 1

    return "Maria" if maria_wins > ben_wins else "Ben"

# Test case
print(isWinner(5, [2, 5, 1, 4, 3]))  # Expected: "Maria" or "Ben"


from math import sqrt, floor

# The program is finding the sum of the factors of 10551260.

def factors(n):
    output = []
    for i in range(1, floor(sqrt(n))):
        if n % i == 0:
            output.append(i)
            output.append(int(n/i))
    return output

print(sum(factors(10551260)))
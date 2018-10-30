def is_prime(num):
    factor_count = 0
    if num == 1:
        return False
    for i in range(1, num+1):
        if num % i == 0:
            factor_count += 1
            i += 1
        else:
            i += 1
    if factor_count > 2:
        return False
    else:
        return True


def find_prime(n):
    prime_count = 1
    for current in range(1, 10001):
        if is_prime(current):
            prime_count += 1
            if prime_count == n:
                return current
            else:
                current += 1
        else:
            current += 1


# print(is_prime(8))
print(find_prime(8))

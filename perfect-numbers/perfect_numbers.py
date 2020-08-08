def classify(number):
    if number <= 0:
        raise ValueError("Number must be greater than zero")
    factors = factor(number)
    total = sum(i for i in factors)
    if total == number:
        return "perfect"
    elif total > number:
        return "abundant"
    else:
        return "deficient"


def factor(n):
    return [i for i in range(1, (n // 2) + 1) if not n % i]

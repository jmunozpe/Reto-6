from math import isqrt

class InputTypeError(Exception):
    pass
class NotEnoughDataError(Exception):
    pass


def ensure_iterable_min_len(xs, min_len, name):
    if not hasattr(xs, "__len__"):
        raise InputTypeError(f"'{name}' must be a sequence.")
    if len(xs) < min_len:
        raise NotEnoughDataError(f"'{name}' must have at least {min_len} elements. Got {len(xs)}.")

def ensure_all_ints(xs, name):
    for i, v in enumerate(xs):
        if not isinstance(v, int):
            raise InputTypeError(f"All elements of '{name}' must be int. Index {i} is {type(v).__name__}")

def is_prime(n: int) -> bool:
    if n < 2:
        return False
    if n in (2, 3):
        return True
    if n % 2 == 0:
        return False
    limit = isqrt(n)
    d = 3
    while d <= limit:
        if n % d == 0:
            return False
        d += 2
    return True

def filter_primes(numbers):
    ensure_iterable_min_len(numbers, 1, "numbers")
    ensure_all_ints(numbers, "numbers")
    return [x for x in numbers if is_prime(x)]

if __name__ == "__main__":
    raw = input("Enter integers separated by spaces: ")
    nums = [int(p) for p in raw.split()]
    print("Prime numbers:", filter_primes(nums))


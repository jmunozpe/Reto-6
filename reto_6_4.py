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


def max_consecutive_sum(numbers):
    ensure_iterable_min_len(numbers, 2, "numbers")
    ensure_all_ints(numbers, "numbers")

    best = numbers[0] + numbers[1]
    for i in range(1, len(numbers) - 1):
        s = numbers[i] + numbers[i + 1]
        if s > best:
            best = s
    return best


if __name__ == "__main__":
    raw = input("Enter integers separated by spaces: ")
    nums = [int(p) for p in raw.split()]
    print("Max consecutive sum:", max_consecutive_sum(nums))


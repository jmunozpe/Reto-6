class InputTypeError(Exception):
    pass

def ensure_str(x, name):
    if not isinstance(x, str):
        raise InputTypeError(f"'{name}' must be a string. Got: {type(x).__name__}")

def is_palindrome(word: str) -> bool:
    ensure_str(word, "word")

    s = word.lower()
    i, j = 0, len(s) - 1
    while i < j:
        if s[i] != s[j]:
            return False
        i += 1
        j -= 1
    return True


if __name__ == "__main__":
    w = input("Enter a word: ")
    print("Is palindrome?", "Yes" if is_palindrome(w) else "No")


from collections import Counter

class InputTypeError(Exception):
    pass

def ensure_str(x, name):
    if not isinstance(x, str):
        raise InputTypeError(f"'{name}' must be a string. Got: {type(x).__name__}")

def filter_anagrams(text: str):
    ensure_str(text, "text")
    words = text.split()
    keys = ["".join(sorted(w.lower())) for w in words]
    counts = Counter(keys)
    return [w for w, k in zip(words, keys) if counts[k] >= 2]

if __name__ == "__main__":
    s = input("Enter words separated by spaces: ")
    print("Words with anagrams:", filter_anagrams(s))


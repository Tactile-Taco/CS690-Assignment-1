def is_palindrome_normalized(text):
    normalized = (ch.lower() for ch in text if ch.isascii() and ch.isalnum())
    sequence = ''.join(normalized)
    return sequence == sequence[::-1]

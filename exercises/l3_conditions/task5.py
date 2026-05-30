# Write the body of the function to make the script work without errors
def is_vowel(c: str) -> bool:
    vowels = "aeiou"
    return c.lower() in vowels

print(is_vowel(""))


if __name__ == "__main__":
    # Do not change the below asserts
    assert is_vowel("a") is True
    assert is_vowel("e") is True
    assert is_vowel("z") is False
    assert is_vowel("B") is False
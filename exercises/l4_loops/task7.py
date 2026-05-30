# Use `while` loop to calculate the number
# of digits in a number `n`
def count_digits(n: int) -> int:
    count = 0
    if n == 0:
        return 1
    else:
        while n > 0:
            count += 1
            n = n // 10
    return count

print(count_digits(5551))
# Do not change the below's code
if __name__ == "__main__":
    assert count_digits(0) == 1
    assert count_digits(134) == 3
    assert count_digits(54) == 2
    assert count_digits(55678) == 5

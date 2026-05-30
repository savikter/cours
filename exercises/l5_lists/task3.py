from typing import Any


# Write the body of the function that returns
# the first element from the list `l`
def first(l: list[Any]) -> Any:
    num = l[0]
    return num

print(first([1, 5, 4]))
print(first(["a", "b", "c"]))
print(first([True, False]))

# Do not change the below's code
if __name__ == "__main__":
    assert first([1, 5, 4]) == 1
    assert first(["a", "b", "c"]) == "a"
    assert first([True, False]) == True

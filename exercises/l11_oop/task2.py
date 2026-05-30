# Add a constructor to the class Vehicle
class Vehicle:
    def __init__(self, brand):
        self.name = brand


if __name__ == "__main__":
    # Assign the needed value to the variable `c`
    # to make the script work without errors
    c = Vehicle("Mercedes")

    assert isinstance(c, Vehicle)
    assert c.name == "Mercedes"
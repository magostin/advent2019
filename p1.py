from math import floor


def rocket_fuel(mass):
    return max(floor(mass / 3) - 2, 0)


def rocket_fuel_recursive(mass):
    total_fuel = 0
    fuel = int(mass)
    while fuel := rocket_fuel(fuel):
        total_fuel += fuel

    return total_fuel


if __name__ == "__main__":
    with open("input_p1.txt", "r") as reader:
        print(sum(rocket_fuel(int(mass)) for mass in reader.readlines()))

    with open("input_p1.txt", "r") as reader:
        print(sum(rocket_fuel_recursive(int(mass)) for mass in reader.readlines()))

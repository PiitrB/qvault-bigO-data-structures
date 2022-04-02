import random


def count_kias(cars):
    counter = 0
    for item in cars:
        if "kia" in item:
            counter += 1
    return counter


def list_tail(cars):
    if len(cars) > 0:
        return cars[len(cars)-1]


    # -- TEST SUITE, DON'T TOUCH BELOW THIS LINE --


def main():
    print(count_kias(get_cars(10)))
    print(count_kias(get_cars(100)))
    print(count_kias(get_cars(1000)))
    print(count_kias(get_cars(10000)))
    print(count_kias(get_cars(100000)))


def get_cars(num):
    random.seed(1)
    options = ["tesla", "ford", "chevy", "gm", "kia"]
    cars = []
    for i in range(num):
        optionI = random.randint(0, len(options)-1)
        cars.append(options[optionI])
    return cars


main()

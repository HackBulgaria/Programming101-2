from random import randint

a = 5


def add(a, b):
    return a + b


def sum_dice_rolls(a, b):
    return add(dice_roll(a), dice_roll(b))


def dice_roll(n):
    return randint(1, n)


def plusplus(n):
    global a
    a = a + 1
    n = n + a
    return n + 1


class Person():
    """Person!"""
    def __init__(self, name, unique_id):
        self.name = name
        self.unique_id = unique_id

    def __eq__(self, other):
        return self.unique_id == other.unique_id


def member(x, xs):
    if len(xs) == 0:
        return False

    if x == xs[0]:
        return True

    return member(x, xs[1:])


def io():
    name = input()
    return name


def map2(f, items):
    result = []

    for item in items:
        result.append(f(item))

    return result


def filter2(pred, items):
    result = []

    for item in items:
        if pred(item):
            result.append(item)

    return result


def concat(listOfStrings):
    return reduce(lambda x, y: x + y, listOfStrings, "")


def sum2(numbers):
    return reduce(lambda x, y: x + y, numbers, 0)


def main():
    p1 = Person("Ivo", "1")
    p2 = Person("Rado", "2")
    p3 = Person("Maria", "1")

    print(member(Person("", "5"), [p1, p2, p3]))

if __name__ == '__main__':
    main()

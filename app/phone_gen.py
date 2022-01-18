import random


def make_first():
    first_digit = random.randint(1, 9)
    remaining = random.randint(0, 99)
    return first_digit*100 + remaining


def make_second():
    middle = 0
    while middle == 0:
        middle1 = random.randint(0, 8)
        middle2 = random.randint(0, 8)
        middle3 = random.randint(0, 8)
        middle = 100*middle1 + 10*middle2 + middle3
    return middle


def make_last():
    return ''.join(map(str, random.sample(range(10), 4)))


def make_phone():
    first = make_first()
    second = make_second()
    last = make_last()
    return f'+7 ({first}) {second}-{last[:2]}-{last[2:]}'

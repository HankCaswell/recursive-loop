def count_up (integer):
    if integer == 0:
        print(integer)
        return
    else:
        count_up(integer- 1)
        print(integer)


count_up(10)


def count_down(integer):
    if integer == 0:
        print(integer)
        return
    else:
        print(integer)
        count_down(integer-1)
count_down(10)
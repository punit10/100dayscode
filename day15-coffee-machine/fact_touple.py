import math
list1 = [5, -3, 7, 0, 2]

tuple_list = []


def tuple_of_fact():
    for i in list1:
        if i < 0:
            tup1 = (i, None)
            tuple_list.append(tup1)
        else:
            tup1 = (i, fact(i))
            tuple_list.append(tup1)
    return tuple_list


def fact(n):
    result = 1
    if n == 0 or n == 1:
        result = 1
    else:
        for i in range(1, n+1):
            result *= i
    return result


res = tuple_of_fact()
print(res)

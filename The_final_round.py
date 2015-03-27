from math import log
from datetime import date

def count_words(arr):
    result = {}
    for i in arr:
        result[i] = arr.count(i)
    return result
# print(count_words([1,1,1,"b","b"]))


def unique_words(arr):
    sum = 0
    for i in arr:
        if arr.count(i) == 1:
            sum += 1
        return sum
unique_words([1, 2, 3, 4, 5, 1])


def nan_expand(times):
    if times > 0:
        text = "Not a " * times + "Nan"
    return("\" %s\"" % (text))
print(nan_expand(4))


def iterations_of_nan_expand(expanded):
    if expanded != expanded.strip():
        return False
    list_nan = expanded.split()
    n = 0
    a = 0
    if not list_nan or list_nan[0] != 'Not' or list_nan[len(list_nan) - 1] != "NaN":
        return(False)
    for i in list_nan:
        if i == "a":
            a = a + 1
        elif i == "Not":
            n = n + 1
        elif i != list_nan[len(list_nan) - 1]:
            return(False)
    if a == n:
        return n
    else:
        return False
print(iterations_of_nan_expand("Not a  NaN"))


def sum_of_divisors(n):
    return sum([x for x in range(1, n + 1) if n % x == 0])


def is_prime(n):
    return n + 1 == sum_of_divisors(n)


def func(n):
    div = []
    listnew = []
    if is_prime(n):
        return [(n, 1)]
    for i in range(2, n):
        if n % i == 0:
            div.append(i)
            n = n // i
            while(n % i == 0):
                div.append(i)
                n = n // i
            listnew.append((i, div.count(i)))
    return listnew
print(func(89))


def check_spam(number):
    listnum = []
    for i in range(0, int(log(number, 3)) + 1):
        if number % (3**i) == 0:
            listnum.append(i)
    if len(listnum) == 1:
        return (" \'\'")
    else:
        x = "spam " * max(listnum)
        return ("\'%s\'" % x)


def take_same(items):
    first = items[0]
    n = len(items)
    index = 1
    result = [first]

    while index < n and items[index] == first:
        result.append(items[index])
        index += 1

    return result


def group(items):
    result = []

    while len(items) != 0:
        current_group = take_same(items)
        result.append(current_group)

        items = items[len(current_group):]
    return result
print(group([1, 1, 1, 2, 2, 3]))


def check_eggs(number):
    if number % 5 == 0:
        return "eggs"


def prepare_meal(number):
    if check_eggs(number) == "eggs" and check_spam != " \'\'":
        return (" %s and %s" % (check_spam(number), check_eggs(number)))
    elif check_eggs(number) == "eggs":
        return check_eggs(number)
    else:
        return check_spam(number)


print(prepare_meal(45))


def groupby(func, seq):
    result = {}
    for item in seq:
        key = func(item)
        if key in result:
            result[key].append(item)
        else:
            result[key] = [item]
    return result
print(groupby(lambda x: x % 2, [0, 1, 2, 3, 4, 5, 6, 7]))


def is_an_bn(word):
    count = 0
    for i in word:
        if i != "a" and i != "b":
            return False
        if i != "a":
            break
        else:
            count += 1
    if count == word.count("a") and count == word.count("b") and word:
        return True
    else:
        return False
print(is_an_bn("aaabbb"))


def is_credit_card_valid(number):
    list_of_digits = [int(x) for x in str(number)]
    nwl = []
    i = len(list_of_digits) - 1
    while(i >= 0):
        if i % 2 != 0:
            list_of_digits[i] *= 2
        i -= 1
    num = int(''.join(map(str, list_of_digits)))
    nwl = list(map(int, str(num)))
    if sum(nwl) % 10 == 0 and len(nwl) % 2 != 0:
        return True
    else:
        return False
print(is_credit_card_valid(79927398713))


def goldbach(n):
    result = []
    list_num = [x for x in range(2, n) if is_prime(x)]
    for i in list_num:
        for j in list_num:
            if i + j == n:
                result.append((i, j))
                list_num.remove(i)
                list_num.remove(j)
    return result
print(goldbach(100))


def is_leap_year(year):
    return (year % 4 == 0 and year % 100 != 0) or year % 400 == 0


def friday_years(start, end):
    sum = 0
    for i in range(start, end + 1):
        if is_leap_year(i) and (date(i, 1, 1).weekday() == 5 or date(i, 1, 2).weekday() == 5):
            sum += 1
        elif date(i, 1, 1).weekday() == 5:
            sum += 1
    return sum
print(friday_years(1753, 2000))


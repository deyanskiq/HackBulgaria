from math import sqrt


def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
        return result
print(factorial(5))


def fibonacci(n):
    list_of_numbers = [int(
        ((1 + sqrt(5))**i - (1 - sqrt(5))**i) / (2**i * sqrt(5))) for i in range(1, n + 1)]
    return list_of_numbers
print(fibonacci(10))


def sum_of_digits(n):
    if n < 0:
        return sum(map(int, str(-n)))
    else:
        return sum(map(int, str(n)))
print (sum_of_digits(-4634))


def factorial_digits(number):
    return sum([factorial(int(x)) for x in list(str(number))])
print(factorial_digits(999))


def palindrome(obj):
    return str(obj) == str(obj)[::-1]
print(palindrome(21112))


def number_to_list(n):
    list_of_digits = [int(x) for x in str(n)]
    return list_of_digits
print(number_to_list(556608989))


def list_to_number(digits):
    return "".join(digits)
print(list_to_number(['1', '2', '3']))


def fib_number(n):
    list_of_numbers = [int(
        ((1 + sqrt(5))**i - (1 - sqrt(5))**i) / (2**i * sqrt(5))) for i in range(1, n + 1)]
    return "".join(map(str, list_of_numbers))
print(fib_number(3))


def count_vowels(str):
    count = 0
    vowels = ['a', 'e', 'i', 'o', 'u', 'y']
    for char in list(str):
        if char.lower() in vowels:
            count = count + 1
    return count
print(count_vowels("grrrrgh!"))


def count_consonants(str):
    count = 0
    constants = "bcdfghjklmnpqrstvexz"
    for letter in list(str):
        if letter.lower() in constants:
            count = count + 1
    return count
print(count_consonants)


def char_histogram(string):
    list_str = list(string)
    dict = {}
    for i in list_str:
        dict[i] = list_str.count(i)
    return dict
print(char_histogram("aaab!B"))


def p_score(n):
    if str(n) == str(n)[::-1]:
        return(1)
    else:
        return 1 + p_score(n + int(str(n)[::-1]))
print(p_score(198))


def is_increasing(seq):
    return seq == sorted(seq)
print(is_increasing([1, 3, 4, 5, 1]))


def is_decreasing(seq):
    return seq == sorted(seq)[::-1]
print(is_decreasing([5, 249, 3, 1]))


def palindrome(obj):
    return str(obj) == str(obj)[::-1]


def odd_ones(binary):
    return (bin(binary).count("1")) % 2 != 0


def next_hack(n):
    i = n + 1
    while(n):
        if n == 0:
            return 1
        elif palindrome(bin(i)[2:]) and odd_ones(i):
            return i
            break
        else:
            i += 1
print(next_hack(0))

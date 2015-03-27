def sum_of_divisors(n):
    sum_of_divisors = 0
    for i in range(1, n + 1):
        if n % i == 0:
            sum_of_divisors += i
    return sum_of_divisors
print(sum_of_divisors(1))


def is_prime(n):
    if n < 0:
        n = -n
    if n == 1:
        return False
    for i in range(2, n // 2 + 1):
        if n % i == 0:
            bool_prime = False
            break
        else:
            bool_prime = True
    return bool_prime
print (is_prime(10))


def prime_number_of_divisors(n):
    sum = 0
    bool_p = True
# Finds the number of divisors
    for i in range(1, n + 1):
        if n % i == 0:
            sum = sum + 1
# Checks if this number is odd
    for i in range(2, sum):
        if sum % i == 0:
            bool_p = False
            break
        else:
            bool_p = True
    return bool_p
print(prime_number_of_divisors(9))


def contains_digit(number, digit):
    return str(digit) in str(number)
print(contains_digit(2, 2))


def contains_digits(number, digits):
    bool_is = True
    for i in digits:
        if str(i) in str(number):
            bool_is = True
        else:
            bool_is = False
            break
    return bool_is
print(contains_digits(1234, [1, 2]))


def is_balanced(n):
    digits = [int(i) for i in str(n)]
    size = len(list(digits))
    if size % 2 != 0:
        return sum(digits[0:size // 2]) == sum(digits[size // 2 + 1:size])
    else:
        return sum(digits[0:size // 2]) == sum(digits[size // 2:size])
print(is_balanced(1238033))


def count_substrings(haystack, needle):
    return haystack.count(needle, 0, len(haystack))
print(count_substrings("OHO BOho hoho hou", "ho"))


def zero_insert(n):
    list_digits = [int(i) for i in str(n)]
    size = len(list_digits)
    i = 0
    while(i < size - 1):
        if list_digits[i] == list_digits[i + 1] or (list_digits[i] + list_digits[i + 1]) % 10 == 0:
            list_digits.insert(i + 1, 0)
            size = size + 1
        i = i + 1
    return "".join(map(str, list_digits))
print(zero_insert(1))


def sum_matrix(m):
    sum = 0
    for row in m:
        for elm in row:
            sum = sum + elm
    return sum
print(sum_matrix([[7, 9, 6], [5, 3, 2], [7, 2, 1]]))


from sum_matrix import sum_matrix
import copy


def handle_neighbour(m, x, y, bomb):
    if x >= 0 and x < len(m[0]) and y >= 0 and y < len(m):
        if m[y][x] >= bomb:
            m[y][x] -= bomb
        else:
            m[y][x] = 0


def blow_bomb(m, x, y):
    bomb = m[y][x]
    for x_pos in range(x - 1, x + 2):
        for y_pos in range(y - 1, y + 2):
            if not (x_pos == x and y_pos == y):
                handle_neighbour(m, (x_pos, y_pos), bomb)
    return sum_matrix(m)


def matrix_bombing_plan(m):
    result = {}
    for y in range(0, len(m)):
        for x in range(0, len(m[y])):
            matrix = copy.deepcopy(m)
            result[(y, x)] = blow_bomb(matrix, (x, y))
    return result


def main():
    m = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print(matrix_bombing_plan(m))
    m2 = [[4, 8, 3], [5, 2, 7], [3, 9, 6]]
    print(matrix_bombing_plan(m2))

if __name__ == '__main__':
    main()

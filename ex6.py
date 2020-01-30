def sum_of_square(num):
    sum = 0
    for i in range(1, num):
        i = i**2
        sum += i
    return sum


def square_of_sum(num):
    result = 0
    for i in range(1, num):
        result += i
    return result**2


answer = square_of_sum(101) - sum_of_square(101)
print(answer)
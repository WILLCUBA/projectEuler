def is_divisible1to20(numb):
    for i in range(1, 21):
        if number % i != 0:
            return False
    return True

number = 1

while True:
    if is_divisible1to20(number):
        break
    number += 1
print(number)

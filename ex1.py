nums = range(1, 1000)
sumOfMultiples = 0

for number in nums:
    if number % 3 == 0 or number % 5 == 0:
        sumOfMultiples += number

print(sumOfMultiples)
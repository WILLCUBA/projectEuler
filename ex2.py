fib = [1, 2]
while fib[-1] <= 4000000:
    fib.append(
        fib[-2] + fib[-1]
    )
sum = 0
for terms in fib:
    if terms % 2 == 0:
        sum += terms
print(sum)
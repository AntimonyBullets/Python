numbers = [11, 4, 1, 12, 7, 12]
largest = numbers[0]
for n in numbers:
    if n > largest:
        largest = n
print(largest)
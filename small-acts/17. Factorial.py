num = int(input("Enter a positive integer: "))
factorial = 1
i = 1
while i <= num:
    factorial *= i
    i += 1
print(num,"! =", factorial)


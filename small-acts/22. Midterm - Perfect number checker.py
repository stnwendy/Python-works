while True:
    num=eval(input("Enter a positive integer (or 0 to exit): "))
    if num==0:
        print("Goodbye!")
        break
    elif num != 0:
        divisors_sum=0
        for i in range (1,num):
            if num%i==0:
                divisors_sum += i
        if divisors_sum == num:
            print(num, "is a perfect number.")
        else:
            print(num, "is not a perfect number.")


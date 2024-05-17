n=eval(input("How many Fibonacci numbers do you want in the sequence? "))
n1,n2 = 1,1
nf = n1+n2

print(n1)
print(n2)

for i in range (n-2):
    print(nf)

    n1,n2 = n2,nf
    nf = n1+n2

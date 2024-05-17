n=eval(input("Until what number should the sequence be? "))
n1=1
n2=1
nf=n1+n2

print(n1)
print(n2)

while nf<n:
    print(nf)

    n1=n2
    n2=nf
    nf=n1+n2
    
    if nf >= n:
        break
        

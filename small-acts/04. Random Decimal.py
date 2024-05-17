import random 

#define
def print_rn_ave():
    rn1=round((random.uniform(1.00,100.00)),2)
    rn2=round((random.uniform(1.00,100.00)),2)
    rn3=round((random.uniform(1.00,100.00)),2)
    rn4=round((random.uniform(1.00,100.00)),2)
    rn5=round((random.uniform(1.00,100.00)),2)
    rn_ave=(rn1+rn2+rn3+rn4+rn5)/5.00
    print(rn1,rn2,rn3,rn4,rn5, sep=",")
    print("The average of the five random numbers is ", round(rn_ave,2), sep="")

#call
print_rn_ave()


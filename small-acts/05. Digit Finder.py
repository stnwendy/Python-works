#input
pwr=eval(input("Kindly input your desired power in 2^n: "))
dgt=eval(input("What is the maximum number of last digits do you want to find? "))
  
#define function  
def print_dgt_fndr():
    val = (pow(2,pwr))
    dgt_fndrA= (pow(2,pwr)) % 10
    dgt_fndrB= (pow(2,pwr)) % 100
    dgt_fndrC= (pow(2,pwr)) % (pow(10,dgt))
    
    print("A.)The last digit when 2 is raised to ", pwr, " is ", dgt_fndrA, sep="")
    print("B.)The last two digits when 2 is raised to ", pwr, " is ", dgt_fndrB, sep="")
    print("C.)The last ", dgt," digits when 2 is raised to ", pwr, " is ", dgt_fndrC, sep="")
    print("The value of 2^",pwr,"is ",val)
    
#call
print_dgt_fndr()

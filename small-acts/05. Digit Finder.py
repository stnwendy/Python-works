#input
pwr=eval(input("Kindly input your desired power: "))
dgt=eval(input("How many digits do you want to find in letter C? "))
  
#define function  
def print_dgt_fndr():
    dgt_fndrA= (pow(2,pwr)) % 10
    dgt_fndrB= (pow(2,pwr)) % 100
    dgt_fndrC= (pow(2,pwr)) % (pow(10,dgt))
    print("A.)The last digit when 2 is raised to ", pwr, " is ", dgt_fndrA, sep="")
    print("B.)The last two digits when 2 is raised to ", pwr, " is ", dgt_fndrB, sep="")
    print("C.)The last ", dgt," digits when 2 is raised to ", pwr, " is ", dgt_fndrC, sep="")
    
#call
print_dgt_fndr()
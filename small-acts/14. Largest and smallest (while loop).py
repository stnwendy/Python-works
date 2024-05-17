largest = 0
smallest = 0
num=""

while num != 0:
    num=eval(input("Type the integer [0 to stop input]: "))
    if num > largest:
        largest=num
        smallest = num
    
    elif num < largest and num !=0:
        smallest = num
        
    
    elif num==0:
       smallest=smallest
       
    continue
        
else: 
    print("The difference of the largest integer,", largest, ", and the smallest integer,", smallest, ",  is", largest - smallest)
    
    

list=[]
add=""

while add != 0:
    add=eval(input("Type the integer [type 0 to stop]: "))
    if add != 0:
        list.append(add)
    elif add == 0:
        continue
        
else: 
    count=len(list)
    sumAll=sum(list, start=0)
    mean=(sum(list, start=0)/len(list))
    
    print("count:", count)
    print("sum:", sumAll)
    print("mean:", mean)
    print("list: ", list)
    


list=[]
num=""

while num!=0:
    num=eval(input("Type the integer [type 0 to stop]: "))
    if num!=0:
        list.append(num)        
    #elif num==0:
    #    pass
    #continue

else:
    sorted(list, reverse=True)
    #list.sort(reverse=True)
    #print("The difference between the largest number", list[-1], end=" ")
    #print("and the smallest number", list[0], "is", (list[-1]-list[0]))
    #print("The difference between the largest number", max(list), end=" ")
    #print("and the smallest number", min(list), "is", (max(list)-min(list)))
    print(list)
    
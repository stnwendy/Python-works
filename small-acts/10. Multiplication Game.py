import random

scr=0
qs=1
n=1
for n in range (10):
    rn1=random.randint(1,10)
    rn2=random.randint(1,10)
    
    qsAns=eval(input("Question " + str(qs) + ": " + str(rn1) + " x " + str(rn2) + " = "))
    #qsAns=eval(input(f"Question {qs} : {rn1} x {rn2} = "))
    if qsAns == rn1 * rn2:
        print("Right!")
        scr=scr+1
        qs=qs+1
    else:   
        print("Wrong! The answer is ", rn1 * rn2, ".", sep="")
        qs=qs+1
 
        

        
        
print("\nYou've got ", scr, "/10", sep="")
        
            
    



 
grd=eval(input("Kindly input your grades: "))
loop=True

if grd>=90 and grd<=100:
    print("Your grade is A. Outstanding performance!")
elif 80<=grd<90:
    print("Your grade is B. Very good performance!")
elif grd>=70 and grd<80:
    print("Your grade is C. Good performance!")
elif grd>=60 and grd<70:
    print("Your grade is D. Fair performance!")
elif grd>=0 and grd<60:
    print("Your grade is E. Poor performance!")
else:
    print("Invalid. Please type again.")
    loop()


    

#input
x_1=eval(input("Input your x_1: "))
x_2=eval(input("Input your x_2: "))
y_1=eval(input("Input your y_1: "))
y_2=eval(input("Input your y_2: "))
    
def print_slope():
    slp= (y_2-y_1)/(x_2-x_1)
    print("The slope of the line is ", round(slp, 2),".", sep="")
          
#call
print_slope()
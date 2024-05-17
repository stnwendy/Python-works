from random import randint

num=randint(1,20)

print("This program is a guessing game! There are only 3 chances to play this game.")
print("The number is", num)

for i in range(3):      
    guess=eval(input("Type your guess number between 1 and 20: "))
    if guess == num:
        print("\nCongratulations, You got it! ")
        break 
    else:  
        i=i+1
        if i == 1:
            print("Oops wrong!", end="")
            if guess < num:
                print("Too low! Please try again.")
            elif guess > num:
                print("Too high! Please try again.")
            else: 
                continue
        elif i == 2:
            print("Oops wrong!", end="")
            if guess < num:
                print("Too low! Please try again.")
            elif guess > num:
                print("Too high! Please try again.")
            else: 
                continue
        else:
            print("\nGame over! ", end="")
            print("The number is", num)
    







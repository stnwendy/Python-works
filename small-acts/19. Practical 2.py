print("\t\tIrrashaimase!! Welcome to Emiru's Noodle Shop!")
print("\t\t\t\t\t\t\tMenu")
print("\t\tOrder Code", "\t\tNoodle Dish", "\t\tPrice" )
print("\t\t\t[A1]", "\t\tClassic Ramen", "\t\t150.00" )
print("\t\t\t[B1]", "\t\tCreamy Udon", "\t\t120.00" )
print("\t\t\t[C1]", "\t\tSoba Noodles", "\t\t180.00" )

total_bill=0
ord_nmb=eval(input("How many orders are you going to make? "))


for i in range(ord_nmb):
    ord_code=input("Please choose the code of your noodle choice [A1, B1, C1]: ")
    #if ord_code != "A1" or "B1" or "C1" or "a1" or "b1" or "c1":
        #print("Invalid Code. Try again.")
        #ord_code=input("Please choose the code of your noodle choice [A1, B1, C1]: ")
    #else:
        #continue      
                
    ord_quan=eval(input("What is the quantity of your chosen order?"))
    price=ord_code*ord_quan
    if ord_code=="A1" or ord_code=="a1":
        price1=150*ord_quan
        print(ord_quan,"Classic Ramen Order Price: PHP ", float(price1))
        total_bill=total_bill+price1
    elif ord_code=="B1" or ord_code=="b1":
        price2=120*ord_quan
        print(ord_quan,"Creamy Udon Order Price: PHP ", float(price2))
        total_bill=total_bill+price2
    elif ord_code=="C1" or ord_code=="c1":
        price3=180*ord_quan
        print(ord_quan,"Soba Noodles Order Price: PHP ", float(price3))
        total_bill=total_bill+price3
    else:
        print("Invalid Code")
        exit()
    
        
        
        
print("Your total bill is ", total_bill)
paid=eval(input("How much will you pay?"))
print("You have paid ", float(paid))

if paid >= total_bill:
    print("Your change is PHP ", float( paid-total_bill), ".", sep="")
else:
    print("Insufficient amount. The bill is PHP ",float(total_bill), ". You still need PHP ", float(abs(paid-total_bill)), ".", sep="")
    paid=eval(input("How much will you pay?"))
    print("You have paid ", float(paid))    
    
#while True:
    #if paid >= total_bill:
        #print("Your change is PHP ", float( paid-total_bill), ".", sep="")
        #break
    #else:
        #print("Insufficient amount. The bill is PHP ",float(total_bill), ". You still need PHP ", float(abs(paid-total_bill)), ".", sep="")
        #paid=eval(input("How much will you pay?"))
        #print("You have paid ", float(paid))
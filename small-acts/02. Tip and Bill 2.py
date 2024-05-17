#input
intl_price=eval(input("How much did the meal cost? "))
prcnt_tip=eval(input("Please put how much percentage tip do you want to give? "))
    
def print_final_msg():
    tip_amt = intl_price*(prcnt_tip/100)
    ttl_bill = intl_price + tip_amt
    print("Your tip amount is PHP", tip_amt,".")
    print("Your total bill to pay is PHP", ttl_bill, ". Thank you.")
          
#call
print_final_msg()
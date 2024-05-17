intl_price=eval(input("How much did your meal cost?  "))
prcnt_tp=eval(input("Kindly input your tip in percentage. Thank you.  "))
tip= prcnt_tp/100
tip_amt= intl_price*tip
ttl_bill= intl_price+tip_amt

print("Your tip amount is PHP", tip_amt,". Your total bill to pay is PHP", ttl_bill, ". Thank you." )

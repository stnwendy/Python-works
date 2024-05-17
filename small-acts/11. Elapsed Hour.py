orgHour=eval(input("Enter hour: "))
meridian= eval(input("am (1) or pm (2)? ")) 
while meridian > 2 or meridian < 1:
    print("You entered the wrong key. Try again")
    meridian= eval(input("am (1) or pm (2)? ")) 
    continue
leapHour= eval(input("How many hours ahead? "))


def newHour():
    if fnTime==12: 
        print("New Hour: 12nn", sep="") 
    elif fnTime==24 or fnTime==0: 
        print("New Hour: 12mn", sep="") 
    elif 12<fnTime<24: 
        print("New Hour: ",fnTime-12,"pm", sep="") 
    else: 
        print("New Hour: ",fnTime,"am", sep="")
    

if meridian == 1:
    fnTime=orgHour+leapHour
    if fnTime <=24:
        newHour()
    else:
        fnTime= fnTime-(24*(fnTime//24))
        newHour()
         
elif meridian == 2: 
    fnTime=orgHour+leapHour+12
    if fnTime <=24:
        newHour()
    else:
        fnTime= fnTime-(24*(fnTime//24))
        newHour()
                    
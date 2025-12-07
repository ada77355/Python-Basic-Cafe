MENU ={
    'COFFEE':40,
    'COLD COFFEE':60,
    'CHAI':20,
    'PAKODE':30,
    }
print("WELCOME TO OUR CAFE\nWHAT WOULD YOU LIKE TO HAVE\n")
print("COFFEE:40\nCOLD COFFEE:60\nCHAI:20\nPAKODE:30")

order_total =0

item_1=(input("WHAT WOULD YOU LIKE TO HAVE?"))
if item_1 in MENU:
    order_total +=MENU[item_1]
    print("YOUR ITEM IS ADDED ")
else:
    print("order somthing that we can serve you")
    

    
other_order=(input("WOULD YOU LIKE TO HAVE ANYTHING ELSE YES/NO"))
if other_order=="YES":
    item_2=(input("WHAT WOULD YOU LIKE TO HAVE",))
    if item_2 in MENU:
        print("YOUR ITEM IS ADDED")


    
    order_total+=MENU[item_2]
    
    print("TOTAL VALUE",order_total)
    
else:
    print("THANK YOU,YOUR TOTALIS ",order_total)


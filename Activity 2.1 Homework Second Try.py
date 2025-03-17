#Week 5 Homework - Embedded Applications
#Author: Ryan Page
#Date: 15/03/2025
#Activity 2.1
#1.	Write a program which simulates a basic vending machine
#provides change based on the users monetary input and item price. 
#Your change total must be represented in dollars and cents. 

#In this homework I learned about the EAFP style -from the python codex
#https://docs.python.org/3/glossary.html#term-EAFP

#legend
    #variables -
        #items - items for sale in the vending machine
        #name - placeholder for name of item selected from array
        #price - placeholder for the price of item selected from the array
        #number - address number of the item in the array to be selected
        #selection - the item to be selected from the array
        #item_name - the name to be printed out when displaying the item and the cost when selected
        #item_price - the price to be printed out when displaying the item and the cost when selected
        #payment - the money entered by the user as an input
        #change - the amount of money returned when subtracting the cost of the item against the money entered
def upsell():
    while True:
        try:
            goforthesale = int(input("Enter 5 to make another purchase or 0 to exit: "))
            if goforthesale == 5:
                vmachine()
            elif goforthesale == 0:
                break
                   
        except ValueError:
            print("Please enter 0 or 5...")
            
print("Activity 2.1 Vending Machine, what would you like to purchase today?\n")
def vmachine():
    #list of items available for sale in the vending machine
    items = {
        1: {"name": "Chocolate Bar", "price": 2.0},
        2: {"name": "Museli Bar", "price": 1.50},
        3: {"name": "Bundaburg Ginger Beer", "price": 3.80},
        4: {"name": "Sanitary Items", "price": 2.50},
        5: {"name": "Perfume", "price": 5.00},
        6: {"name": "Cologne", "price": 4.50},
    }
    
    print("Here are the available items")
  
    #display the items in the vending machine
    for number, item in items.items():
        print(f"{number}. {item['name']}: ${item['price']:.2f}")
   
   #collect a number from the user of the item they want
    try:
       selection = int(input("Enter the number of the item you'd like: "))
       
    except ValueError:
       #I learned about this perment exception ValueError. It is raised when an operation or function  
       #receives an argument that has the right type but an inappropriate value.
       #I am going to use this alot going forwards until it bites me.
       print("Error.\nPlease enter a valid number.")
       return
       
    if selection not in items:
       print("If you do that again, you'll get mouldy cabbages. Try again.\n")
       vmachine()
             
    item_name = items[selection]["name"]
    item_price = items[selection]["price"]
    
    #collect the moola, I learned to use """ to carry across lines, it's not very pretty though.
    try:
        payment = float(input(f"""This machine takes cash only.
{item_name} is ${item_price:.2f}
Enter your cash amount: $"""))
        
    except ValueError:
       print("Error.\n\
       Please enter a valid number.")
       return
        
    if payment < item_price:
        print(f"Not enough moola.")
        return
#Calculate the change to be received 
    change = payment - item_price
    dollars = int(change)
    cents = round((change - dollars) * 100)
    
    print(f"Your change is ${dollars}.{cents}.")
    print("Thank you for your purchase.")
    upsell()
#Go for the upsell with a while True loop

                     
vmachine()
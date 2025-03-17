#Week 5 Homework - Embedded Applications
#Author: Ryan Page
#Date: 12/03/2025

#2.	Write a program which will calculate the cost of petrol 
#based on a road trip in kilometers. 



while True:
    FuelPrice = input("What is the price of fuel per litre? ")
    RoadTripKm = input("How long is the trip? ")
    CarEfficiency = input("How many liters per 100km in your car? ")
    
    try:
        illegalchar = "$kmkilometersdollars"
        for char in illegalchar: #easy way to ensure string gets converted to float
            FuelPrice = FuelPrice.replace(char, "")
            RoadTripKm = RoadTripKm.replace(char, "")
            CarEfficiency = CarEfficiency.replace(char, "")
    
        ce = float(CarEfficiency)
        fp = float(FuelPrice)
        rtkm = float(RoadTripKm)
        fa = rtkm / ce #fuel amount used = distance / car efficiency
        fckm = (fa * fp) / ce #working out fuel cost per km. = (fuel amount * fuel price) / car efficiency
        cot = fa * fp #working out cost of petrol for trip = fuel amount * fuel price

        print("Your cost per km is: $",fckm,"AUD")
        print("Total cost of the petrol for your", RoadTripKm,"km" " trip is: $",cot,"AUD")
        
        break
    except IncorrectEntry:
        print("Incorrect entry. Try again.")
    except Exception as e:
        print(f"An error has occurred: {e}")
        break

    
  
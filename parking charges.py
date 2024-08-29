def calculate_parking_charges(vehicle_type, hours):

    rates = {
        'b': 20,  
        't': 20,  
        'c': 10,  
        'm': 5,   
        'y': 20,
    }

    
    vehicle_type = vehicle_type.lower()
    
    if vehicle_type in rates:
        charge = rates[vehicle_type] * hours
        return charge
    else:
        return "Invalid vehicle type!"


vehicle_type = input("Enter the type of vehicle (b for bus/truck, c for car, m for bike/cycle): ")
hours = int(input("Enter the number of hours parked: "))

charge = calculate_parking_charges(vehicle_type, hours)
if isinstance(charge, int):
    print(f"The parking charge for {hours} hour(s) is Rs.{charge}")
else:
    print(charge)

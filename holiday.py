# Get user input fo holiday destination.
city_flight = input (
                     "Please enter the city you will be fltying to "
                     "(Cape Town, East London, Durban or Polokwane) :"
)
num_nights =float(input(
                    "Please enter the number of nights you will be"
                    "statying at the hotel : "             
))
rental_days = int(input("Please enter the number of days you will be renting a car : "))

# Fuction to calculate hotel costs.
def hotel_cost(num_nights) :
    price_per_night = 560.70
    return num_nights * price_per_night

# Fuction to calculate plane costs based on the destination.
def plane_cost(city_flight):
    if city_flight.lower() == "Cape Town":
        return 3000
    elif city_flight.lower() == "East London":
        return 2500
    elif city_flight.lower() == "Durban":
        return 1500
    elif city_flight.lower() == "Polokwane":
        return 1200
    else:
        return 1800
    
# Fuction to calculate car rental based on number of days.
def car_rental(rental_days):
    price_per_day = 1050
    return rental_days * price_per_day

# Fuction to calculate total holiday cost.
def holiday_cost(num_nights, city_flight, rental_days):
    total_hotel = hotel_cost(num_nights) 
    total_flight = plane_cost(city_flight) 
    total_car = car_rental(rental_days) 
    total = total_hotel + total_flight + total_car
    return total

# Calculate cost
total_hotel_cost = hotel_cost(num_nights)
total_plane_cost = plane_cost(city_flight)
total_car_cost = car_rental(rental_days)
total_cost = holiday_cost(num_nights, city_flight, rental_days)

# Print results base on the user input.
print("\n HOLIDAY DETAILS:")
print(f"Destination: {city_flight}")
print(f"Hotel stay: {num_nights} nights at R560 per night = R{total_hotel_cost:.2f}")
print(f"Flight cost: R{total_plane_cost}")
print(f"Car rental: {rental_days} days at R1050 per day = R{total_car_cost}")
print(f"Total holiday cost: R{total_cost:.2f}")
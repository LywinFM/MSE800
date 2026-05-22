import random

#Generate a 6-digit booking ID 
booking_id = str(random.randint(100000, 999999))

database = {}

# Save Booking details
database[booking_id] = {
	"service": "YBS Rental Car",
	"status": "Confirmed"
}


print("Booking confirmed")
print("Your Booking ID: " + booking_id)
print("Thank you for choosing YBS Rental car services")

print("\n--- Database Record ---")
print(database)

# End Transaction Car_Rental_System
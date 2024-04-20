from prac_09.silver_service_taxi import SilverServiceTaxi

# Create a SilverServiceTaxi object with name "Hummer", 200 units of fuel and fanciness of 4
hummer_taxi = SilverServiceTaxi("Hummer", 200, 4)

# Print hummer taxi's details
print(f"Hummer taxi's details {hummer_taxi}")

# With fanciness of 2
hummer_taxi = SilverServiceTaxi("Hummer", 200, 2)
# Drive the hummer taxi for a distance of 18 km
hummer_taxi.drive(18)

print(f"Current fare: ${hummer_taxi.get_fare():.2f}")
# create an array of vehicles, each with a type, model and a speed
vehicles = [
    {"type": "car", "model": "Toyota Camry", "speed": 120},
    {"type": "truck", "model": "Ford F-150", "speed": 100},
    {"type": "motorcycle", "model": "Harley Davidson", "speed": 150}
]

# loop through the array and print out the type and model of each vehicle

for vehicle in vehicles:
    print(f"Type: {vehicle['type']}, Model: {vehicle['model']}, Speed: {vehicle['speed']} km/h")

# create a function that takes in a vehicle type and returns the average speed of that type of vehicle
def average_speed(vehicle_type):
    total_speed = 0
    count = 0
    for vehicle in vehicles:
        if vehicle["type"] == vehicle_type:
            total_speed += vehicle["speed"]
            count += 1
    if count > 0:
        return total_speed / count
    else:
        return 0
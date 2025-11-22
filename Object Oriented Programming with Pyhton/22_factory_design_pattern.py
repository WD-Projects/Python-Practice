"""
📌 Purpose

1. Used to create objects without exposing the creation logic to the client.
2. The factory decides which class to create based on input.

📌 When to Use Factory

Use it when:
1. A class has multiple subclasses, and the decision of which object to create depends on user input/conditions.
2. You want to hide object creation complexity.

Examples:
1. Shape generator → circle, square, triangle
2. Notification system → email, SMS, push notification
3. Data parser → JSON, XML, CSV

⚙️ Workflow

1. Client makes a request (e.g., "circle").
2. Factory receives the request.
3. Factory returns an object of the correct class.
"""

class Car:
    def drive(self):
        return "Car is driven"
    
class Bike:
    def drive(self):
        return "Bike is driven"

class Vehicle_factory:
    @staticmethod
    def get_vehicle(type):
        if type.lower() == "car":
            return Car()
        elif type.lower() == "bike":
            return Bike()
        else:
            raise ValueError("Unknown vehicle")
        
vehicle = Vehicle_factory.get_vehicle("Bike")
print(vehicle.drive())
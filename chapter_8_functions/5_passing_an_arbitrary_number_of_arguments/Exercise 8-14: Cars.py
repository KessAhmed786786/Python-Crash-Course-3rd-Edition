# Chapter 8 - Functions
# Kess Ahmed, 30th July 2025
# Write a function that stores information about a car in a dictionary, the function should always recieve a manufacturer and a model name. Then arbitrary number of keyword arguments. Call and print to prove working


# Create function
def make_car(manufacturer, model_name, **car_info):
    car_info["manufacturer"] = manufacturer
    car_info["model_name"] = model_name
    return car_info


# Call function
car = make_car("subaru", "outback", color="blue", tow_package=True, wheels=4)

# Print and prove
for key, value in car.items():
    print(f"- {key}: {value}")

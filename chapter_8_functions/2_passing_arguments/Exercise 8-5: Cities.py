# Chapter 8 - Functions
# Kess Ahmed, 29th July 2025
# Write function called describe_city, accept name and country, print simple sentence, give parameter for country a default value, call 3x with one changing default value.

# Create function
def describe_city(city, country="United States of America"):
    """Prints a simple message related with country and city"""
    print(f"{city.title()} is in {country.title()}")

# Call function
describe_city('New York')

# Call function
describe_city(city='Houston')

# Call function
describe_city(city='london', country='united kingdom')

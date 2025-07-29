# Chapter 8 - Functions
# Kess Ahmed, 29th July 2025
# Write a function called city_country() that takes name of city and country, should return a string formatted like "Santiago, Chile", call three pairs

# Create a function
def city_country(city="", country=""):
    """Returns formatted string with city and country"""
    city_country_pair = f'"{city}, {country}"'
    return city_country_pair.title()

# Call function
formatted_city_country = city_country('santiago','chile')
print(formatted_city_country)

# Call function
print(city_country())

# Call function
print(city_country('tokyo','japan'))

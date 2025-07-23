# Chapter 6 - Dictionaries
# Kess Ahmed, 23nd July 2025
# Create a nested dictionary called cities, use the name of three cities as keys. and the values as a dictionary of country, population, fact

# Create nested dictionary structure
cities = {
    'paris': {
        'country': 'france',
        'population': 10_000_000,
        'fact': 'They eat baguettes',
    },
    'cardiff': {
        'country': 'united kingdom',
        'population': 1_000_000,
        'fact': 'They eat sandwiches',
    },
    'mumbai': {
        'country': 'india',
        'population': 100_000_000,
        'fact': 'They eat rotis',
    },
}

for city, city_info in cities.items():
    print(f"City: {city}")
    print(f"\tCountry: {city_info['country'].title()}")
    print(f"\tPopulation: {city_info['population']}")
    print(f"\tFact: {city_info['fact']}")

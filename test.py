cities = {
    'paris': {
        'country': 'france',
        'population': 10_000_000,
        'size': 'Big',
    },
    'cardiff': {
        'country': 'united kingdom',
        'population': 1_000_000,
        'size': 'Small',
    },
    'mumbai': {
        'country': 'india',
        'population': 100_000_000,
        'size': 'Big',
    },
}

for city, city_dictionary in cities.items():
	print(f"--- {city.title()} ---")
	for key, value in city_dictionary.items():
		print(f"\t {key}: {value}")

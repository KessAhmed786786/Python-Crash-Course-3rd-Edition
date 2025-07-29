# Chapter 8 - Functions
# Kess Ahmed, 29th July 2025
# 

def get_format_name(first_name, last_name):
    """Return a full name, neatly formatted"""
    full_name = f"{first_name} {last_name}"
    return full_name.title()

print(get_format_name('jimi','hendrix'))

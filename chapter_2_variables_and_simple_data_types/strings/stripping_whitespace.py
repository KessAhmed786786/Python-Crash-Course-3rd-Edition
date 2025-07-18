# Chapter 2 - Variables and Simple Data Types
# stripping_whitespace.py
# Clean strings both sides, left side and right side
# Kess Ahmed, 12th July 2025

# Declaring test string
favourite_language = "   python programming   "
marker = "!"

# Right side
print(favourite_language.rstrip())

# Left side
print(favourite_language.lstrip())

# Both sides
print(favourite_language.strip())

# Seeing Left side better
print(marker, favourite_language.lstrip(), marker)
print(marker, favourite_language.strip(), marker)

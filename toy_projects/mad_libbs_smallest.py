# 1. Define Your Story Template with placeholders
story_template = "The {adjective} {noun} ran quickly."

# 2. Get User Input for each word
user_adjective = input("Enter an adjective: ")
user_noun = input("Enter a noun: ")

# 3. Substitute User Words into the Story using f-strings
final_story = f"The {user_adjective} {user_noun} ran quickly."

# 4. Display the Completed Story
print("\n--- Your Mad Lib ---")
print(final_story)
print("--------------------")

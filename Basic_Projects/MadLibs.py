def get_input(word_type:str):
    user_input = input(f"Please enter a {word_type}: ")
    return user_input

noun1 = get_input("noun")
verb1 = get_input("verb")
noun2 = get_input("noun")
verb2 = get_input("verb")

story = f'''
Once upon a time, there was a {noun1} who loved to {verb1} all day long.
One day, it met another {noun2} who also loved to {verb2}.
They became the best of friends and lived happily ever after.
The end.
'''

print(story)
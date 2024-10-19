'''
This module ensures that the data allowed into the system is valid.
Techniques such as removing leading and trailing whitespaces along with
checking if a string is all space have been employes to ascertain real
data is collected.
If data entered is incorrect, the system reprompts the user to input data
until it is valid.
'''

# Name validation, returns valid name
def validate_name(name):
    name = name.title().strip()
    
    while len(name) <= 1 or name.isspace():
        print("Name must not have only whitespace or less than 2 letters")
        name = input("Re-enter a valid name: ")

    return name


# Validate rating
def validate_rating(rating, name):
    try:
        rating = int(rating)
        if rating < 0 or rating > 5:
            rating = __rating_internal(rating, name)
    except ValueError:
        rating = __rating_internal(rating, name)
    return rating


# Pivate method to help in rating validation
def __rating_internal(rating, name):
    try:
        print(f"{rating} is not within the specified range of 1 - 5")
        rating = int(input(f"Re-enter {name}'s valid rating (1 - 5): "))
        if rating < 0 or rating > 5:
            rating = __rating_internal(rating, name)
    except ValueError:
        rating = __rating_internal(rating, name)
    return rating


# Validating feedback
def validate_feedback(feedback, name):
    feedback = feedback.strip()
    
    while len(feedback) <= 1 or name.isspace():
        print("Feedback must not have only whitespace or less than 2 letters")
        feedback = input(f"Re-enter {name}'s feedback: ")

    return feedback
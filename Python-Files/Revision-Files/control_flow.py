# What is control flow

# Conditional statements and loops
# IF, ELSE, ELIF, FOR LOOP, WHILE LOOP

weather = "snowy"
conditional_weather = "rainy"

# Do a comparison to see if the value "sunny" is inside the weather variable
# This is a conditional block of code, if "sunny" then display "Lets go to.."
# If it is not "sunny" E.G. any other type of weather then "Lets play games.."
if weather == "sunny" and conditional_weather == "rainy":  # Both conditions MUST be TRUE
    print(" Lets go to the beach")
else:
    print(" Lets play games indoors...")

# This time we use the OR operator
if weather == "sunny" or conditional_weather == "rainy":  # Either conditions can be TRUE
    print(" Lets go to the beach")
else:
    print(" Lets play games indoors...")

print()  # Space in terminal

age = 17
# Similar example but is asking if the user is 18
if age >= 18:
    print("Please proceed to check out")
else:
    print("Sorry you aren't 18")

print()  # Space in terminal

# ~ Exercise ~
# write a 12a, PG, 18, 15, X
# writing a program to check these conditions by getting user input

# If age <= 18 can't watch the movie
# if age 12 or under can't watch any movies above rating of 12
# Display messages accordingly

users_age = input("What is your age? ")
movie_rating = "X"

# If the movie is a alphanumeric rating it will convert it to a number
if movie_rating == "PG":
    movie_rating = 13
elif movie_rating == "X":
    movie_rating = 16

# Dynamic way to check users age and rating depending on what data was entered
# Using variables helps you avoid hardcoded control-flows
if int(users_age) <= movie_rating:
    print("You are {0} so you cannot watch this movie, Sorry!\n The required age is {1}years old.\n"
          .format(users_age, movie_rating.__str__()))
elif int(users_age) >= movie_rating:
    print("Ah you " + str(users_age) + " perfect! Please take a seat and enjoy the movie!")
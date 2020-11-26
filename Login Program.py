##########                                                Start of Code                                           ##########

"""
This is a Login program that provides security to a user's
login details.  

Developed by Bright U.O
"""
# Assign values to essential variables
user_name = input("Please enter your username: ")
password = input("Password: ")
# Login welcome message
welcome = "Your login was successful. Welcome @{}."
# Invalid detail message 
try_again = "Incorrect password entered. Try again with the correct password."
# Unsuccessful login message 
error = "Sorry, login wasn't successful and you have exhausted the trial limit."
# Create List to hold banned users
blacklist = []
# Loop switch
login = False
# Create trials variables
limit = 0
trials = 5

# Loop Login process
while login == False:
    confirmation = input("Retype password to login: ")
    limit += 1
    trials -= 1
    if confirmation != password and limit != 5:
        print(try_again)
        print("You have {} trial(s) left".format(trials))
    elif confirmation != password and limit == 5:
        print(error)
        print("{} has been blacklisted and subsequently denied access to this system.".format(user_name))
        blacklist.append(user_name)
        # Measure for new user profile creation
        while True:
            user_name = input("Enter a new username: ") 
            if user_name in blacklist:
                print("Username in blacklist. Try a different one.")   # >>> To prevent banned users from logging in
            else:
                password = input("Enter new password: ")
                trials = 5
                break
    else:
        confirmation == password
        print(welcome.format(user_name))
        login = True

##########                                                End of Code                                           ##########
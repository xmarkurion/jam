
print("Enter the name (upper case for the first letter)") 
inputFour = input(message)
# Round1#
match inputFour:
    case "Cathal":
        print("Everybody loves " + inputFour) 
    case "Oli":
        print("Everybody loves " + inputFour) 
    case "Eoghan":
        print("Everybody loves " + inputFour) 
    case "Marek":
        print("Everybody loves " + inputFour) 
        

    case _:
        print(inputFour + " is not a valid team member :/")



def hello(message):
    # When this command is used, everything after the word "hello" in the message will be sent to this function.
    # Example: "@Jam hello Ronan" -> this function receivces "Ronan" as the messsage.
    #
    # Your job is to process the message so that this function returns the correct outputs for challenge 1.
    # (for now, it just echoes back the same message)
    rValue = "Hello, Cisco!"
    return rValue

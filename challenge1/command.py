
def hello(message):
    # When this command is used, everything after the word "hello" in the message will be sent to this function.
    # Example: "@Jam hello Ronan" -> this function receivces "Ronan" as the messsage.
    #
    # Your job is to process the message so that this function returns the correct outputs for challenge 1.
    # (for now, it just echoes back the same message)
    if message == "Chuck Robbins":
        return f"Hello Cisco's favourite CEO Chuck Robbins"
    if( len(message) > 0 ):
        return f"Hello, {message}!"
    else:
        return f"Hello, Cisco!"
    

# //If the message length is greater than 0,
#  you can assume someone entered their name. Return a message in the format **“Hello, (name)!”**.
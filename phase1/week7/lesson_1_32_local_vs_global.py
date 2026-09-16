# Create a global variable
message = "Global message"

def show_message():
    # Create a local variable
    message = "Local message"
    print(message)

show_message()
print(message)
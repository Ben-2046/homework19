# Input the base and power
b = int(input("Base b: "))
n = int(input("Power n: "))

# Initialize the message string
message = ""

# Use range(1, n+1) to build the multiplication string
for x in range(1, n+1):
    message += str(b) + " X "

# Calculate the result
answer = b ** n

# Replace the last " X " with " = "
message = message[:-3] + f" = {answer}"

# Print the final message
print(message)
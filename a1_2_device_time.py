# Pseudocode
# 1. Prompt the user for the number of practices and whether they mow the lawn (yes or no).
# 2. If they mow the lawn, calculate device time as 15 minutes per practice.
# 3. If the number of practices is at least 7, give a cupcake bonus.
# 4. Display the allocated device time and cupcake message.

# User Input Point
print("Device Time Determinator")
practices = int(input("Number of practices: "))
mow_lawn = input("Did you mow? ").lower()

# Processing User Input with The Constant
if mow_lawn == "yes":
    device_time = practices * 15
    if practices >= 7:
        cupcake_bonus = "And you get a cupcake!"
    else:
        cupcake_bonus = ""
    message = f"You get {device_time} minutes of device time :)\n{cupcake_bonus}"
else:
    message = "No device time :("

# Output after User Inputting and Processing
print(message)

# Pseudocode
# 1. Initialize a variable to keep track of total sleep hours.
# 2. Loop for a week (7 days):
#    a. Prompt the user for the number of hours of sleep each day.
#    b. Add the daily sleep hours to the total sleep hours.
# 3. Calculate the average daily sleep by dividing the total sleep hours by 7.
# 4. Display the total sleep hours and average daily sleep.

## Constants for the application
DESIRED_HOURS_PER_DAY = 8
DAYS_IN_PERIOD = 5

# Initialize variables to default value 0
total_actual_sleep = 0

print("Sleep Tracker Application")

# Loop for a 5-day work-week
for day in range(1, DAYS_IN_PERIOD + 1):
    while True:
        try:
            hours_sleep = float(input(f"Night {day} hours sleep: "))
            if 0 <= hours_sleep <= 24:
                break
            else:
                print("Invalid number of hours. Please enter a value that is in the range of 0 to 24.")
        except ValueError:
            print("Invalid input. Please enter a valid number of hours.")

    total_actual_sleep += hours_sleep

# Calculating the sleep debt
total_desired_sleep = DESIRED_HOURS_PER_DAY * DAYS_IN_PERIOD
sleep_debt = total_desired_sleep - total_actual_sleep

# Output after the inputting of the values
print(f"Recommended total sleep is: {total_desired_sleep}")
print(f"Your total hours of sleep : {total_actual_sleep}")
print(f"Your sleep debt over this time is: {sleep_debt:.2f}")

# Check sleep debt status
if sleep_debt < 0:
    print("You are getting enough sleep. Keep it up!")
elif sleep_debt == 0:
    print("You are meeting your recommended sleep needs.")
else:
    print("You need more sleep. Try to get some rest!")

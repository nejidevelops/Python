# Pseudocode
# 1. Prompt the user for the number of hours worked and experience level.
# 2. Calculate the hourly pay rate based on the experience level using a constant.
# 3. Calculate the total pay by multiplying the hourly pay rate with the number of hours worked.
# 4. Display the experience level, hourly pay rate, and total pay to the user.


# Constants
BASE_PAY_RATE = 45.00

# User Input Point
print("Experience Counts Pay Calculator")
hours_worked = float(input("Number of hours worked: "))
experience_level = int(input("Experience level: "))

# Processing User Input with The Constant
hourly_pay_rate = BASE_PAY_RATE * (1 + experience_level * 0.05)
total_pay = hours_worked * hourly_pay_rate

# Output after User Inputting and Processing
print(f"Based on your experience level of ({experience_level}):")
print(f"Your hourly pay rate is ${hourly_pay_rate:.2f}")
print(f"Your total pay is ${total_pay:.2f}")

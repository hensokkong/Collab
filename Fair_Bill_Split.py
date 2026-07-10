# Define the total bill amount and the number of people
total_bill = 95.50
people = 4

# Calculate how much each person owes using float division
amount_per_person = total_bill / people

# Display the result rounded to two decimal places for currency
print(f"The total bill is ${total_bill:.2f}")
print(f"Divided among {people} friends, each person owes: ${amount_per_person:.2f}")
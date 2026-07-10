# Define the total number of slices and friends
total_slices = 20
friends = 6

# Calculate whole slices per person and the leftover remainder
slices_per_friend = total_slices // friends
leftover_slices = total_slices % friends

# Display the results
print(f"Each friend gets: {slices_per_friend} whole slices")
print(f"Slices left over: {leftover_slices}")
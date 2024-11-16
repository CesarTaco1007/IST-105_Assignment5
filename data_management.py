# Added comments explaining Git branching
import sys

# Function to check if a value can be converted to an integer
# Returns True if the value is numeric, otherwise False
def is_numeric(value):
    try:
        int(value)
        return True
    except ValueError:
        return False

# Collect the first five command-line arguments
args = sys.argv[1:6] 

# Validate the inputs:
# Ensure there are exactly five arguments and all of them are numeric
if len(args) != 5 or not all(is_numeric(arg) for arg in args):
    print("Content-Type: text/html\n")
    print("<p>Error: All inputs must be numbers.</p>")
    sys.exit(1)  # Exit if the inputs are invalid

# Convert the validated arguments to integers
numbers = [int(arg) for arg in args]

# Check if any of the numbers are negative
# Exit with an error message if negative numbers are found
if any(n < 0 for n in numbers):
    print("Content-Type: text/html\n")
    print("<p>Error: Negative numbers are not allowed.</p>")
    sys.exit(1)

# Calculate the average of the numbers
average = sum(numbers) / len(numbers)

# Check if the average is greater than 50 (boolean result)
is_avg_above_50 = average > 50

# Count the number of positive numbers in the list
positive_count = sum(1 for n in numbers if n > 0)

# Determine if the count of positive numbers is even using a bitwise operation
is_even_positive_count = (positive_count & 1) == 0

# Create a sorted list of numbers greater than 10
greater_than_10 = sorted([n for n in numbers if n > 10])

# Output results in HTML format for integration with a web application
print("Content-Type: text/html\n")
print(f"<p>Original Values: {numbers}</p>")  # Display the original list of numbers
print(f"<p>Average > 50: {is_avg_above_50}</p>")  # Display whether the average is above 50
print(f"<p>Even Positive Count: {is_even_positive_count}</p>")  # Display if positive count is even
print(f"<p>Sorted greater than 10 Values: {greater_than_10}</p>")  # Display sorted numbers > 10

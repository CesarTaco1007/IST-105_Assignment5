import sys

def is_numeric(value):
    try:
        int(value)
        return True
    except ValueError:
        return False

args = sys.argv[1:6] 
if len(args) != 5 or not all(is_numeric(arg) for arg in args):
    print("Content-Type: text/html\n")
    print("<p>Error: All inputs must be numbers.</p>")
    sys.exit(1)  

numbers = [int(arg) for arg in args]

if any(n < 0 for n in numbers):
    print("Content-Type: text/html\n")
    print("<p>Error: Negative numbers are not allowed.</p>")
    sys.exit(1)

average = sum(numbers) / len(numbers)
is_avg_above_50 = average > 50
positive_count = sum(1 for n in numbers if n > 0)
is_even_positive_count = (positive_count & 1) == 0
greater_than_10 = sorted([n for n in numbers if n > 10])

print("Content-Type: text/html\n")
print(f"<p>Original Values: {numbers}</p>")
print(f"<p>Average > 50: {is_avg_above_50}</p>")
print(f"<p>Even Positive Count: {is_even_positive_count}</p>")
print(f"<p>Sorted greater than 10 Values: {greater_than_10}</p>")
from turtle import Screen, Turtle

# Dictionary for memoization to store calculated sums
memo = {}


# Function to compute the sum of a list or tuple
def sum_list(values):
    # Check if the sum is already calculated
    values_tuple = tuple(values)  # Convert to tuple to use as a dictionary key
    if values_tuple in memo:
        return memo[values_tuple]

    # Calculate the sum of the list or tuple
    result = sum(values)

    # Store the result in memoization dictionary
    memo[values_tuple] = result

    return result


# Function to generate Koch curve instructions
def koch(n):
    if n == 0:
        return "F"
    tmp = koch(n - 1)
    return tmp + "L" + tmp + "R" + tmp + "L" + tmp + "R" + tmp + "L"


# Function to draw the Koch curve using Turtle
def draw_koch(n):
    s = Screen()  # create a screen
    t = Turtle()  # create a turtle
    directions = koch(n)  # get directions to draw Koch(n)

    for move in directions:
        if move == "F":
            t.forward(300 / (3**n))  # move forward with normalized size
        elif move == "L":
            t.left(60)  # turn 60 degrees left
        elif move == "R":
            t.right(120)  # turn 120 degrees right

    s.mainloop()  # keep the window open


# Test the corrected functions
n_tuple = (20, 10, 40, 28, 12, 53)

print("Sum of the tuple:", sum_list(n_tuple))  # Output: 163

# Draw the 3rd Koch curve
draw_koch(3)  # Adjust the level as needed

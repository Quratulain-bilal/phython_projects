import turtle

# Turtle setup
tu = turtle.Turtle()
tu.screen.bgcolor("black")  # Set background color
tu.pensize(2)  # Set pen size
tu.color("green")  # Initial color
tu.left(90)  # Face upwards
tu.backward(100)  # Move turtle backward to start position
tu.speed(100)  # Set speed
tu.shape("turtle")  # Set turtle shape

# Function to write heading
def write_heading():
    tu.penup()
    tu.goto(-50, 200)  # Move to a good position
    tu.color("white")  # Text color

    tu.goto(0, -100)  # Reset position
    tu.pendown()

# Recursive tree function
def tree(i):
    if i < 10:
        return
    else:
        tu.forward(i)  # Move forward
        tu.color("orange")  # Change color to orange
        tu.circle(2)  # Draw small circle
        tu.color("brown")  # Change color to brown
        
        tu.left(30)  # Turn left
        tree(3 * i / 4)  # Recursive call for left branch
        
        tu.right(60)  # Turn right
        tree(3 * i / 4)  # Recursive call for right branch
        
        tu.left(30)  # Reset angle
        tu.backward(i)  # Move backward

# Call heading function
write_heading()

# Call tree function
tree(100)

# Keep turtle window open
turtle.done()

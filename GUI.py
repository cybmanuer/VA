import turtle

# Function to start the virtual assistant
def start_virtual_assistant(x, y):
    # Add your virtual assistant code here
    output_text.clear()  # Clear the output text
    output_text.write("Virtual assistant started!", align="center", font=("Arial", 14, "normal"))

# Function to stop the virtual assistant
def stop_virtual_assistant(x, y):
    # Add any necessary cleanup code here
    output_text.clear()  # Clear the output text
    output_text.write("Virtual assistant stopped!", align="center", font=("Arial", 14, "normal"))

# Create the turtle window
window = turtle.Screen()
window.title("Virtual Assistant GUI")
window.bgcolor("white")

# Create the start button
start_button = turtle.Turtle()
start_button.penup()
start_button.goto(0, -50)
start_button.shape("square")
start_button.color("green")
start_button.shapesize(2, 4)
start_button.onclick(start_virtual_assistant)

# Create the stop button
stop_button = turtle.Turtle()
stop_button.penup()
stop_button.goto(0, -100)
stop_button.shape("square")
# create a text on button
stop_button.color("red")
stop_button.shapesize(2, 4)
stop_button.onclick(stop_virtual_assistant)
stop_button.write("Stop", align="center", font=("Arial", 14, "normal"))

# Create the output text turtle
output_text = turtle.Turtle()
output_text.penup()
output_text.goto(0, 50)
output_text.color("black")
output_text.hideturtle()

# Run the turtle event loop
turtle.mainloop()

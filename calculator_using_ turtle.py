import turtle

# --- 1. Screen Setup ---
screen = turtle.Screen()
screen.title("Turtle Calculator")
screen.setup(width=400, height=500)
screen.tracer(0) # Turns off animation so the UI draws instantly

pen = turtle.Turtle()
pen.hideturtle()
pen.speed(0)

# Global variable to hold our math equation
expression = ""

# --- 2. Button Layout ---
# List of buttons: [x_center, y_center, width, height, "Label"]
buttons = [
    [-112.5,  50, 65, 50, "7"], [-37.5,  50, 65, 50, "8"], [ 37.5,  50, 65, 50, "9"], [112.5,  50, 65, 50, "/"],
    [-112.5, -20, 65, 50, "4"], [-37.5, -20, 65, 50, "5"], [ 37.5, -20, 65, 50, "6"], [112.5, -20, 65, 50, "*"],
    [-112.5, -90, 65, 50, "1"], [-37.5, -90, 65, 50, "2"], [ 37.5, -90, 65, 50, "3"], [112.5, -90, 65, 50, "-"],
    [-112.5,-160, 65, 50, "C"], [-37.5,-160, 65, 50, "0"], [ 37.5,-160, 65, 50, "="], [112.5,-160, 65, 50, "+"]
]

def draw_button(x, y, w, h, text):
    """Draws a rectangular button and writes text inside it."""
    pen.penup()
    pen.goto(x - w/2, y + h/2) # Go to top-left corner of the button
    pen.pendown()
    
    # Draw rectangle
    for _ in range(2):
        pen.forward(w)
        pen.right(90)
        pen.forward(h)
        pen.right(90)
        
    # Write text in the center
    pen.penup()
    pen.goto(x, y - 10) 
    pen.write(text, align="center", font=("Arial", 16, "bold"))

def draw_display():
    """Draws the screen at the top that shows the numbers."""
    pen.penup()
    pen.goto(-145, 170)
    pen.pendown()
    
    # Draw display box
    for _ in range(2):
        pen.forward(290)
        pen.right(90)
        pen.forward(60)
        pen.right(90)
        
    pen.penup()
    pen.goto(130, 125)
    
    # Show '0' if empty, otherwise show the math expression
    display_text = expression if expression else "0"
    pen.write(display_text, align="right", font=("Arial", 24, "normal"))

def draw_ui():
    """Clears the screen and redraws everything based on current state."""
    pen.clear()
    draw_display()
    for btn in buttons:
        draw_button(btn[0], btn[1], btn[2], btn[3], btn[4])
    screen.update()

# --- 3. Click Logic ---
def handle_click(x, y):
    """Determines which button was clicked based on mouse coordinates."""
    global expression
    
    for btn in buttons:
        bx, by, bw, bh, text = btn
        
        # Check if the mouse click (x,y) is inside the button's boundaries
        if (bx - bw/2 <= x <= bx + bw/2) and (by - bh/2 <= y <= by + bh/2):
            if text == "C":
                expression = "" # Clear
            elif text == "=":
                try:
                    # eval() does the math for us based on the string
                    expression = str(eval(expression))
                except Exception:
                    expression = "Error"
            else:
                if expression == "Error":
                    expression = ""
                expression += text
                
            draw_ui() # Redraw the screen to update the display
            return

# --- 4. Start the Program ---
draw_ui()
screen.onscreenclick(handle_click) # Tell turtle to listen for mouse clicks
turtle.done()
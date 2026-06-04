<h2>Turtle Graphical Calculator</h2>

A fully functional, clickable graphical calculator built entirely using Python's built-in turtle module. This project bypasses standard GUI frameworks (like PyQt or Tkinter)
to demonstrate a deep understanding of coordinate geometry, custom UI rendering, and event-driven programming using only core Python.


🚀 Features : 
Custom UI Rendering: Dynamically draws a complete numeric keypad, mathematical operators, and a visual display screen from scratch using turtle graphics.

Coordinate-Based Collision Detection: Maps mouse click coordinates (X, Y) to specific button boundaries to determine user input.

Event-Driven Architecture: Utilizes turtle.onscreenclick() to actively listen for user interactions and update the graphical state in real-time.

Dynamic Equation Evaluation: Captures button clicks as strings and processes the final mathematical expression using Python's eval() function, complete with try-except error handling for invalid operations (e.g., division by zero).

Zero External Dependencies: Runs completely out-of-the-box using the Python Standard Library.

🛠️ Skills Demonstrated : 


Graphical User Interface (GUI) Logic: Understanding screen states, rendering loops, and instantaneous visual updates (screen.tracer(0)).

Event Listeners & Callbacks: Handling asynchronous user inputs via mouse clicks.

Algorithmic Thinking: Creating a collision-detection algorithm to verify if a mouse click falls within a button's mathematical area.

String Manipulation & Error Handling: Safely building and evaluating mathematical strings while catching calculation exceptions.

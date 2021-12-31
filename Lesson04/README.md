1. Introduction to Turtle graphics

   - [Turtle graphics](https://docs.python.org/3/library/turtle.html) is a built-in Python library that enables users to create pictures and shapes by providing them with a virtual canvas. The onscreen pen that you use for drawing is called the turtle and this is what gives the library its name.

   - Basic turtle graphics operations
     ```
     # first, import turtle library
     import turtle

     # set screen color
     turtle.bgcolor("gray")

     # set screen title
     turtle.title("My cool drawings")    

     # initialize a variable to access turtle
     t = turtle.Pen()

     # move the turtle
     t.forward(100)
     t.backward(200)

     # turn the turtle
     t.right(90)
     t.left(90)

     # draw a circle
     t.circle(150)

     # move the turtle to any position
     t.goto(100, 100)
     t.goto(-50, -40)
    
     # change the color of the pen
     t.pencolor('purple')

     # set the line thickness with either of the following
     t.width(5)
     t.pensize(5)
     
     # set turtle speed
     t.speed(0)
     t.speed(1)
     ```

1. Review and pratice the following sample codes
   1. [Draw a square](https://github.com/pangmi/learntocode/blob/main/Lesson04/Code/MySquare1.py)
     
   1. [Draw another square](https://github.com/pangmi/learntocode/blob/main/Lesson04/Code/MySquare2.py)
     
   1. [Square spiral](https://github.com/pangmi/learntocode/blob/main/Lesson04/Code/MySquareSpiral.py)
   
1. Home work
   1. Create a program which draws a triangle with the size length provided by the user. **Hint**: use `input()` function to ask user to enter the size length.
   2. Create a program which draws a pentagon with the size length provided by the user. **Hint**: use `input()` function to ask user to enter the size length.
   3. Create a program which draws a hexagon with the size length provided by the user. **Hint**: use `input()` function to ask user to enter the size length.
   4. Create a program which draws a rectangle with the length and width provided by the user. **Hint**: use `input()` function to ask user to enter the length and width.


1. Python programming style:
   - Proper indent in code block:
      ```
      # indent 4 spaces within code block
      for x in range(10):
          x = x * 2
          print(x)
      ```

1. Some cool featues in turtle graphics:
   ```
   import turtle
   t = turtle.Pen()

   # turtle shape:
   t.shape('turtle')   # arrow, turtle, circle, square, triangle, classic
   
   # turtle color:
   t.color('green')
   
   # turtle pen and outline color
   t.pencolor('blue')
   
   # turtle size
   t.turtlesize(3, 3, 2)
   ```
   
1. Sample Code:
   ```
   import turtle

   t = turtle.Pen()

   t.shape('turtle')
   t.color('green')
   t.pencolor('blue')

   t.turtlesize(3, 3, 2)

   t.forward(200)
   t.right(120)
   t.forward(200)
   t.right(120)
   t.forward(200)

   t.pencolor('red')
   t.circle(200)
   t.pencolor('orange')
   t.circle(150)
   t.pencolor('pink')
   t.circle(100)

   t.pencolor('purple')
   for x in range(4):
       t.forward(200)
       t.right(90)
   ```
   
1. Practice 
   - Review and practice all the programs in the downloaded sample code **s02** folder

1. Homework
   1. Create a program which draws a polygon with any number of sizes from 3 to 100:
      - the program asks the user to enter the number of size from 3 to 100.
      - then, it asks the user to enter the size length.
      - the program will use the folloing colors alternately in drawing the polygon: *"red", "yellow", "blue", "orange", "green", "purple"*
   2. Create a program which draws a star like below:\
      ![image](https://user-images.githubusercontent.com/36340668/148716949-67be0460-4807-4ba0-a7a0-6f433f80082c.png)

      - the program asks the user to enter the size length of the star.
      - draw each side with different colors

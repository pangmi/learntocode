#### 1. Revisit Turtle graphics:
   - Review Turtle methods and coordinate at [Lesson04](https://github.com/pangmi/learntocode/tree/main/Lesson04)
   - New Turtle methods:
      - `setpos(x, y)`: Move turtle to (x, y) position. Remember, we had also learned `goto(x, y)` which is the same as `setpos(x, y)`.
      - `turtle.window_width()`: Return the width of the turtle window.
      - `turtle.window_height()`: Return the height of the turtle window.
   
#### 2. Code examples:
   ``` Python
   import turtle
   
   t = turtle.Pen()
   t.pencolor('purple')
   t.penup()
   t.setpos(170, 200)
   t.pendown()
   
   width = turtle.window_width()
   print(width)
   
   h = turtle.window_height()
   print(h)
   ```
   
#### Homework
   1. Review Turtle graphics in [Lesson04](https://github.com/pangmi/learntocode/tree/main/Lesson04)
   2. Review Random libary in [Lesson13](https://github.com/pangmi/learntocode/tree/main/Lesson13)
   3. Review and run `RandomSpirals.py` in sample code **s06** folder
   4. Review and run `RockPaperScissors.py` in sample code **s06** folder
   5. Write a program to create 10 random stars in random positions. Be creative to make these stars have different color, length, etc. ***Hint***: We had created a star in [Lesson05](https://github.com/pangmi/learntocode/tree/main/Lesson05) before.
   6. Write a program to create a list of 100 random numbers from 1, 2 and 3. 
      - You must add each number into the list and then print them out all together.
      - Count the total number of 1s, 2s and 3s, and print these total counts out

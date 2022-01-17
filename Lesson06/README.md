#### 1. Primitive Types
   - Integer: `35`
   - Float: `3.5`
   - String: `'Thirty Five'`
   - Boolean: `True` / `False`

#### 2. Other Types
   - List: 
     ```
     coders = ['Kingston', 'Felix', 'Clara']
     prime_nums = [3, 7, 11, 17, 19, 29]
     ```

   - Range:
     ```
     a = range(5)            # a = 0, 1, 2, 3, 4
     b = range(1, 8)         # b = 1, 2, 3, 4, 5, 6, 7
     c = range(0, 14, 3)     # c = 0, 3, 6, 9, 12
     d = range(8, 1, -1)     # d = 8, 7, 6, 5, 4, 3, 2
     ```
     
#### 3. Variable Name and Programming Style
   - Variable name should begin with a letter (a - z)
   - The rest of the name can include letters, numbers, or underscore ( _ )
   - Variable name should be lowercase words with underscore in between
   - **Remember**: variable names are case sensitive

#### 4. Numbers and Arithmetic Operators
   - Please review [Arithmetic Operators](https://github.com/pangmi/learntocode/blob/main/Lesson01/README.md#arithmetic-operators)
   - Please review and learn from the following code on how to assign operation result back to the same variable
     ```
     x = 24
     x = x + 1
     print(x)
     x = x - 1
     print(x)
     x = x * 2
     print(x)
     x = -x
     print(x)
     x = +x
     print(x)
     x = -x
     print(x)
     x = x ** 2
     print(x)
     ```

#### 5. Syntax Errors
  ```
  What is 1 + 2?
  3 + 4 = 
  ```

#### 6. Introducing New Functions from turtle
  ```
  t.penup()
  t.pendown()
  t.goto(200, 200)
  ```

#### 7. Sample Code
   - Multiply all the number in a number list
     ```
     # Multiply all the number in a number list
     nums = [5, 7, 8, 13, 25, 100]
     product = 1
     for x in nums:
         product = product * x
         print(product)

     print('The Final Product is', product)
     ```
   - Using new turtle functions:
     ```
     import turtle

     t = turtle.Pen()

     t.speed(9)
     turtle.bgcolor("black")

     t.pencolor('blue')
     t.circle(40)
     t.penup()
     t.goto(-100, 100)
     t.pendown()
     t.goto(200, 200)
     t.goto(200, 0)
     t.goto(0, 0)
     ```

#### 8. Please review and run the following programs in sample code **s03** folder
   - ThankYou.py
   - AtlantaPizza.py
   - SayMyName.py
   - SpiralMyName.py

#### 9. Homework
   - Write a program, which asks user to enter a number, then increase the number itself by 5, then decrease itself by 2, and then square itself up. For example, if the user enters 25, the expected the results should be like below:
     ```
     Please enter a number: 25
     n + 5 = 30
     n - 2 = 28
     The square of n =  784
     ```

   - Write a program, which asks user to enter a positive number and then generates the [factorial](https://en.wikipedia.org/wiki/Factorial) of the number. The expected result should be like below:
     ```
     Please enter a positive number: 9
     n! = 362880
     ```
     ***Hint:*** 1. Refer to the first sample code on how to accumulate the result.    2. Use the newly learned range function

   - With newly learned turtle functions, write a program to generate a smiley face like the following 
     ![image](https://user-images.githubusercontent.com/36340668/149713921-96217238-f8f0-45e6-9d03-9ac6a0a39da6.png)
     
     ***Hint:*** For your reference, you can use the following coordinates, radiuses and sizes
     ![image](https://user-images.githubusercontent.com/36340668/149713361-cba17b8f-469f-4b50-b74d-4198a497cdc8.png)
     

    

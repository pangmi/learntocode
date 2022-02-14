#### 1. if statement
   The ***if*** statement allows us to tell the computer to execute a set of statements based on a condition:
   ```python
   if condition:
       statement(s)
   ```

   For example:
   ``` Python
   x = 12
   if x > 0:
       print(x, 'is positive number')
   ```

#### 2. boolean expressions for ***Python*** condition:
   - Equals:  `a == b`
   - Not Equals: `a != b`
   - Less than:  `a < b`
   - Less than or equal to:  `a <= b`
   - Greater than:  `a > b`
   - Greater than or equal to:  `a >= b`
   
   Examples:
   ``` Python
   a = 56
   b = 64
  
   a == b
   False
   a != b
   True
   a < b
   True
   a <= b
   True
   a > b
   False
   a >= b
   False

   b <= 64
   True
   b >= 64
   True

   if b > a:
       print("b is greater than a")
   ```

#### 3. if-else statement
   ```python
   if condition:
       statement(s)
   else:
       statment(s)
   ```

   For example:
   ``` Python
   x = -12
   if x > 0:
       print(x, 'is positive number')
   else:
       print(x, 'is negative or zero')

   if x % 2 == 0:
       print(x, 'is even number')
   else:
       print(x, 'is odd number')       
   ```

#### 4. if-elif-else statement
   ```python
   if condition1:
       statement(s)
   elif condition2:
       statement(s)
   elif condition3:
       statement(s)
   ....
   else:
       statment(s)
   ```

   For example:
   ``` Python
   x = 0
   if x > 0:
       print(x, 'is positive number')
   elif x < 0:
       print(x, 'is negative number')
   else:
       print(x, 'is zero')
   ```

#### Homework
   1. Review and run all programs in sample code ***s04*** folder
   2. ***Learn about [Caesar Cipher](https://en.wikipedia.org/wiki/Caesar_cipher) as we will discuss it in the next class***
   3.  Write a program to create a list of your teammates' names in one of your sports team:
       - Ask user to enter a teammate name or letter ***q***
       - If user entered letter ***q***, end the iteration
       - Otherwise, add the name to the list.
       - Continue to ask the user to enter 
       - When the iteration ends, print out the list
   4. Write a program to create a list of colors excluding *white*:
       - Ask user to enter a color or letter ***q***
       - If user entered letter ***q***, end the iteration
       - If the color is *white*, do not add it to the list
       - Otherwise, add the color to the list.
       - Continue to ask the user to enter 
       - When the iteration ends, print out the list

   5. Write a program to create a list of even numbers in the following iteration:
       - Ask user to enter a number or letter ***q***
       - If user entered letter ***q***, end the iteration
       - If the number is *even*, add it to the list
       - Continue to ask the user to enter 
       - When the iteration ends, print out the list of even numbers

   6. Write a program to ask user to enter a number,
       - If the number is *even*, print a message indicating the number is even
       - If the number is *odd*, print a message indicating the number is odd
       - If the number is a multiple of 4, print a message like `the number is multiple of 4`. 
       - **Please note**: if the number is a multiple of 4, you should not print the message that indicates the number is even. For example, if the user entered `24`, you only print out `24 is multiple of 4`.

   7. Write a program to ask user to enter two numbers,
       - If the numbers are equal, print a message indicating they are equal
       - Otherwise, print out the bigger number. For example, if user entered 46 and 105, the output should be `105 is the bigger number`
   
   8. Write a program to create a list of odd numbers with the following steps:
       - Ask user to enter two positive numbers
       - Find all the odd numbers between these two numbers, and add them to a list
       - print out the list
   
   9. Write a program to ask user to enter three numbers and print out the biggest number. **Please do not use Pythton [max](https://docs.python.org/3/library/functions.html#max)** function.

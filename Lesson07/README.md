#### 1. New turtle functions
   - Pop up a dialog window for input of a string 
     ```
     turtle.textinput(title, prompt)
     ```
     
   - Pop up a dialog window for input of a number 
     ```
     turtle.numinput(title, prompt, default=None, minval=None, maxval=None)
     ```

#### 2. In-place (Shorthand) Assignment Operations

   | Operation | Description |
   |-----------|-------------|
   | x += y  | x = x + y |
   | x -= y  | x = x - y |
   | x *= y  | x = x * y |
   | x /= y  | x = x / y |
   | x //= y  | x = x // y |
   | x **= y  | x = x ** y |
   | x %= y  | x = x % y |

#### 3. while loop
   ```
   i = 1
   while i < 10:
       print(i)
       i += 2
   ```
   
   **Note**: be aware of the following infinite loops:
   ```
   i = 1
   while i < 10:
       print(i)
   ```
   
   ```
   condition = True
   while condition:
       print('Ok')   
   ```
   
#### 4. Homework
   - Review and run all programs in sample code ***s03*** folder

   - Write a program to accept a positive number from a user and calculate the sum of all numbers from 1 to a given number. For example, if the user entered 10,
     the output should be 55. The expected result should be like below:
     ```
     Please enter a positive number: 10
     Sum = 55
     ```
   
   - Write a program which keeps doing the following:
     1. Ask user to enter a number between 10 to 50, or enter letter ***q***
     1. If user entered letter ***q***, exit the program
     1. Otherwise, print all the even numbers from 0 to the given number. For example, if user entered 9, the ouput should be 0, 2, 4, 6, 8. If user entered 12, 
        the program should print the number 0, 2, 4, 6, 8, 10, 12.
     1. Continue to ask the user to enter

   - 2022 Winter Olympic Game is coming. Please write a program to draw an Olympic Symbol like below:
   
     ![Olympic Rings](https://upload.wikimedia.org/wikipedia/commons/thumb/5/57/International_Olympic_Committee_logo_2021.svg/500px-International_Olympic_Committee_logo_2021.svg.png)
     
     **Note**: 
        - You also need to output the words: International Olympic Committee
        - To make you code simple and elegant, please use a loop to draw the rings

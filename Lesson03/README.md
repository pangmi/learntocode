1. Python programming style:
   - Variable names should be lowercase, with words separated by underscores as necessary
   ```
   # the following are good variable names:
   myage = 7
   my_age = 7

   # the following are not good pratice:
   Myage = 7
   myAge = 7
   MyAge = 7
   ```

1. List is a collection of items
   ```
   numbers = [32, 1, 45, 60]
   even_numbers = [2, 4, 6, 8, 12]
   strs = ['aa', 'bb', 'cc']
   cars = ["Ford Mustang", "Chevy Malibu", "BMW X5", "Toyata Camry", "Tesla 3"]
   coders = ['Kingston', 'Felix', 'Clara']

   # use index to access items in list (index is 0 based)
   some_coder = coders[1]
   print(some_coder)
   print(len(coders))
   print(coders)
   print(coders[0], coders[1], coders[2])
   ```

1. Function range() returns a sequence of numbers within the given range. It is commonly used for loop
   ```
   # range(number): returns a sequence of number from 0 to number-1
   # range(10): returns 0, 1, 2, 3, ..., 9
   # range(360): return 0, 1, 2, 3, ..., 359

   seq = range(6)
   print(seq)
   print(len(seq))

   for x in range(10):
       print(x, x**2, x**3, x*2, x*3)
   ```

1. Function input() takes input from user with a prompting message. **Please note**, it returns the user input as a string.
   ```
   name = input('Please enter your name: ')
   print("Hello", name, name, name, name, name)
   ```

1. Homework:
    - Create a list consisting of odd numbers 3, 7, 15, 17, 27, 31, 45, and print out their square numbers. Can you use the [**for**](https://www.w3schools.com/python/python_for_loops.asp) loop? The expected result should be like the following:
      ```
      3 x 3 = 9
      7 x 7 = 49
      15 x 15 = 225
      ...
      45 x 45 = 2025
      ```
    
    - Create a sequence number of 0, 1, 2, 3, ..., 20, and print out their square numbers using range() function and [**for**](https://www.w3schools.com/python/python_for_loops.asp) loop. The expected result should be like the following:
      ```
      0 x 0 = 0
      1 x 1 = 1
      2 x 2 = 4
      ...
      20 x 20 = 400
      ``` 
 
    - Create a program which asks user the temperature in Fahrenheit and [**convert**](https://www.metric-conversions.org/temperature/fahrenheit-to-celsius.htm) it to Celsius. The program should be run like below:
      ```
      Please enter temperature in Fahrenheit: 68
      The temperature in Celsius: 20
      ``` 

    - Create a program which asks user to enter two numbers and calculates the addition, substraction and multiplication of these two numbers. The program should be run like below:
      ```
      Please enter the first number x: 12
      Please enter the second number y: 7
      x + y = 19
      x - y = 5
      x * y = 84
      ``` 

1. Practice 
   - Practice the programs in the [Code](https://github.com/pangmi/learntocode/tree/main/Lesson03/Code) folder
   - Practice the programs in the downloaded sample code **s01** folder

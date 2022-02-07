#### 1. String operations
   Strings are stored as sequences of Unicode characters indexed by integers, starting at zero.
   ``` Python
   a = 'Hello World'
   print(len(a))            # 11
   b = a[4]                 # b = 'o'
   c = a[-1]                # c = 'd'

   c = a[:5]                # c = 'Hello'
   d = a[6:]                # d = 'World'
   e = a[3:8]               # e = 'lo Wo'
   f = a[-5:]               # f = 'World'
   ```

#### 2. Review range()
   ``` Python
   list(range(10))          # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
   list(range(1, 11))       # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
   list(range(12, 1, -2))   # [12, 10, 8, 6, 4, 2]
   ```

#### 3. while loop
   **Syntax**:
   
       while condition:       
           indented statements

   We test a condition in the while loop.
   If the condition is True, we execute the indented statements in the code block;
   otherwise, we exit the loop.

#### 4. Construct a loop for repeating codes
   We can get the same result with different loops. For example, the following two code block will print our the same even numbers:
   
   ``` Python
   num = 21
   x = 0
   while x <= num:
       print(x)
       x += 2
   ```
   
   ``` Python
   for x in range(0, num, 2):
       print(x)
   ```
   
#### 5. Nested loops
   A nested loop is a loop within another loop
   
   **Examples**:
   ``` Python
   for x in range(10):
       for y in range(6):
           print(x, end=' ')
       print()
   ```
   ``` Python
   for x in range(1, 10):
       for y in range(1, x+1):
           result = y * x
           print(result, end=' ')
       print()   
   ```
   ``` Python
   for x in range(9, -1, -1):
       for y in range(x):
           print(x, end=' ')
       print()
   ```   

#### 6. Working with lists
   ``` Python
   # start with an empty list
   codi = []
   
   # add elements to the list
   codi.append('Clara')
   codi.append('Felix')
   codi.append('Kingston')
   codi.append('Knighton')
   print(codi)
   
   # check the length of the list
   len(codi)
   
   # modify / replace element
   codi[3] = 'Bing'
   print(codi)
   
   # remove element
   del codi[3]
   print(codi)   
   ```

#### Homework
   - Read the following post to understand how to use ***sep*** and ***end*** parameters in the `print` statement.
     https://www.studytonight.com/post/the-sep-and-end-parameters-in-python-print-statement
     
   - Write a program to iterate from 1 to 10. In each iteration, print the previous number, current number and their sum. The expected output should be the following:
     ``` Python
     Previous number: 0 Current number: 1 Sum: 1
     Previous number: 1 Current number: 2 Sum: 3
     Previous number: 2 Current number: 3 Sum: 5
     Previous number: 3 Current number: 4 Sum: 7
     Previous number: 4 Current number: 5 Sum: 9
     Previous number: 5 Current number: 6 Sum: 11
     Previous number: 6 Current number: 7 Sum: 13
     Previous number: 7 Current number: 8 Sum: 15
     Previous number: 8 Current number: 9 Sum: 17
     Previous number: 9 Current number: 10 Sum: 19     
     ```

   - Write a program to accept a string from the user and display characters that are present at an even index number. For example, if user input ***PythonIsFun***, the output should be `y h n s u`

   - Write a program to create a number list in the following iteration:
     1. Ask user to enter a number or letter ***q***
     1. If user entered letter ***q***, end the iteration
     1. Otherwise, add the number to the list.
     1. Continue to ask the user to enter 
     1. When the iteration ends, print out the list

   - Write a program to print out the following pattern:
     ``` Python
     1 
     1 2 
     1 2 3 
     1 2 3 4 
     1 2 3 4 5 
     ```

   - Write a program to print out multiplication table. The expected output should be the following:
     ``` Python
     1x1=1  
     1x2=2  2x2=4  
     1x3=3  2x3=6  3x3=9  
     1x4=4  2x4=8  3x4=12  4x4=16  
     1x5=5  2x5=10  3x5=15  4x5=20  5x5=25  
     1x6=6  2x6=12  3x6=18  4x6=24  5x6=30  6x6=36  
     1x7=7  2x7=14  3x7=21  4x7=28  5x7=35  6x7=42  7x7=49  
     1x8=8  2x8=16  3x8=24  4x8=32  5x8=40  6x8=48  7x8=56  8x8=64  
     1x9=9  2x9=18  3x9=27  4x9=36  5x9=45  6x9=54  7x9=63  8x9=72  9x9=81  
     ```
     Please refer to the first exercise on how to use ***sep*** and ***end*** parameters in the `print` statement
     
   - Write a program to draw a rosette with a number of circles:
     1. Ask the user to enter the number of circles
     1. Ask the user to enter the color for the rosette
     1. Draw the rosette with circle radius of 150
     
     The expected output should be like below with color *green* and 50 circles
     ![image](https://user-images.githubusercontent.com/36340668/151743728-8f85d1f7-987d-4af4-b676-42d4eeb32bff.png)
     
   - Write a program to draw nested rosettes with a number of circles:
     1. Ask the user to enter the number of circles
     1. Ask the user to enter the color for the outside rosette
     1. Ask the user to enter the color for the outside rosette
     1. Draw the rosettes with circle radiuses of 150, 75
     
     The expected output should be like below with color *blue*, *red*,  and 50 circles
     ![image](https://user-images.githubusercontent.com/36340668/151744110-1115a42c-9274-4dd9-ad12-38f0f692a8c0.png)

   - ***Challenge Problem 01***: Print out a STAR tree with the following pattern:
     ``` Python
               *
              ***
             *****
            *******
           *********
          ***********
         *************
        ***************
       *****************
      *******************
               *
               *
               *
               *
               *   
     ```

   - ***Challenge Problem 02***: Write a program to print out a STAR tree. The program first asks user to enter the number of lines of the tree's main part and then print it out. For example, if the user enters *19*, the expected result should be the following:
     ``` Python
      Please enter the number of lines of the tree's main part: 19
      
                        *
                       ***
                      *****
                     *******
                    *********
                   ***********
                  *************
                 ***************
                *****************
               *******************
              *********************
             ***********************
            *************************
           ***************************
          *****************************
         *******************************
        *********************************
       ***********************************
      *************************************
                        **
                        **
                        **
                        **
                        **
     ```
     

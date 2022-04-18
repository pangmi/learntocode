#### 1. Review some basic arithmetic operations:
   ``` Python
   hours = 2
   mins = 34
   secs = 12
   
   total_secs = hours * 60 * 60 + mins * 60 + secs
   print('Total Seconds:', total_secs)
   ```

#### 2. Review some string operations:

   ``` Python
   # split function
   str = "02:06:35"
   ts = str.split(':')
   print(ts)
   ```
   
   ``` python
   # Access string
   s = 'Hello World!'
   for x in s:
       print(x)
       
   # First letter in string
   print(s[0])
   
   # string size
   print(len(s))
   
   # Last letter in string
   print(s[len(s) - 1])
    
   ```

#### 3. `break` statement
   The `break` statement terminates / breaks out from the current loop, and resumes the next statement right after the current loop.
   
   ``` Python
   str = 'Hello World!'
   for s in str:
       if (s == ' '):
           break
       print(s)

   print('Program ends')
   ```
   
   ``` Python
   nums = [3, 5, 6, 3, 4, 5, 7, 9, 10, 19, 13]
   for x in nums:
       if x == 4:
           break
       print(x);
   ```   
   
   ``` Python
   # break from inner loop
   for x in range(1, 6):
       for y in range(1, 6):
           if y > 3:
               break
           print(x, '*', y, '=', x * y)
   ```

#### 4. `continue` statement
   The `continue` statement skips the rest of the code in the current loop. Loop does not terminate but continues on with the next iteration.
   
   ``` Python
   # The following code will not print out the space in the text
   str = 'Hello World!'
   for s in str:
       if (s == ' '):
           continue
       print(s, end='')
   ```
   
   ``` Python
   # print all numbers from 1 to 100 except those that can be divided by 3
   for n in range(1, 101):
       if n % 3 == 0:
           continue
       print(n, end=', ')   
   ```
   
   ``` Python
   # providing a sentence, do not print out vowels and spaces
   str = input('Please enter a statement: ')
   for i in str:
       if i.lower() in 'aeiou' or i == ' ': 
           continue
       print(i, end='')   
   ```
   
#### Homework
   1. Review Windows commannds in [Lession 11](https://github.com/pangmi/learntocode/blob/main/Lesson11/readme.md)
   1. Write a program to convert time to seconds with the following steps:
       - Ask use to enter time with the format of ***hh:mm:ss***
       - Convert the time to total seconds. 
       - For example, if user enters ***02:34:12***, the program should print out ***Total Seconds: 9252***
   1. Write a program that asks user to enter a string and returns the number of vowels contained within it. 
       - Let's assume the vowels are `A, E, I, O, U`
       - For example, if user enters ***Hello Everyone!***, the program should print out ***Total vowels: 6***
   1. Write a program that asks user to enter a string and returns that string in reverse order. For example, if user enters ***Hello***, the result should be ***olleH***
   1. Write a program to print odd numbers starting from 1 to 200. However, when the odd number can be divided by 11 and 13, stop printing and exit the program.

   1. Write a program that asks user to enter a string and returns the number of consonants contained within it. 
       - A consonat letter is a letter which is not `A, E, I, O, U`
       - For example, if user enters ***Hello Everyone!***, the program should print out ***Total consonants: 7***
       - *hint*: Use `isupper()`, `islower()` or `isalpha()` to check if a character is alphabet letter
   1. Write a program to print even numbers from 2 to 100 except those that can be divided by 6 or 9 or 13.
   1. Write a program to encode text to numbers:
       - Ask user to enter a positive shift value (1 - 10)
       - Ask user to enter any text message
       - Encode the text into a list of numbers and print out the result. *Hint*: you can use function `ord()` to convert text to an ASCII number

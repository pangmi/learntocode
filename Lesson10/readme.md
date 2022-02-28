#### 1. Data (chracters, numbers) are stored as numeric binary in computer.
   ASCII (American Standard Code for Information Interchange)


#### 2. `not` operator
   The ***not*** operator syntax:
   ```python
   not operand
   ```
   `not` operator returns True if the operand is False, and returns False if the operand is True

   For example:
   ``` Python
   a = False
   if not a:
       print('Variable "a" is False')
   
   x = '#'
   if not x.isupper():
       print('x is not upper case')
   ```

#### 3. if statement with multiple conditions
   ```python
   if (cond1 and/or COND2) and/or(cond3 and/or cond4):
       code1
   else:
       code2
   ```

   Example:
   ```python
   a = 19
   b = 89
   c = 64
  
   if a > b and a > c:
       print("a is the largest")
   elif b > a and b > c:
       print("b is the largest")
   elif c > a and c > b:
       print("c is the largest")
   else:
       print("The numbers are equal")
   ```

#### 4. New Python functions:
   - `ord()` returns the number of a specified character
   - `chr()` returns the character that represents the specified unicode
   - `isupper()` returns True if all the characters are in upper case, otherwise False
   - `islower()` returns True if all the characters are in lower case, otherwise False
   - `upper()` returns a string where all characters are in upper case
   - `lower()` returns a string where all characters are lower case
   - `split()` splits a string into a list.
   - concate string with + operator

   Example:
   ```python
   ord('A')
   ord('Z')
   ord('!')
   ord('a')
   ord('r')
   chr(114)
   chr(87)
   chr(33)
   
   x = 'a'
   x.isupper()
   x.islower()
   
   x = 'this is lower case 123 !'
   x.upper()
   
   a = "This is"
   b = "code"
   c = a + ' ' + b
   c.split()
   
   str = '23, 34, 456, 637,4984,13,54'
   nums = []
   for s in str.split(','):
       n = int(s)
       nums.append(n)
   print(nums)
   ```
   
#### 5. Caesar Cipher
   ```python
   shift = 5
   message = "Hello world!"
   result = ""

   message = message.upper()
   for x in message:
       if x.isupper():
           num = ord(x)
           num += shift
           x = chr(num)
           if not x.isupper():
               num -= 26
               x = chr(num)

       result += x

   print(result)   
   ```

#### Homework
   1. Write a program to create a list of numbers that are between 1 and 200 and are divisible by 5 and 7
   1. Write a program which asks the user to enter a list of comma-delimited numbers and print the smallest and biggest numbers.
      - user must enter at least 5 numbers
      - for example, if the user enters `23, 34, 156, 637, 49, 13, 54, 33`, the output should be `The smallest number is 13, the biggest number is 637`
   1. Write a program to cipher text with Caesar Cipher:
      - Ask user to enter a positive shift value (1 - 25)
      - Ask user to enter any text
      - Cipher the text and print out the result
   1. Write a program to decode ciphered text with Caesar Cipher:
      - Ask user to enter a positive shift value (1 - 25)
      - Ask user to enter the ciphered text
      - Decipher the text and print out the result

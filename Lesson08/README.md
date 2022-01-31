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

   We test a condition in while loop.
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

#### 1. Generate random number:
   - [`randint(a, b)`](https://www.w3schools.com/python/ref_random_randint.asp) returns a random integer number N between `a` and `b` such that `a <= N <= b`.
   - [`randrange(stop)` or `randrange(start, stop[, step])`](https://www.w3schools.com/python/ref_random_randrange.asp) returns a random integer number N between `start` and `stop` such that `start <= N < stop`.
   
#### 2. Select a random element:
   - [choice(seq)](https://www.w3schools.com/python/ref_random_choice.asp) returns a randomly selected element from the specified sequence. The sequence can be a string, a range, a list, a tuple or any other kind of sequence.

#### 3. Notes:
   - `randrange(start, stop[, step])` is equivalent to `choice(range(start, stop, step))`, but doesn’t actually build a range object.
   - `randint(a, b)` is alias for `randrange(a, b+1)`.

#### 4. Code examples:
   ``` Python
   # Generate a random number between 1 and 10
   import random
   x = random.randint(1, 10)
   print(x)
   
   # Generate a random number between 1 and 9
   import random
   x = random.randrange(1, 10)
   print(x)
   ```
   
   ``` python
   # Randomly select a color from a color list
   colors = ["red", "yellow", "blue", "green", "orange", "purple", "white", "gray", "ruby", "azure"]
   c = random.choice(colors)
   print(c)
       
   # Randomly select an animal from an animal list
   animals = ['dog', 'cat', 'goldfish', 'lama', 'alpaca', 'camel', 'lion', 'tiger', 'panda', 'pig', 'cow']
   a = random.choice(animals)
   print(a)
   
   # Randomly select a character from a string
   str = 'Hello World!'
   s = random.choice(str)
   print(s)
   ```

#### 5. Sample Number Guessing Program
   ``` Python
   # Sample 1
    import random

    rnd_num = random.randint(1, 100)

    user_num = int(input('Please enter a number between 1 and 100: '))
    while True:
        if user_num == rnd_num:
            print("Matched!")
            break
        elif user_num > rnd_num:
            print("Your number is greater")
        else:
            print("Your number is smaller")

        user_num = int(input('Please enter a number between 1 and 100: '))

   ```
   
   ``` Python
   # Sample 2
    import random

    rnd_num = random.randint(1, 100)

    user_num = int(input('Please enter a number between 1 and 100: '))
    while user_num != rnd_num:
        if user_num > rnd_num:
            print("Your number is greater")
        else:
            print("Your number is smaller")

        user_num = int(input('Please enter a number between 1 and 100: '))

    print("Matched")

   ```
   
#### Homework
   1. Create a list of 12 numbers that are randomly generated between 1 and 2000
   1. Guessing colors
   1. Guessing animals
   1. Guessing even or odd numbers

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
   1. Write a program to create a list of 12 numbers. Each number in the list is randomly generated between 1 and 2000. **Please do not generate and print each number separately. You must add each number into the list and then print them out all together**. 
   1. Write a program to ask user to guess animal.
      - First, randomly select an animal from list `['dog', 'cat', 'goldfish', 'lama', 'alpaca', 'camel', 'lion', 'tiger', 'panda', 'pig', 'cow', 'duck']`
      - Then ask the user to guess the animal
      - User can guess up to 3 times. If the user guessed right, print `You guessed right`. If the user did not guess right for 3 times, print `You guessed wrong`
      - **Hint**: you may need to use loop and `break` statement (e.g., if the user guessed right, you need to break from the loop)
   1. Write a program to ask user to guess odd or even number.
      - First, randomly generate a number between 1 and 2000
      - Then ask the user to guess if the number is odd or even. 
      - User can guess up to 3 times. If the user guessed right, print `You guessed right`. If the user did not guess right for 3 times, print `You guessed wrong`
      - **Hint**: 
         - You may need to use loop and `break` statement (e.g., if the user guessed right, you need to break from the loop)
         - Think about how to determine the random number and the guessed number are even or odd and how to compare them
         - You can ask user to enter 0 for even number and 1 for odd number like the following code:
             `user_num = int(input("Please enter 0 for even number or enter 1 for odd number: "))`

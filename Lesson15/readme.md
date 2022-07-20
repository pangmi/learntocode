#### 1. Index of list:
   - We can access an item in a list with its index position in the list.
     ``` Python
     suits = ["clubs", "diamonds", "hearts", "spades"]
     print(suits[0])
     print(suits[1])
     ```
     
   - The `index()` method returns the position at the first occurrence of the specified item.
     ``` Python
     suits = ["clubs", "diamonds", "hearts", "spades"]
     print(suits.index("clubs"))
     print(suits.index("hearts"))
     ```
   
#### 2. Keep it going in a loop:
   ``` Python
   keep_going = True
   while keep_going:
       # 1. do some coding
       

       # 2. keep it going or not?
       answer = input("Enter 'c' to continue or 'q' to quit")
       if answer == 'c':
           keep_going = True
       else:
           keep_going = False
   ```
   
   ``` Python
   keep_going = True
   while keep_going:
       # 1. do some coding
       

       # 2. keep it going or not?
       answer = input("Enter 'c' to continue or 'q' to quit")
       keep_going = (answer == 'c')
   ```
   
   ``` Python
   keep_going = True
   while keep_going:
       # 1. do some coding
       

       # 2. keep it going or not?
       answer = input("Hit [Enter] to keep going, any key to exit: ")
       keep_going = (answer == "")
   ```
   
#### Homework
   1. Review and execute the code of [Deck of Cards](https://github.com/pangmi/learntocode/blob/main/Lesson15/Code/DeckOfCards.py)
   1. Read section ***1 Concepts and Vocabulary*** (Page 1 to 69) in book **Python Flash Cards**
   1. Read section ***2.1 - 2.4*** (Page 70 to 79) in book **Python Flash Cards**
   1. Review the code of [Roll 5 Dice](https://github.com/pangmi/learntocode/blob/main/Lesson15/Code/Roll5Dice.py); add code to in the program with the following change:
      - if any of the two dice are the same, print `Two of a kind!`
   1. Read section ***2.5 - 2.9*** (Page 80 to 89) in book **Python Flash Cards**
   1. Review the code of [Kaleidoscope](https://github.com/pangmi/learntocode/blob/main/Lesson15/Code/Kaleidoscope.py)

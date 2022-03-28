
#### 1. Windows Commands:
   - `dir`: Displays a list of files and subdirectories in a directory.
   - `cd`: Change directory. `cd \` brings you to the root directory. `cd ..` goes up one level.
   - `md/mkdir`: You can use `md` or `mkdir` to create a new directory. Examples:
      - `md newFolder`: Create a single folder named `newFolder`. 
      - `md folderOne folderTwo folderThree`: Create multiple folders in the current directory 
      - `md \folderOne\folderTwo\folderThree`: Create a new file path that doesn’t currently exist
   - `rd/rmdir`: You can use `rd` or `rmdir` to remove a directory. 
   - `copy`: Copies a specified file to a given location. 
   - `del`: Deletes a file or number of files. Examples:
      - `del someFile.txt`: Delete a specific file named *someFile.txt*
      - `del *.doc`: Delete files with a file type of *doc*. 
      - `del a*` or `del *a.*`: Delete files with names beginning with or ending with a specific letter
   - `move`: Rename a file, or move a file from one location to another. 
   - `cls`: Clears the screen.
   - **Change the Drive**:  type the drive's letter, followed by ":". For instance, if you wanted to change the drive to "D:", you can type `d:` and then press Enter on your keyboard.
   - You can always get help on the command with `/?`. For example: `copy /?`

#### 2. Be aware of infinite loop:

   ``` Python
   x = 1
   while x <= 20:
       square = x ** 2
       print(x, '->', square)
   ```

#### Homework
   1. Learn to use Windows commands with the following videos:
      - https://youtu.be/MBBWVgE0ewk
      - https://youtu.be/7ABkcHLdG_A
      - https://youtu.be/LHhPvq5R0hA
      - https://youtu.be/ODk8CoSLofA
      - https://youtu.be/hM7VPEatggE
      - https://youtu.be/hNrhLdo8qas
   1. Using Windows Command Prompt, do the following:
       - Create a folder under *C:* drive: `C:\Temp\Temp01\Temp02\Temp03`
       - In the above folder, create an empty text file named `MyTempFile01.txt`
       - In the same folder, copy the above file to `MyTempFile02.txt`
       - Display the files in the newly created folder

 

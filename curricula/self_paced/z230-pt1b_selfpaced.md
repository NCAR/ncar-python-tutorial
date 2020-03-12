Python 0-30 for Scientists
==========================

25. [python] Now, one big string isn't very useful, so let's 
   consider parsing the data file into a data structure we
   can use.  Change the `mysci.py` script to read:
   
   ```python
   # Initialize my data variable
   data = []
   
   # Read and parse the data file
   filename = "data/wxobs20170821.txt"
   with open(filename, 'r') as datafile:
   
       # Read the first three lines (header)
       for _ in range(3):
           datafile.readline()
       
       # Read and parse the rest of the file
       for line in datafile:
           data.append(line.split())
   
   # DEBUG
   for datum in data:
      print(datum)
   ```

We probably don't want our data in the form of one long string, so we're going to write a for-loop that reads the datafile line, by line, splitting the line along columns. 

So first initialize your data variable as an empty list. Lists are denoted by square brackets.

So as before, with, open, filename, for reading capabilities, but now we have 2 for loops. The first reads the header of the file which is the first 3 lines. For loops in Python have the line "for a in b" followed by a colon, then all lines within your loop are indented. In this first loop the the underscore variable is a placeholder, meaning the variable is never called within the loop - we are simply indicating to read the next line of the file by calling datafile.readline(), 3 times.

Then in the rest of the lines in your file, append your data list (so add a new element to the end of your existing list) with the data from that line, with that line split along white space. Other options for split are `/t ` for splitting along tabs, or `,` along commmas - depending on the format of your datafile. So now we have a list of lists for our data variable - a list of the data in each line for multiple lines.

When we print each datum in data, we'll see that each datum is a list of string values.

If anyone has any questions, speak up know. We just covered a lot of Python nuances in a very little bit a code!

26. [python] Now, we'll get the first, 10th, and last row in `data`.  
   Change the `DEBUG` section of our `mysci.py` script to:
   
   ```python
   # DEBUG
   print(data[0])
   print(data[9])
   print(data[-1])
   ```

To pull out the first, 10th, and last row from data, you can index your list by adding the number of your index in square brackets after the name of the list. Python is 0-indexed so data[0] refers to the first index, [-1] refers to the last index. Let's print this in our debugging section to see what this looks like.

27. [python] Now, we'll get the first 10 rows in `data`.  
   Change the `DEBUG` section of our `mysci.py` script to:
   
   ```python
   # DEBUG
   for datum in data[0:10]:
       print(datum)
   ```

Now we're going to introduce slice indexing. Using a colon between two index integers a and b, you get all indexes between a and b. See what happens when you type `data[:10]`, `data[0:10:2]`, and `data[slice(0,10,2)]`.  What's the difference?

28. [python] Exercise: Try getting the 5th, first 5, and every other *column*
   of rows `8` in `data`.
   
   Solution: Change the `DEBUG` section of the `mysci.py` script to:
   
   ```python
   # DEBUG
   print(data[8][4])
   print(data[8][:5])
   print(data[8][::2])
   ```
Now try changing your `DEBUG section` to print the 5th, first 5, and every other column of day from row 9 in `data`. To do this we will have to understand nested list indexing, where the first index determines the row, and the second determines the element from that row. Also try printing `data[5:8][4]`, why doesn't this work?

29. [git] Clean up the file (remove `DEBUG` section), stage the changes, and
   commit. (i.e., `git add mysci.py` and `git commit -m "Parsing file"`)

Let's clean up the file, stage our changes, and commit.

30. [python] Can you remember which column is which?  Is time the first
   column or the second?  Which column is the temperature?
   
   Each column is a time-series of data.  We would ideally like each
   time-series easily accessible, which is *not* the case when `data`
   is row-column ordered (like it currently is).  (Remember what happens
   when you try to do something like `data[:][4]`!)
   
   Let's get our data into a more convenient named-column format.
   Change `mysci.py` to the following:

   ```python
   # Initialize my data variable
   data = {'date': [],
           'time': [],
           'tempout': []}
   
   # Read and parse the data file
   filename = "data/wxobs20170821.txt"
   with open(filename, 'r') as datafile:
   
       # Read the first three lines (header)
       for _ in range(3):
           datafile.readline()
       
       # Read and parse the rest of the file
       for line in datafile:
           split_line = line.split()
           data['date'].append(split_line[0])
           data['time'].append(split_line[1])
           data['tempout'].append(split_line[2])
   
   # DEBUG
   print(data['time'])
   ```

You probably don't remember which column is which?  Is time the first column or the second?  Which column is the temperature?
   
Each column is a time-series of data.  We would ideally like each time-series easily accessible, which is *not* the case when `data` is row-column ordered (like it currently is).  (Remember what happens when you try to do something like `data[:][4]`!)
   
Let's get our data into a more convenient named-column format. To do that we have to change `mysci.py` to the following:

First we'll initialize a dictionary, indicated by the curly brackets. This is like our list of lists, but we now have 'keys', rather than positions, that point to lists for specific data variables, each element being a string. We're going to grab date, time, and temperature data, which are currently all themselves empty lists that we will fill with a similar for loop as before.

31. [git] Clean up (remove `DEBUG` section), stage, and commit
   (`git commit -m "Parsing select time-series"`)

Again let's clean up, stage, and commit.
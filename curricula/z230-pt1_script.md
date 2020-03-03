Python 0-30 for Scientists
==========================

Welcome to the Python 0 to 30 for Scientists tutorial. Today you will learn how to write Python code using Python best practices. This will be done live so that you can see how each step of using Python fits together, without us skipping over steps that are fundamental to using Python outside of this tutorial. We will develop scripts together and we will be using git and GitHub to save and organize our work after each lesson, or natural stopping point. My hope is that at the end of this tutorial you will have a grasp of how to begin building your own library of Python tools for your analysis workflows.


Why Python?
-----------
You're all here because you want to learn to use Python for your data analysis and visualizations. Python can be compared to other interpreted object-oriented languages, but is especially great because it is free and open source! 

Being open source means that when people have identified gaps in Python's abilitlies, they have built libraries of code that make those tasks easier. There are libraries specifically for improved mathmatics, statistics, plotting, etc -  collections of code bases that you can pull in and use without having to start from scratch. Perhaps you are familiar with importing libraries into your workflow already, I know in IDL often people pass around files that contain unique user-written IDL functions for this same purpose of reducing redundant work between scientists. Matlab has packages that you can pay extra money to install and use. Again Python is free, so when there are improvements to be made, you can take advantage of other people's efforts to make these improvements.

There are many many different libraries of code you can import and use. We are only going to teach you the most commonly used libraries, and one at a time, to reduce any confusion you may have about what each library offers.


Requirements & Installation
--------------------------

But first, let'd double check - Everyone should have conda or miniconda installed on their linux or mac OS at this point. If you have an old version of conda installed, update it. Raise your hand if you had any trouble with this.


Outline - Part 1 - First Python Script
--------------------------------------

Okay, let's build our first Python script. I will teach you about syntax and the reasoning behind why things are done the way they are as we go.

1. [bash] Create a directory:

   ```bash
   $ mkdir mysci
   ```

The first thing we have to do is create a directory to store our work. So open a terminal and type "mkdir". Let's call it "mysci".
   
2. [bash] Go into the directory:

   ```bash
   $ cd mysci
   ```
"cd" into your new directory.

3. [conda] Create a virtual environment for this project:

   ```bash
   $ conda create --name mysci python
   ```

We are going to use conda to create a virtual environment for this project. Type "conda create --name", the name of your project, here that is "mysci," and then specify that we are using python. 

A conda environment is a directory that contains a collection of packages or libraries that you would like installed and accessible for this work. It is a good idea to create new environments for different projects in this way because since Python is open source, new versions of tools you may use become available. You would hate for your script to no longer work because, for example, a function you called before now has slightly different input arguments. This is a way of guaranteeing that your script will use the same versions of packages and libraries and should run the same as you expect it to.

4. [git] Make the directory a git repository:

   ```bash
   $ git init .
   ```
   
We are going to make a git repository of our "mysci" directory. Does everyone has a github account and git installed? **If not, how to help** Git is a program that tracks changes made to files. This makes it easy to maintain access to multiple versions of your code as you improve it, and revert your code back to a previous version if you've made any mistakes. I will show you how to do these as we need to.
   
5. [bash] Create a data directory:

   ```bash
   $ mkdir data
   ```

And we'll make a directory for our data.

6. [bash] Go into the data directory:

   ```bash
   $ cd data
   ```
Let's "cd" into the data directory. 

7. [bash] Download sample data:

   ```bash
   $ curl -O https://sundowner.colorado.edu/weather/atoc8/wxobs20170821.txt
   ```

And download data from the CU Boulder weather station.

This weather station is a Davis Instruments wireless Vantage Pro2 located on the CU-Boulder east campus at the SEEC building (40.01 N, 05.24 W, 5250 ft elevation). The station is monitored by the Atmospheric and Oceanic Sciences (ATOC) department and is part of the larger University of Colorado ATOC Weather Network.
   
8. [git] Add the file to the *git staging area*:

   ```bash
   $ git add wxobs20170821.txt
   ```
   
By adding this datafile to our directory, we have made a change that is not yet reflected in our Github repository. Type "git add" and then the name of the altered file to stage your change.
   
9. [git] Commit the file to the *git repository*:

   ```bash
   $ git commit -m "Adding sample data file"
   ```
   
 And then with "git commit" we update our repository by all the changes we staged, in this case just one file. Let's take a look at our repositories to check this.

10. [git] Look at the git logs:

   ```bash
   $ git log
   ```
   
If you type "git log" you will show a log of the commits, or changes made to your repository.

11. [bash] Go back to the top-level directory:

   ```bash
   $ cd ..
   ```
   
"cd" up a level.

12. [bash] Create a blank Python script:

   ```bash
   $ touch mysci.py
   ```

And now that we've set up our workspace, we'll create a blank Python script, called "mysci.py"

13. [python] Edit the `mysci.py` file:

   ```python
   print("Hello, world!")
   ```

Our classic first command will be to print "Hello World".

14. [python] Try testing the script:

   ```bash
   $ python mysci.py
   ```
   
And let's test it with "python mysci.py" Yay!  You've just created your first Python script. We'll repeat this step to test our script regularly.
   
15. [python] Now delete the `print("Hello, world!")` line
   from the `mysci.py` file, and let's read our sample data file.
   Change the `mysci.py` script to read:
   
   ```python
   # Read the data file
   filename = "data/wxobs20170821.txt"
   with open(filename, 'r') as datafile:
       data = datafile.read()
   
   # DEBUG
   print(data)
   ```
You probably won't need to run your Hello World script again, so let's delete it and start over with something more useful. Let's open the .txt file we downloaded earlier. First we'll create a variable for our file name, which is a string - this can be in single or double quotes. Then type "with open" and in parenthesis your filename, 'r' indicating you want to open this file to 'read' it, and "as datafile:" on the next line type "data = datafile.read()" With these two lines of code you are saying that with the file opened, you'd like to read it. 

The "with" statement is a context manager that procides clean-up and assures that the file is automatically closed after you've read it. Other input arguments for "open" include "w", for example, if you wanted to write to the file.

And to test that this worked. We'll print "data"

Let's add some comments to our script to parse out the two sections. Comments in Python are indicated with a hash.

And execute with "python mysci.py"

16. [python] What did we just see?  What is the `data` object?  What
   type is `data`?  How do we find out?  Add the following to the
   `DEBUG` section of our script:
   
   ```python
   print(type(data))
   ```

What did we just see?  What is the `data` object?  In the 'DEBUG' section of our script let's find out the type of our data object. Object types refer to 'float' 'integer' 'string' or other types that you can create. Python is a dynamically typed language, which means you don't have to explicitly specify the datatype when you name a variable, Python will automatically figure it out by the nature of the data.

17. [python] Try testing the script, again.

And let's test it with "python mysci.py" We see that `data` is a string.
   
18. [git] Now, clean up the script by removing the `DEBUG`
   section, before we commit this to git.

Remove the 'debug' section to clean up the script.

19. [git] Let's check the status of our git repository

   ```bash
   $ git status
   ```
   
Let's check the status of our git repository. Note what files have been changed in the repository.

20. [git] Stage these changes:

   ```bash
   $ git add mysci.py
   ```

As before, let's stage the changes to our file with "git add"

21. [git] Let's check the status of our git repository,
   again.  What's different from the last time we 
   checked the status?

Again with "git status" let's now check the status of our repository. What is different since our last status check?

22. [git] Commit these changes:

   ```bash
   $ git commit -m "Adding script file"
   ```
Commit the changes with "git commit -m for message, and the message "Adding script file"

23. [git] Let's check the status of our git repository,
   now.  It should tell you that there are no changes
   made to your repository (i.e., your repository is
   up-to-date with the state of the code in your
   directory).'

Again with "git status" let's now check the status of our repository.

24. [git] Look at the git logs, again:

   ```bash
   $ git log
   ```
   
   **NOTE:** Explain the changes in the logs.
   Introduce simplified logs with the `--oneline` option.
When we look at the git logs, we'll notice some changes ...

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
   
   **NOTE:** Introduces `[index]` (i.e., `getitem`) notation, zero-based
   indexing, and negative indexes.  Also, note that each row is a `list`!

1. [python] Now, we'll get the first 10 rows in `data`.  
   Change the `DEBUG` section of our `mysci.py` script to:
   
   ```python
   # DEBUG
   for datum in data[0:10]:
       print(datum)
   ```
   
   **NOTE:** Introduces `slice` indexing.  Have students see what happens
   with `data[:10]`, `data[0:10:2]`, and `data[slice(0,10,2)]`.  What's the
   difference?  Explain `slice`.

1. [python] Exercise: Try getting the 5th, first 5, and every other *column*
   of rows `8` in `data`.
   
   Solution: Change the `DEBUG` section of the `mysci.py` script to:
   
   ```python
   # DEBUG
   print(data[8][4])
   print(data[8][:5])
   print(data[8][::2])
   ```
   
   **NOTE:** Introduces nested-`list` indexing.  Note that when printing
   strings to the screen, the quotation marks are not displayed!  (They
   are only displayed when you are printing the list containing the strings.)
   Also, what happens when you try something like `data[5:8][4]`?  You should
   get an error!  Why?

1. [git] Clean up the file (remove `DEBUG` section), stage the changes, and
   commit. (i.e., `git add mysci.py` and `git commit -m "Parsing file"`)

1. [python] Can you remember which column is which?  Is time the first
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
   
   **NOTE:** Introduces `dict` and `{}` short-hand; talk about
   `list` vs `dict`, why use one over another?  Advantages and
   disadvantages of `dict`s and `lists`.  Note that the output
   is a `list` of `str`s.

1. [git] Clean up (remove `DEBUG` section), stage, and commit
   (`git commit -m "Parsing select time-series"`)

1. [python] Now it's easy to get the time-series information
   for each column that we are interested in grabbing, and we
   can get each column by name.  However, everything read from
   the text file is a `str`.  What if we want to do math on this
   data, then we need it to be a different data type!
   
   So, let's convert the `tempout` time-series to be a `float`
   by changing the line:
   
   ```python
           data['tempout'].append(split_line[2])   
   ```
   
   to:
   
   ```python
           data['tempout'].append(float(split_line[2]))
   ```
   
   **NOTE:** Should also introduce `int`.

1. [python] Add a `DEBUG` section at the end and see what
   `data['tempout']` now looks like.  Do you see a difference?
   It should now be a `list` of `float`s.

1. [git] Clean up (remove `DEBUG` section), stage, and commit
   (`git commit -m "Converting tempout to floats"`)

1. [python] This seems great, so far!  But what if we want to
   read more columns to our data later?  We will have to change
   the initialization of the `data` variable (at the top of 
   `mysci.py`) *and* we will have to add the appropriate line
   in the "read and parse" section.  Essentially, that means
   you need to maintain 2 parts of the code and make sure that
   both remain consistent with each other.
   
   This is generally not good practice.  Ideally, you want to
   be able to change only 1 part of the code and know that
   the rest of the code will remain consistent.  So, let's fix
   this.
   
   Change `mysci.py` to:
   
   ```python
   # Column names and column indices to read
   columns = {'date': 0, 'time': 1, 'tempout': 2}

   # Data types for each column (only if non-string)
   types = {'tempout': float}

   # Initialize my data variable
   data = {}
   for column in columns:
       data[column] = []

   # Read and parse the data file
   filename = "data/wxobs20170821.txt"
   with open(filename, 'r') as datafile:

       # Read the first three lines (header)
       for _ in range(3):
           datafile.readline()

       # Read and parse the rest of the file
       for line in datafile:
           split_line = line.split()
           for column in columns:
               i = columns[column]
               t = types.get(column, str)
               value = t(split_line[i])
               data[column].append(value)

   # DEBUG
   print(data['tempout'])
   ```
   
   Now we only need to modify the `columns` variable
   to indicate which columns of the data file to read
   and the `types` variable to indicate to what type to
   convert the data.
   
   **NOTE:** Introduces passing types/functions as arguments
   (or holding pointers to types/functions in a variable,
   namely the `types` variable), looping over `dict`s, adding
   key-value pairs to a `dict` via assignment, and the
   `dict.get()` method (to avoid key-not-found errors)

1. [git] Clean up (remove `DEBUG` section), stage, and commit
   (`git commit -m "Refactoring data parsing code"`)

1. [python] Okay, now that we've read the data in a way that
   is easy to modify later, let's actually do something with
   the data.
   
   Let's compute the *wind chill* factor.  We've read the
   temperature data into the `tempout` variable, but we need
   to read the `windspeed` variable from column `7`.  So,
   let's modify the `columns` variable to read:
   
   ```python
   columns = {'date': 0, 'time': 1, 'tempout': 2, 'windspeed': 7}
   ```
   
   and modify the `types` variable to be:
   
   ```python
   types = {'tempout': float, 'windspeed': float}
   ```
   
1. [git] Great!  Let's save this in our git repo.  Stage and
   commit (`git commit -m "Reading windspeed as well"`).

1. [python] Now, let's write our first function to compute
   the wind chill factor.  We'll add this function to the
   bottom of the file.
   
   ```python
   # Compute the wind chill temperature
   def compute_windchill(temp, windspeed):
       v16 = windspeed ** 0.16
       return 35.74 + 0.6215*temp - 35.75*v16 + 0.4275*temp*v16
   ```
   
   **NOTE:** Introduces `def` for functions and math operators
   (`+`, `-`, `*`, and `**`).  Also mention `/` for division.
   
   And then let's compute a new list with `windchill` data at
   the bottom of `mysci.py`:
   
   ```python
   # Let's actually compute the wind chill factor
   windchill = []
   for temp, windspeed in zip(data['temp'], data['windspeed']):
       windchill.append(compute_windchill(temp, windspeed))
   ```
   
   **NOTE:** Introduces `zip` and automatic "unraveling" of a
   `tuple`... Introduces `tuple`s implicitly, so should cover it.
   Take a look at `zip([1,2], [3,4,5])`.  What is the result?

   And finally, we'll add a typical `DEBUG` section to see the
   results:
   
   ```python
   # DEBUG
   print(windchill)
   ```
   
   Test this out and see the results.
   
1. [git] Clean up, stage, and commit (`git commit -m "Compute wind chill factor"`)

1. [python] Now, the wind chill factor is actually in the data file,
   so we can read it from the file and compare that value to our computed
   values.  To do this, we need to read the `windchill` column as a `float`:
   
   ```python
   columns = {'date': 0, 'time': 1, 'tempout': 2, 'windspeed': 7,
              'windchill': 12}
   ```
   
   **NOTE:** Introduces line continuation indentation (I think?)
   
   and
   
   ```python
   types = {'tempout': float, 'windspeed': float, 'windchill': float}
   ```
   
   Then, let's add a `DEBUG` section at the end to compare the two
   different values (from `data` and computed by our function):
   
   ```python
   # DEBUG
   for wc_data, wc_comp in zip(data['windchill'], windchill):
       print(f'{wc_data:.5f}   {wc_comp:.5f}   {wc_data - wc_comp:.5f}')
   ```
   
   **NOTE:** Introduces f-strings with `float` formatting.  Point people 
   to different kinds of formatting that can be done in f-strings.
   
   Test the results.  What do you see?  Our computation isn't very good
   is it?


1. [git] Clean up, stage, and commit (`git commit -m "Compare wind chill factors"`)

1. [python] Now, let's format the output so that it's easy to understand and
   rename this script to something indicative of what it actually does.
   
   To the end of the file, let's add:
   
   ```python
   # Output comparison of data
   print('                ORIGINAL  COMPUTED')
   print(' DATE    TIME  WINDCHILL WINDCHILL DIFFERENCE')
   print('------- ------ --------- --------- ----------')
   for date, time, wc_orig, wc_comp in zip(data['date'], data['time'], data['windchill'], windchill):
       print(f'{date} {time:>6} {wc_orig:9.6f} {wc_comp:9.6f} {wc_orig-wc_comp:10.6f}')
   ```
   
   **NOTE:** Introduces f-string formatting of strings, `zip` with more than 2 arguments
   and more `float` formating options.
   
   You now have your first complete Python script!  Let's write another...
   
1. [git] DON'T CLEAN UP!  Just stage and commit
   (`git commit -m "Output formatting comparison data"`)

1. [git] Let's rename this script to something meaningful.

   ```bash
   $ git mv mysci.py windchillcomp.py
   $ git commit -m "Renaming first script"
   ```

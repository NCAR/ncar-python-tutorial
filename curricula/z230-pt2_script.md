Python 0-30
===========

Outline - Part 2 - First Python Package
---------------------------------------

Welcome back everyone. Today we are going to continue learning Python, introducing the concepts of packages which will make your complicated analysis methods much much easier.

1. [bash] Let's make a copy of our first script.
   
   ```bash
   $ cp windchillcomp.py heatindexcomp.py
   ```
First let's make a copy of our first script, but with the name heatindexcomp.py. You guessed it today we will compute heat index.

2. [git] And add and commit this new file.
   (`git commit -m "Copying first script to start second"`)

Let's add and commit this file,

3. [python] Now, we want to compute the Heat Index, which we
   will do by replacing the `compute_windchill` function with
   a `compute_heatindex` function:
   
   ```python
   # Compute the heat index
   def compute_heatindex(temp, hum):
       T = temp
       H = hum / 100
       HI = (-42.379 + 2.04901523*T + 10.14333127*H -
             0.22475541*T*H - 6.83783e-3*T**2 - 5.481717e-2*H**2 +
             1.22874e-3*T**2*H + 8.5282e-4*T*H**2 -
             1.99e-6*T**2*H**2)
       return HI
   ```
   
   Then, we need to change the columns we read from the data file:
   
   ```python
   columns = {'date': 0, 'time': 1, 'tempout': 2, 'humout': 5,
              'heatindex': 13}
   ```
   
   and
   
   ```python
    types = {'tempout': float, 'humout': float, 'heatindex': float}
   ```

   and then we update the rest of the script to match
   
   ```python
   # Let's actually compute the heat index
   heatindex = []
   for temp, hum in zip(data['tempout'], data['humout']):
       heatindex.append(compute_heatindex(temp, hum))

   # Output comparison of data
   print('                ORIGINAL  COMPUTED')
   print(' DATE    TIME  HEAT INDX HEAT INDX DIFFERENCE')
   print('------- ------ --------- --------- ----------')
   for date, time, hi_orig, hi_comp in zip(data['date'], data['time'], data['heatindex'], heatindex):
       print(f'{date} {time:>6} {hi_orig:9.6f} {hi_comp:9.6f} {hi_orig-hi_comp:10.6f}')
   ```
   
   Let's run this script and see the results.
   
   **NOTE:** This computation is not too bad!  Pretty close.

Change the core calculation, the columns we are extracting, calculate it, and pring the results.

Maybe change this to dew point temperature so that we introduce numpy.

4. [git] Stage and commit this new script.
   (`git commit -m "Updating new heat index script"`)

Stage and commit.

5. [bash] Now, we have two scripts that do very similar things.
   In fact, all of the data reading and parsing code is duplicated!
   And the output is similarly formatted, too.  So, let's fix this
   by creating a *module*.
   
   Create a new file called `readdata.py`:
   
   ```python
   def read_data(columns, types={}, filename="data/wxobs20170821.txt"):
       """
       Read data from CU Boulder Weather Station data file
       
       Parameters:
           columns: A dictionary of column names mapping to column indices
           types: A dictionary of column names mapping to types to which
               to convert each column of data
           filename: The string path pointing to the CU Boulder Weather
               Station data file
       """

       # Initialize my data variable
       data = {}
       for column in columns:
           data[column] = []

       # Read and parse the data file
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

       return data
   ```
   
   **NOTE:** Introduces keyword arguments to functions and
   docstrings!  Might also want to mention what `help(read_data)`
   will do with the docstring.

So we've moved our common code, the function for reading the file, from both the windchill and heatindex file to its own file.

And we've made some changes to the function, most notably we've introduced keyword arguments - when you see types={} it means that types is presumed to be an empty dictionary if you don't specify it (and so you don't have to specify it every time you call the function when this keyword isn't relevant). Similarly we've specified a filename that is used as long as the user doesn't specify a different file. Let's them be in any order.

We have also added docstrings to the function. The "Read data from CU Boulder Weather Station data file" purpose of the function and list of parameters are standard information included in a docstring.

6. [git] Stage and commit this new file
   (`git commit -m "Adding new readdata module"`)

7. [python] Now, let's amend our two Python scripts by *first* deleting
   the equivalent code in them.
   
   Then, add the following import statement to the top of each script:
   
   ```python
   from readdata import read_data   
   ```
   
   And finally, after the initializations of the `columns` and `types`
   variables, replace the deleted code with a function call.
   
   ```python
   # Read data from file
   data = read_data(columns, types=types)
   ```
   
   Test out both of these scripts to make sure they still work!
   
   **NOTE:** Introduces *modules*, the `import` statement
   
In python you can call up functionality from scripts outside of your active script using the 'import' statement. Here we import our read_data function from the readdata file. And now we can call up the function from these scripts.

8. [git] Do a `git status` now.  Do you notice something new?  Running
   our new scripts created the `__pycache__` directory.  We *don't*
   want to add this directory to our project repository, so before we
   commit anything, let's tell git to ignore it!
   
   Create a new file (in the top-level directory of your project) called
   `.gitignore` with the following contents:
   
   ```text
   __pycache__/
   ```
   
   Do another `git status`.  What do you see?
   
   Now, instead of `__pycache__` being listed as "untracked", you see
   `.gitignore` being listed as "untracked"...and no mention of `__pycache__`.
   
   So, let's stage and commit out new `.gitignore` file.
   (`git commit -m "Ignoring pycache"`)
   
   Finally, do another `git status` to see where we are at.  Notice that
   the edits we made to our two scripts have still not been committed to
   the project repository!  Because we never staged them before our last
   commit.
   
When you run a python program the interpreter compiles your scripts to bytecode and stores them in a cache, making your scripts run a little faster. This is a simplification, but you as a user can for the most part ignore this new folder. If you change or delete your scripts they will be recompiled and reappear in this folder. Created when you use an import.

9. [git] Stage *both files* and commit all new changes in one commit
   (`git commit -m "Refactor scripts to use new module"`)

10. [python] We still have some duplicated code in our scripts.  Namely, the
   final output code is mostly the same.  All we need to do is functionalize
   this code.
   
   Let's create another module file called `printing.py` with the following
   contents:
   
   ```python
   def print_comparison(name, date, time, original_data, computed_data):
       """
       Print a comparison of two timeseries (original and computed)

       Parameters:
           name: A string name for the data being compared. (Limited
               to 9 characters in length)
           date: List of strings representing the dates for each data element
           time: List of strings representing time of day for each data element
           original_data: List of original data (floats)
           computed_data: List of computed data (floats)
       """

       print(f'                ORIGINAL  COMPUTED')
       print(f' DATE    TIME  {name.upper():>9} {name.upper():>9} DIFFERENCE')
       print(f'------- ------ --------- --------- ----------')
       for date, time, orig, comp in zip(date, time, original_data, computed_data):
           print(f'{date} {time:>6} {orig:9.6f} {comp:9.6f} {orig-comp:10.6f}')
   ```

   **NOTE:** Introduces `str.upper()` ...mention more `str` methods.
   
   Exercise: Edit the two scripts to use this new module.  Test your results.
   
   Solution: Add the `from printing import print_comparison` line to the top
   of each script, and then replace the printing output section at the bottom
   of each script with:
   
   ```python
   print_comparison('WINDCHILL', data['date'], data['time'], data['windchill'], windchill)
   ```
   
   and
   
   ```python
   print_comparison('HEAT INDX', data['date'], data['time'], data['heatindex'], heatindex)
   ```
string.upper() capitalzes all lower case letters in a string

11. [git] Stage all changes and commit (`git commit -m "Creating printing module"`)

12. [python] We now have 2 different modules related to the same project.  We could
   have put all of these new functions into the same module, but it is best practice
   to separate different functions into different modules depending upon the kind of
   functionality they represent.  In this case, we've separated out the concepts of
   "data input" and "printing output" into different modules.
   
   We could also do the same thing with the computation functions that we've already
   created, `compute_windchill` and `compute_heatindex`.
   
   Exercise: Let's move these functions into a new module called `computation.py`, 
   and modify the scripts to use this new module.  Remember to add docstrings!
   
   Solution: I did the following:
   
   ```python
   def compute_windchill(temp, windspeed):
       """
       Compute the wind chill factor given the temperature and wind speed

       NOTE: This computation is valid only for temperatures between
       -45F and +45F and for wind speeds between 3 mph and 60 mph.

       Parameters:
           temp: The temperature in units of F
           windspeed: The wind speed in units of mph
       """

       v16 = windspeed ** 0.16
       return 35.74 + 0.6215*temp - 35.75*v16 + 0.4275*temp*v16


   def compute_heatindex(temp, hum):
       """
       Compute the heat index given the temperature and the humidity

       Parameters:
           temp: The temperature in units of F
           hum: The relative humitidy in units of %
       """

       T = temp
       H = hum / 100
       HI = (-42.379 + 2.04901523*T + 10.14333127*H -
             0.22475541*T*H - 6.83783e-3*T**2 - 5.481717e-2*H**2 +
             1.22874e-3*T**2*H + 8.5282e-4*T*H**2 -
             1.99e-6*T**2*H**2)
       return HI
   ```
   
   And then modified the scripts accordingly.

13. [git] Stage and commit everything (`git commit -m "Creating computation module"`)

14. [python] Now, we've got quite a few Python files in our main directory.
   Which ones are scripts?  Which ones are modules meant to be imported?
   
   Typically, we group all of the modules meant for import only into another
   directory called a *package*.  A *package* is a directory with a `__init__.py`
   file inside it.
   
   So, let's create a new directory called `mysci` and create an empty file in it
   called `__init__.py`:
   
   ```bash
   $ mkdir mysci
   $ cd mysci
   $ touch __init__.py
   $ cd ..
   ```
   
   Then, let's move our 3 modules into this package:
   
   ```bash
   $ git mv readdata.py mysci/
   $ git mv printing.py mysci/
   $ git mv computation.py mysci/
   ```
   
   Then, let's modify the import statements at the top of our two scripts so
   that the modules are automatically imported from the new package:
   
   ```python
   from mysci.readdata import read_data
   from mysci.printing import print_comparison
   from mysci.computation import compute_heatindex
   ```
   
   **NOTE:** Obviously introduces packages.  Should also talk about the
   fact that the `__init__.py` file is run when the package is imported.

15. [git] Stage everything (don't forget the `__init__.py` file!) and
   commit (`git commit -m "Creating mysci package"`)
   
   **NOTE:** Our commits are getting bigger, but that's okay.  Each commit
   corresponds to a *single* (conceptually) change to the codebase.
   
   With this last change, our project should look like this (ignoring the
   `__pycache__` directories:
   
   ```text
   mysci/
   
       data/
           wxobs20170821.txt
           
       mysci/
           __init__.py
           readdata.py
           printing.py
           computation.py
           
       heatindexcomp.py
       windchillcomp.py
   ```

16. [python] Let's take a brief aside and look at the use of the computation
   functions in our scripts.  In the case of the wind chill factor computation,
   it looks like this:
   
   ```python
   windchill = []
   for temp, windspeed in zip(data['tempout'], data['windspeed']):
       windchill.append(compute_windchill(temp, windspeed))
   ```
   
   This divides the initialization of the `windchill` variable as an empty `list`
   from the "filling" of that `list` with computed values.
   
   Python gives you some shortcuts to doing this via a concept called 
   "comprehensions", which are ways of initializing containers (`list`s,
   `dict`s, etc.) with an *internal loop*.  For example, we could have
   written the previous 3 lines in the form of a "one-liner" like so:
   
   ```python
   windchill = [compute_windchill(t, w) for t, w in zip(data['tempout'], data['windspeed'])]
   ```
   
   This is a *list comprehension*, and it initializes the entire list with the
   computed contents, rather than initializing an empy list and appending values
   to it after the fact.  Computationally, this is actually *more efficient*.
   
   Exercise: Use list comprehensions to make the computation steps in both of
   our scripts one-liners.
   
   **NOTE:** Introduces list comprehensions.  Should also mention dict comprehensions.
   Should also mention *conditional* comprehensions (i.e., `for ... in ... if` statements)

17. [git] Stage and commit changes (`git commit -m "Using list comprehensions"`)

18. [bash] [bash] Let's make a copy of our first script.
   
   ```bash
   $ cp windchillcomp.py dewpointtempcomp.py
   ```

19. [git] And add and commit this new file.
   (`git commit -m "Copying first script to start a third"`)

20. Write function for computing dew point and change columns and types dictionaries 
    ```python
    import math
    
    #columns names and column indices to read
    columns = {'date':0 , 'time':1, 'tempout':2, 'humout':5, 'dewpt':6}

    #data types for each column (only if non-string)
    types = {'tempout':float, 'humout':float, 'dewpt':float}

    def compute_dewpoint(temp, rel_humidity):
        T = (temp - 32) * 5 / 9 #F to C   #have a function for this
        H = rel_humidity / 100
        a = 6.112 #mbar
        b = 18.678
        c = 257.14 #degC
        gamma = math.log(H) + (b * T) / (c + T)
        tdp = c * gamma / (b - gamma)
        tdp_F = 9 / 5 * tdp + 32
        return tdp_F
        ```

21. add and commit
    git commit -m "  Computed dew point temperature"

22. refactor to mysci.compute and add docstring
def compute_dewpoint(temp, hum):
        """
        Compute the dew point temperature given the temperature and humidity

        Parameters:
                temp: The temperature in units of F
                humL: The relative humidity in units of %
        """

        T = (temp - 32) * 5 / 9 #F to C
        H = rel_humidity / 100
        a = 6.112 #mbar
        b = 18.678
        c = 257.14 #degC

        gamma = numpy.log(H) + (b * T) / (c + T)
        tdp = c * gamma / (b - gamma)
        tdp_F = 9 / 5 * tdp + 32
        return tdp_F

#calculate windchill
dewpointtemp = [compute_dewpoint(t, h) for t, h in zip(data['tempout'], data['humout'])]

23. add and commit
    commit -m "Moved dew point fx to computation.py"


#-------------------------------------------------

24. move to numpy
    
    Conda install numpy
    And use numpy so you can pass in a list without having to do for loops and zip
    convert all 3 scripts to work well with numpy

25. plot time vs dpt, time vs humidity, etc in matplotlib
    conda install matplotlib    
    
26.     contours of dewpoint, axis of temperature and humidity.
    but they'd need mapping of dewpoint to 2d (or use numpy to generate a new table of temp and humiity that we compute on)

27. get a different data set - satellite data LENS data
        take something from the geocat examples (great way to show gallery to recovering NCL users)
Python 0-30 for Scientists
==========================

32. [python] Now it's easy to get the time-series information
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

Now it's easy to get the time-series information for each column that we are interested in grabbing, and we can get each column by name.  However, everything read from the text file is a string.  If we want to do math on this data, then we need it to be a different data type! So, let's convert the `tempout` time-series to be a `float` by changing each element into a float before we append it to the list for our temperature data. You could also change it 'int', which will round the values down to the closest full integer.

33. [python] Add a `DEBUG` section at the end and see what
   `data['tempout']` now looks like.  Do you see a difference?
   It should now be a `list` of `float`s.

Print `data['tempout']` in a `DEBUG` section of your code to show the difference between a list of floats and our previous list of strings.

34. [git] Clean up (remove `DEBUG` section), stage, and commit
   (`git commit -m "Converting tempout to floats"`)

Clean up, stage and commit.

35. [python] This seems great, so far!  But what if we want to
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

This seems great, so far!  But what if we want to read more columns to our data later?  We will have to change the initialization of the `data` variable (at the top of `mysci.py`) *and* we will have to add the appropriate line in the "read and parse" section.  Essentially, that means you need to maintain 2 parts of the code and make sure that both remain consistent with each other.
   
This is generally not good practice.  Ideally, you want to be able to change only 1 part of the code and know that the rest of the code will remain consistent.  So, let's fix this by using a `columns` variable.

 Now we only need to modify the `columns` variable to indicate which columns of the data file to read and the `types` variable to indicate to what type to convert the data.

 In this step we have demonstrated passing types as an argument, looping over a dictionary, adding key-value pairs to a dictionary via assignment, and the dict.get() method.

36. [git] Clean up (remove `DEBUG` section), stage, and commit
   (`git commit -m "Refactoring data parsing code"`)

Clean up, stage and commit.

37. [python] Okay, now that we've read the data in a way that
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

Okay, now that we've read the data in a way that is easy to modify later, let's actually do something withmthe data. Let's compute the *wind chill* factor.  We've read the temperature data into the `tempout` variable, but we need to modify the `columns` variable to include reading `windspeed` variable from column `7`

38. [git] Great!  Let's save this in our git repo.  Stage and
   commit (`git commit -m "Reading windspeed as well"`).

Clean up, stage and commit.

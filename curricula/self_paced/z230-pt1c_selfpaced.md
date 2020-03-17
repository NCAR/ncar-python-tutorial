Python 0-30 for Scientists
==========================

This is intended to pick off right where part 1b left off- you had just commited your new script that reads the file, saving the variables of date, time, and tempout in a data dictionary.

Part 1c - First Python Script Cont
--------------------------------------
33. [python] Now it's easy to get the time-series information
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

The `float` datatype refers to floating point real values - the datatype of any numbers with values after a decimal point. You could also change the datatype to `int`, which will round the values down to the closest full integer.

34. [python] Add a `DEBUG` section at the end and see what
   `data['tempout']` now looks like.  Do you see a difference?
   It should now be a `list` of `float`s.

35. [git] Clean up (remove `DEBUG` section), stage, and commit
   (`git commit -m "Converting tempout to floats"`)

36. [python] This seems great, so far!  But what if you want to
   read more columns to our data later?  You would have to change
   the initialization of the `data` variable (at the top of 
   `mysci.py`) *and* have to add the appropriate line
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
You have now created a `columns` dictionary that points each data variable to its column-index. And a `types` dictionary, that indicates what type to convert the data when necessary. When you want new variables pulled out of the datafile, change these two variables.

Initializing the `data` dictionary now includes a `for` loop, where for each variable specified in `columns` that key is initialized pointing to an empty list. This is the first time you have looped over a `dict` and added key-value pairs toa `dict` via assignment.

When reading and parsing the file, you created your first nested `for` loop. For every line of the datafile, split that line - and then for every desired variable in the `columns` dictionary (`date`, `time`, `tempout`): grab the datum from the current split line with the specified index (`0`, `1`, `2`), use the `dict.get()` method to find the desired datatype if specired (avoiding key-not-found errors and defaulting to `str` if unspecified), convert the datum to the desired datatype, and append the datum to the `list` associated with each `column` key within the `data` dictionary.

37. [git] Clean up (remove `DEBUG` section), stage, and commit
   (`git commit -m "Refactoring data parsing code"`)

38. [python] Okay, now that we've read the data in a way that
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

Python 0-30 for Scientists
==========================

39. [python] Now, let's write our first function to compute
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
   for temp, windspeed in zip(data['tempout'], data['windspeed']):
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


Now, let's write our first function to compute the wind chill factor.  We'll add this function to the bottom of the file. (put the formula in a ppt).

To indicate a function in python you type `def` for define, the name of your function, and then in parenthesis the input arguments of that function, followed by a colon. On the next lines tab-indented is the code of your function, and your return value.

Here we are also going to have to introduce math operators in Python. Addition, subtraction, and multiplication look much like you'd expect. A double astericks indicates an exponential. A backslash is for dicision, and a double backslash for integer division.

Now we'll call our function. Initialize a list for wind chill with empty square brackets. And in a for-loop, loop through our temperature and wind speed data, applying the function to each tuple data pair. Tuples are ordered like lists, but they use parenthesis instead of square brackets and cannot be changed or appended. We use the zip function in Python to automatically unravel the tuples. Take a look at `zip([1,2], [3,4,5])`.  What is the result?

And finally in `DEBUG` section, let's take a look at our new windchill variable.


40. [git] Clean up, stage, and commit (`git commit -m "Compute wind chill factor"`)

Clean up, stage, and commit. 

41. [python] Now, the wind chill factor is actually in the data file,
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

Now, the wind chill factor is actually in the data file, so we can read it from the file and compare that value to our computed values.  To do this, we need to read the `windchill` column from column 12 as a `float`. Edit the columns and types dictionaries.

In the `DEBUG` section let's print our calculated values, the data provided, and the difference between the two. 
If we use f-strings with `float` formatting we can determine how many decimal places we want to print our answer to.

How do our values compare?

42. [git] Clean up, stage, and commit (`git commit -m "Compare wind chill factors"`)

Clean up, stage, and commit.

43. [python] Now, let's format the output so that it's easy to understand and
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

Now, let's format the output via print statements so that it's easy to understand. Here we'll use f-string formatting with more `float` formatting options.

44. [git] DON'T CLEAN UP!  Just stage and commit
   (`git commit -m "Output formatting comparison data"`)

Stage and commit.

45. [git] Let's rename this script to something meaningful.

   ```bash
   $ git mv mysci.py windchillcomp.py
   $ git commit -m "Renaming first script"
   ```

Let's rename the script to something more meaningful using `git mv`
Contrats you have your first Python script!
Tomorrow we'll write another.

46. [git] Let's push to GitHub!
Python 0-30 for Scientists
==========================

This is intended to pick off right where part 1b left off- you had just commited your new script that reads the file, saving the variables of date, time, and tempout in a data dictionary.

Part 1c - First Python Script Cont
--------------------------------------


38. [python] Okay, now that you've read the data in a way that
   is easy to modify later, it is time to actually do something with
   the data.
   
   Compute the *wind chill* factor.  You've read the
   temperature data into the `tempout` variable, but you also need
   to read the `windspeed` variable from column `7`.  
   Modify the `columns` variable to read:
   
   ```python
   columns = {'date': 0, 'time': 1, 'tempout': 2, 'windspeed': 7}
   ```
   
   and modify the `types` variable to be:
   
   ```python
   types = {'tempout': float, 'windspeed': float}
   ```


39. [git] Great!  Let's save this in our git repo.  Stage and
   commit (`git commit -m "Reading windspeed as well"`).

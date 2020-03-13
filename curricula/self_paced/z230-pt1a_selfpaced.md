Python 0-30 for Scientists
==========================

Welcome to the Python 0 to 30 for Scientists tutorial. In this self-paced course you will learn how to write Python code using Python best practices. Part 1 was designed to take one work day, but you may move through the content much slower or more quickly. Through these instructions you will develop scripts and use git and GitHub to save and organize your work. At the end of this tutorial you will have a grasp of how to begin building your own library of Python tools for your scientific analysis workflows.


Why Python?
-----------
You're already here because you want to learn to use Python for your data analysis and visualizations. Python can be compared to other interpreted object-oriented languages, but is especially great because it is free and open source! 

Being open source means that when people have identified gaps in Python's abilitlies, they have built libraries of code that make those tasks easier. There are libraries specifically for improved mathmatics, statistics, plotting, etc -  collections of code that you can use without having to build yourself. 

Perhaps you are already familiar with importing libraries into your workflow. In IDL people pass around files that contain unique user-written functions -  which achieves this same purpose of reducing the amount of redundant work between scientists, but in Python package managers help you know what version of those functions you are using. Matlab has packages that you can pay extra money to install and use - again Python is free! 

There are many many different libraries of code you can import and use. We are only going to teach you the most commonly used libraries, and one at a time in order to reduce any confusion you may have about what each library offers.

Part 1 will focus on teaching fundamental git and Python, without any external libraries.


Requirements & Installation
--------------------------

But first, check that you have conda or miniconda installed on your OS. 

1. [bash] Check your conda version:

   ```bash
   $ conda list anaconda
   ```
At the time of writing this, the latest version of conda is 4.6. If you have an old version of conda installed, update it.

2. [bash] If necessary, update:

   ```bash
   $ conda update
   ```

If you don't have conda installed at all, please install it. Using the instructions at https://docs.conda.io/projects/conda/en/latest/user-guide/install/index.html 

***NOTE** If you have a REALLY old version of conda it might be easier to delete it and then reinstall it. But before doing this you have to check your env-list to see if there are any environments you created and want to save.

3. Check your conda version again.

4. Install git

Follopw instructions at https://git-scm.com/book/en/v2/Getting-Started-Installing-Git


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
nano mysci.py  ---> (cntrl X)
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

The "with" statement is a context manager that provides clean-up and assures that the file is automatically closed after you've read it. Other input arguments for "open" include "w", for example, if you wanted to write to the file.

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

git reset discards unwanted changes
git checkout .
git clean - fdx

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
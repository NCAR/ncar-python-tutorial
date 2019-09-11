---
layout: page
title: Python Tutorial
---

## 18-20 September 2019

Follow these instructions for setup and verification of your installation.

- [Agenda and Location](#agenda-and-location)
- [Sprints and Optional Lectures](#sprints-and-optional-lectures)
- [Setup Instructions](#setup-instructions)
  - [Step 1: Clone NCAR Python Tutorial Repository](#step-1-clone-ncar-python-tutorial-repository)
  - [Step 2: Install miniconda and create environments](#step-2-install-miniconda-and-create-environments)
  - [Step 3: Close and re-open your current shell](#step-3-close-and-re-open-your-current-shell)
  - [Step 4: Run the setup verification script](#step-4-run-the-setup-verification-script)
- [How to Launch JupyterLab](#how-to-launch-jupyterlab)
  - [1. Cheyenne or DAV via JupyterHub: https://jupyterhub.ucar.edu/](#1-cheyenne-or-dav-via-jupyterhub-httpsjupyterhubucaredu)
  - [2. Cheyenne or DAV via SSH Tunneling](#2-cheyenne-or-dav-via-ssh-tunneling)
  - [3. Hobart via SSH Tunneling](#3-hobart-via-ssh-tunneling)
  - [4. Personal Laptop](#4-personal-laptop)

----

## Agenda and Location

### Location

The bulk of this tutorial will be held in the NCAR Mesa Laboratory's Main Seminar Room.  Space for hands-on work and collaboration has been made available in the Mesa Laboratory's Damon Room and Library.

### Agenda

**DAY 1: Sept 18, 2019**

| TIME  | TITLE                                 |
|-------|---------------------------------------|
| 8:00  | _Questions & Setup_                   |
| 8:30  | Welcome!                              |
| 9:00  | Getting Started with Jupyter & Python |
| 9:30  | Real World Example: OHC Part 1        |
| 10:00 | _Coffee Break_                        |
| 10:30 | Real World Example: OHC Part 2        |
| 11:00 | Real World Example: OHC Part 3        |
| 11:30 | Real World Example: OHC Part 4        |
| 12:00 | _Lunch_                               |
| 13:00 | Real World Example: ENSO index        |
| 13:30 | Real World Example: Oxygen trends     |
| 14:00 | Real World Example: MetPy             |
| 14:30 | _Optional Real World Example_         |
| 15:00 | _Break_                               |
| 15:30 | Sprint Pitches                        |
| 16:00 | _Discussion, Questions & Planning_    |
| 16:30 | _Happy Hour at Under the Sun_         |

**DAY 2: Sept 19, 2019**

Participants are encouraged to work on their Sprint projects all day, but are welcome to attend any of the below optional lectures.  If you want to do more learning by doing yourself, you are encouraged to work on Sprint projects.  If you want to see more details and go further in a more formal presentation, you are encouraged to attend lectures.    

| TIME  | TITLE                              |
|-------|------------------------------------|
| 8:30  | Introduction to Python (Continued) |
| 9:30  | Git & GitHub                       |
| 10:30 | _Coffee Break_                     |
| 11:00 | Visualization                      |
| 12:00 | _Visualization Office Hours_       |
| 12:30 | _Lunch_                            |
| 13:30 | Object Oriented Programming        |
| 14:30 | Unit Testing                       |
| 15:30 | _Break_                            |
| 16:00 | Python Package Structure           |

**DAY 3: Sept 20, 2019**

Participants are encouraged to work on their Sprint projects in the morning but are welcome to attend any of the below optional lectures.  If you want to do more learning by doing yourself, you are encouraged to work on Sprint projects.  If you want to see more details and go further in a more formal presentation, you are encouraged to attend lectures.

| TIME  | TITLE                                          |
|-------|------------------------------------------------|
| 9:00  | MetPy                                          |
| 10:00 | _Coffee Break_                                 |
| 11:00 | More with Dask                                 |
| 12:00 | _Lunch_                                        |
| 13:00 | Conda & Conda Forge                            |
| 13:30 | Update on GeoCAT (new NCL)                     |
| 14:00 | Sprint Project Presentations (Lightning Talks) |
| 15:30 | _Break_                                        |
| 16:00 | Discussion & Closing Comments                  |

----

## Sprints and Optional Lectures

### Sprints

We understand that there is no way that we can thoroughly teach Python in just three days.  It is for that
reason that we are focusing the entire first day on _real world examples_.  Even then, there is no way to
teach Python in such a short time without having you (the student) actually learn by doing.

In hackathons, participants propose Sprint ideas to the rest of the group.  Sprints are short, well defined
projects that multiple people can collaborate and make progress on during the hackathon.  At the end of the
hackathon, participants briefly describe what they've accomplished during the hackathon on their Sprints.
Basically, Sprints are a great way of taking advantage of the expertise _in the room_ to actually get something
done.

We encourage all of you to come up with a Sprint idea for this tutorial, even if it is as simple as just
converting an existing script that you have to Python.  You do not have to pitch your Sprint ideas to the
rest of the room, but we encourage you to do so.  If you do want to pitch your Sprint idea, perhaps to get
more participation from others in the room, please **add a slide with your Sprint proposal** to this Google
Slides presentation:

[https://docs.google.com/presentation/d/15jDEb7wvVlPE2b57C1fchDL25iM44fkJACBafzAZd_s/edit?usp=sharing](https://docs.google.com/presentation/d/15jDEb7wvVlPE2b57C1fchDL25iM44fkJACBafzAZd_s/edit?usp=sharing)

### Optional Lectures

After the first day of the tutorial, when we walk through real world examples, we recognize that many of 
you may not feel ready to actually _do_ anything with Python.  For that reason, there will be optional lectures
in the Mesa Laboratory's Main Seminar Room that will give you the chance to go a little deeper into various
topics.  You do not have to attend any of these lectures, but feel free to come if you are interested.

All of the presentations on Days 2 and 3 are optional.

----

## Setup Instructions

These instructions covers the installation and setup of a Python environment on:

- Cheyenne
- Casper
- CGD's Hobart
- Personal laptop/desktop with a UNIX-variant Operating System

**NOTE:** For windows users, setup scripts provided in this repository don't work on Windows machines for the time being. You may want to follow the instructions available [here](https://conda.io/projects/conda/en/latest/user-guide/install/windows.html).

### Step 1: Clone NCAR Python Tutorial Repository

Run the following commmand to clone this repo to your system(e.g. cheyenne, casper, your laptop, etc...):

```bash
git clone https://github.com/NCAR/ncar-python-tutorial.git
```

### Step 2: Install miniconda and create environments

- Change directory to the cloned repository

  ```bash
  cd ncar-python-tutorial
  ```

- Run the [`configure`](./setup/configure) script:

  ```bash
  ./setup/configure
  ```

  This script will install `conda` package manager if it is unable to find an existing installation. Otherwise, it will update the `base` environment, create an `analysis` environment (if a conda environment called `analysis` exists, it will update packages in it)

### Step 3: Close and re-open your current shell

For changes to take effect, close and re-open your current shell.

### Step 4: Run the setup verification script

- Check conda info with:

  ```bash
  conda info -a
  ```

- From the `ncar-python-tutorial` directory, activate the newly created analysis enviroment:
  
  ```bash
  conda activate analysis
  ```

- Run the setup verification script to confirm that everything is working as expected:
  
  ```bash
  ./setup/check_setup
  ```

- Check that all Jupyterlab extensions were properly installed:
  
  ```bash
  jupyter labextension list
  ```

  You will see something along the lines of the following output:

  ```console
  JupyterLab v1.1.1
  Known labextensions:
     app dir: /Users/abanihi/opt/miniconda3/envs/analysis/share/jupyter/lab
          @jupyter-widgets/jupyterlab-manager v1.0.2  enabled  OK
          @pyviz/jupyterlab_pyviz v0.8.0  enabled  OK
          dask-labextension v1.0.1  enabled  OK
          nbdime-jupyterlab v1.0.0  enabled  OK
    ```

----

## How to Launch JupyterLab

### 1. Cheyenne or DAV via JupyterHub: https://jupyterhub.ucar.edu/

(Recommended)

To use the Cheyenne or DAV compute nodes, we recommend using JupyterLab via NCAR's JupyterHub deployment.

Open your preferred browser (Chrome, Firefox, Safari, etc...) on your ``local machine``, and head over to https://jupyterhub.ucar.edu/.

**You will need to authenticate with either your _yubikey_ or your _DUO_ mobile app**

### 2. Cheyenne or DAV via SSH Tunneling

In case you are having issues with jupyterhub.ucar.edu, we've provided utility scripts for launching JupyterLab on both Cheyenne and Casper via SSH Tunneling:

```bash
conda activate base
./setup/jlab/jlab-ch # on Cheyenne
./setup/jlab/jlab-dav # on Casper
```

### 3. Hobart via SSH Tunneling

For those interested in running JupyterLab on CGD's Hobart, you will need to use SSH tunneling script provided in [``setup/jlab/jlab-hobart``](./setup/jlab/jlab-hobart)

```bash
conda activate base
./setup/jlab/jlab-hobart
```

```bash
$ ./setup/jlab/jlab-hobart --help
Usage: launch dask
Possible options are:
 -w,--walltime: walltime [default: 08:00:00]
 -q,--queue: queue [default: medium]
 -d,--directory: notebook directory
 -p,--port: [default: 8888]
```

### 4. Personal Laptop

For those interested in running JupyterLab on their local machine, you can simply run the following command, and follow the printed instructions on the console:

```bash
conda activate base
jupyter lab
```

![https://circleci.com/gh/NCAR/ncar-python-tutorial/tree/master](https://img.shields.io/circleci/project/github/NCAR/ncar-python-tutorial/master.svg?style=for-the-badge&logo=circleci)

# NCAR Python Tutorial

- [NCAR Python Tutorial](#ncar-python-tutorial)
  - [Setup](#setup)
    - [Step 1: Clone NCAR Python Tutorial Repository](#step-1-clone-ncar-python-tutorial-repository)
    - [Step 2: Install miniconda and create environments](#step-2-install-miniconda-and-create-environments)
    - [Step 3: Close and re-open your current shell](#step-3-close-and-re-open-your-current-shell)
    - [Step 4: Run the setup verification script](#step-4-run-the-setup-verification-script)
  - [Launch Jupyter Lab](#launch-jupyter-lab)
    - [1. Cheyenne or DAV via JupyterHub (https://jupyterhub.ucar.edu/)(Recommended)](#1-cheyenne-or-dav-via-jupyterhub-httpsjupyterhubucaredurecommended)
    - [2. Cheyenne or DAV via SSH Tunneling](#2-cheyenne-or-dav-via-ssh-tunneling)
    - [3. Hobart via SSH Tunneling](#3-hobart-via-ssh-tunneling)
    - [4. Personal Laptop](#4-personal-laptop)

----
## Setup

This tutorial covers the installation and setup of a Python environment on:

- Cheyenne
- Casper
- CGD's Hobart
- Personal laptop/desktop with a UNIX-variant Operating System

**NOTE:** For windows users, setup scripts provided in this repository don't work on Windows machines for the time being. You may want to follow the instructions available [here](https://conda.io/projects/conda/en/latest/user-guide/install/windows.html).


### Step 1: Clone NCAR Python Tutorial Repository

Run the following commmand to clone this repo to your system(e.g. cheyenne, casper, your laptop, etc...):

```bash
$ git clone https://github.com/NCAR/ncar-python-tutorial.git
```

### Step 2: Install miniconda and create environments

- Change directory to the cloned repository
  ```bash
  $ cd ncar-python-tutorial
  ```

- Run the [`configure`](./setup/configure) script:

  ```bash
  $ ./setup/configure
  ```

  This script will install `conda` package manager if it is unable to find an existing installation. Otherwise, it will update the `base` environment, create an `analysis` environment (if a conda environment called `analysis` exists, it will update packages in it)

### Step 3: Close and re-open your current shell

For changes to take effect, close and re-open your current shell.


### Step 4: Run the setup verification script


- Check conda info with:
  ```bash
  $ conda info -a
  ```

- From the `ncar-python-tutorial` directory, activate the newly created analysis enviroment:
  ```bash
  $ conda activate analysis
  ```

- Run the setup verification script to confirm that everything is working as expected:
  ```bash
  $ ./setup/check_setup
  ```

- Check that all Jupyterlab extensions were properly installed:
  ```bash
  $ jupyter labextension list
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
---

## Launch Jupyter Lab

### 1. Cheyenne or DAV via JupyterHub (https://jupyterhub.ucar.edu/)(Recommended)

To use the Cheyenne or DAV compute nodes, we recommend using JupyterLab via NCAR's JupyterHub deployment.

Open your preferred browser (Chrome, Firefox, Safari, etc...) on your ``local machine``, and head over to ``https://jupyterhub.ucar.edu/``.

**You will need to authenticate with either your _yubikey_ or your _DUO_ mobile app**


### 2. Cheyenne or DAV via SSH Tunneling

In case you are having issues with jupyterhub.ucar.edu, we've provided utility scripts for launching JupyterLab on both Cheyenne and Casper via SSH Tunneling:

```bash
$ conda activate base
$ ./setup/jlab/jlab-ch # on Cheyenne
$ # or
$ ./setup/jlab/jlab-dav # on Casper
```


### 3. Hobart via SSH Tunneling

For those interested in running JupyterLab on CGD's Hobart, you will need to use SSH tunneling script provided in [``setup/jlab/jlab-hobart``](./setup/jlab/jlab-hobart)

```bash
$ conda activate base
$ ./setup/jlab/jlab-hobart
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
$ conda activate base
$ jupyter lab
```

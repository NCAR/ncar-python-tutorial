[![CircleCI](https://img.shields.io/circleci/project/github/NCAR/ncar-python-tutorial/master.svg?style=for-the-badge&logo=circleci)](https://circleci.com/gh/NCAR/ncar-python-tutorial/tree/master)

# NCAR Python Tutorial

- [NCAR Python Tutorial](#ncar-python-tutorial)
  - [Setup](#setup)
    - [Step 1: Clone NCAR Python Tutorial Repository](#step-1-clone-ncar-python-tutorial-repository)
    - [Step 2: Install Miniconda and Create Environments](#step-2-install-miniconda-and-create-environments)
    - [Step 3: Close and re-open your current shell](#step-3-close-and-re-open-your-current-shell)
    - [Step 4: Run the Setup Verification Script](#step-4-run-the-setup-verification-script)
  - [Launch Jupyter Lab](#launch-jupyter-lab)
    - [1. Cheyenne or DAV via JupyterHub (Recommended)](#1-cheyenne-or-dav-via-jupyterhub-recommended)
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

**NOTE:** For windows users, setup scripts provided in this repository don't work on Windows machines for the time being. You may want to follow the instructions available [here](https://conda.io/projects/conda/en/latest/user-guide/install/windows.html) to install miniconda.

### Step 1: Clone NCAR Python Tutorial Repository

Run the following commmand to clone this repo to your system(e.g. cheyenne, casper, your laptop, etc...):

```bash
git clone https://github.com/NCAR/ncar-python-tutorial.git
```

### Step 2: Install Miniconda and Create Environments

- Change directory to the cloned repository

  ```bash
  cd ncar-python-tutorial
  ```

- Run the [`configure`](./setup/configure) script:

  **NOTE**: Be prepared for the script to take up to 15 minutes to complete.

  ```bash
  ./setup/configure
  ```

```bash
$ ./setup/configure --help
usage: configure [-h] [--clobber] [--download] [--prefix PREFIX]

Set up tutorial environment.

optional arguments:
  -h, --help            show this help message and exit
  --clobber, -c         Whether to clobber existing environment (default:
                        False)
  --download, -d        Download tutorial data without setting environment up
                        (default: False)
  --prefix PREFIX, -p PREFIX
                        Miniconda3 install location)
```

Default values for ``--prefix`` argument are:

- Personal laptop / Hobart: `$HOME/miniconda3`
- Cheyenne or Casper: `/glade/work/$USER/miniconda3`

**NOTE**:
In case the default `prefix` is not appropriate for you (due to limited storage), feel free to specify a different installation location such as a `project` workspace on a shared filesystem like GLADE or Hobart's filesystem.

The `configure` script does the following:

- Install `conda` package manager if it is unable to find an existing installation. Otherwise, it will update the `base` environment
- Create or Update `python-tutorial` conda environment.
- Download data if not on Cheyenne or Casper or Hobart. If on Cheyenne or Casper or Hobart, create soft-links to an existing/local data repository.

### Step 3: Close and re-open your current shell

For changes to take effect, close and re-open your current shell.

### Step 4: Run the Setup Verification Script

- Check that *conda info* runs successfully:

  ```bash
  conda info
  ```

- From the `ncar-python-tutorial` directory, activate `python-tutorial` conda environment:

  ```bash
  conda activate python-tutorial
  ```

- Run the setup verification script to confirm that everything is working as expected:

  ```bash
  cd ncar-python-tutorial
  ./setup/check_setup
  ```

  This step should print **"Everything looks good!"**.

----

## Launch Jupyter Lab

### 1. Cheyenne or DAV via JupyterHub (Recommended)

- JupyterHub link: https://jupyterhub.ucar.edu/

To use the Cheyenne or DAV compute nodes,we recommend using JupyterLab via NCAR's JupyterHub deployment.

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

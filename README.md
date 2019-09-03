![https://circleci.com/gh/NCAR/ncar-python-tutorial/tree/master](https://img.shields.io/circleci/project/github/NCAR/ncar-python-tutorial/master.svg?style=for-the-badge&logo=circleci)

# NCAR Python Tutorial

- [NCAR Python Tutorial](#ncar-python-tutorial)
  - [Setup](#setup)
    - [Step 1: Clone NCAR Python Tutorial Repository](#step-1-clone-ncar-python-tutorial-repository)
    - [Step 2: Install miniconda and create environments](#step-2-install-miniconda-and-create-environments)
    - [Step 3: Close and re-open your current shell](#step-3-close-and-re-open-your-current-shell)
    - [Step 4: Run the setup verification script](#step-4-run-the-setup-verification-script)

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
git clone https://github.com/NCAR/ncar-python-tutorial.git
```

### Step 2: Install miniconda and create environments

- Change directory to the cloned repository
  ```bash
  cd ncar-python-tutorial
  ```

- Run the `configure` script:

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

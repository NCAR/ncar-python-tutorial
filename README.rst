====================
NCAR Pangeo Tutorial
====================

First Time Setup
-----------------

Clone this repository and follow the instructions below.

1. Get miniconda and install
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This tutorial covers the installation and setup of a Python environment on:

- Cheyenne/DAV and/or CGD platforms

Throughout this tutorial, we will be using miniconda which provides 
prepackaged Python environments with automated installers, the package manager ``conda``.

https://docs.conda.io/en/latest/miniconda.html

We suggest manually adding the miniconda path to your dot files (answer "no" to the last question).


.. code:: bash

    wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -O miniconda.sh
    bash miniconda.sh

To verify that conda is available on your system, you can try

.. code:: bash 

   conda --version 

After install, update conda:

.. code:: bash

    conda update -n base -c defaults conda

And configure the shell, replacing {SHELL} in the command below with your shell (i.e., bash, tcsh,...):

.. code:: bash

   conda init {SHELL}


2. Create environments
~~~~~~~~~~~~~~~~~~~~~~~~

Conda allows us to set up virtual Python environments for different projects, 
in which different versions of the required dependencies are installed.
With this approach, it is easy to maintain multiple environments with different configurations. 


First update the conda base environment.

.. code:: bash

  conda env update -f environments/env-conda-base.yml


Next create a new environment call "analysis" (this can take 10-15 min).

.. code:: bash

  conda env create -f environments/env-analysis.yml

If you are interested in using Matlab in JupyterLab, consider creating the following environment.

.. code:: bash

  conda env create -f environments/env-py-matlab.yml

(Using Matlab requires building the Matlab Python API; see scripts/build-matlab-api.  Scripts are setup to use API's built in ~/matlab-python or ~mclong/matlab-python.)

To use one of these environments, we need to activate it using the command ``conda activate ENV_NAME``, and to 
deactivate an environment, we use ``conda deactivate``. 


Once you've created the above environments, you will need to run the ``post_build``
script in order to build JupyterLab extensions.

.. code:: bash

  conda activate base
  ./environments/post_build


To manage environments, the ``conda env``, ``conda info``, and ``conda list`` commands
are helpful tools. The ``conda info`` command can be used to list available environments (same as ``conda env list``).



3. Copy configuration file:
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code:: bash

   ./config/copy_config

This adds a file to your home directory: ``~/.config/dask/jobqueue.yaml``.
Consider opening this file in a text editor and changing the lines specifying project number: remove the comment and add your preferred project number. 

4. Start Jupyter Lab
~~~~~~~~~~~~~~~~~~~~~

To use the Cheyenne compute nodes:

.. code:: bash

  cd scripts
  ./jlab-ch


To use the DAV system:

.. code:: bash

  cd scripts
  ./jlab-dav

These scripts print instructions for how to SSH into the machine with an SSH tunnel that enables connecting to the compute node where JupyterLab is running. Once you have made this SSH connection, open a browser on your local machine and go to the address: localhost:8888 (or whichever port specified in the jlab script).

If you want to use Matlab, you must add a flag to enable the module load; for instance:

.. code:: bash

  cd scripts
  ./jlab-dav --matlab

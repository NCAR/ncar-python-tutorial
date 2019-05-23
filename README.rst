First Time Setup
-----------------

This tutorial covers the installation and setup of a Python environment on:

- Cheyenne/DAV 

Throughout this tutorial, we will be using miniconda which provides 
prepackaged Python environments with automated installers, the package manager ``conda``.

https://docs.conda.io/en/latest/miniconda.html


1. Clone NCAR Pangeo Tutorial Repository
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code:: bash 

   git clone https://github.com/NCAR/NCAR-pangeo-tutorial


2. Get miniconda and install
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code:: bash

    wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -O miniconda.sh
    bash miniconda.sh    # Follow the prompts on the installer screens.

If you are unsure about any setting, accept the defaults. We recommend adding the miniconda path to your PATH variable manually. For a bash user, this would entail adding something like the following to your .bashrc file:

.. code:: bash
   
   export PATH=/path/to/installation/miniconda3/bin:${PATH}


.. NOTE::

To make the changes take effect, logout and log back in.
  
Change into the newly created NCAR-pangeo-tutorial directory

.. code:: bash 

   cd /path/to/NCAR-pangeo-tutorial

To verify that conda is available on your system, you can try

.. code:: bash 

   conda --version 

After install, update conda:

.. code:: bash

    conda update -n base -c defaults conda


.. NOTE::
 
The following step may not be necessary with more recent version of the miniconda script.

And configure the shell, replacing {SHELL} in the command below with your shell (i.e., bash, tcsh,...):

.. code:: bash

   conda init {SHELL}


3. Create environments
~~~~~~~~~~~~~~~~~~~~~~~~

Conda allows you to set up virtual Python environments for different projects, 
in which different versions of the required dependencies are installed.
With this approach, it is easy to maintain multiple environments with different configurations. 


First update the conda base environment.

.. code:: bash

  conda env update -f environments/env-conda-base.yml


Next create a new environment call "analysis" (this can take 10-15 min).

.. code:: bash

  conda env create -f environments/env-analysis.yml

Note that some version of CESM do not support Python 3, but support for Python 2 is going away. 
In case you need a Python 2 environment, you can create one as follows.

.. code:: bash

   conda env create -f environments/env-py2.yml

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



4. Copy configuration file:
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code:: bash

   ./config/copy_config

This adds a file to your home directory: ``~/.config/dask/jobqueue.yaml``.
Consider opening this file in a text editor and changing the lines specifying project number: remove the comment and add your preferred project number. 

5. Start Jupyter Lab
~~~~~~~~~~~~~~~~~~~~~

To use the Cheyenne compute nodes, we recommend using JupyterLab via NCAR's JupyterHub deployment. 
This jupyter hub is accessible at ``https://jupyterhub.ucar.edu/ch``. 
You must have a Cheyenne account. The spawning screen will look like this (below):
but with your project account specified.

.. image:: https://i.imgur.com/gLugukz.png
   :alt: JHUB
   :align: center

- Specify your project account 
- You can also change the queue and other settings

Once your session is active: 

- Create a new notebook: ``File ➤ New ➤ Notebook``

.. image:: https://i.imgur.com/pXpwUXC.png
   :alt: launch
   :align: center


- Select which kernel to use:

.. image:: https://i.imgur.com/q8LDBCj.png
   :alt: prompt
   :align: center

.. image:: https://i.imgur.com/zoGymUm.png
   :alt: select-kernel
   :align: center


To use the DAV system:

.. code:: bash

  cd scripts
  ./jlab-dav

These scripts print instructions for how to SSH into the machine with an SSH tunnel that enables connecting to the compute node where JupyterLab is running. Once you have made this SSH connection, open a browser on your local machine and go to the address: localhost:8888 (or whichever port specified in the jlab script).

If you want to use Matlab, you must add a flag to enable the module load; for instance:

.. code:: bash

  cd scripts
  ./jlab-dav --matlab

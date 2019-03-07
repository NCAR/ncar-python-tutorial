NCAR-pangeo-tutorial
--------------------

Getting started
~~~~~~~~~~~~~~~

Clone this repository and follow the instructions below.

1. Get miniconda and install
++++++++++++++++++++++++++++

https://docs.conda.io/en/latest/miniconda.html

We suggest manually adding the miniconda path to your dot files (answer "no" to the last question).


.. code:: bash

    wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -O miniconda.sh
    bash miniconda.sh

After install, update conda:

.. code:: bash

    conda update -n base -c defaults conda

And configure the shell, replacing {SHELL} in the command below with your shell (i.e., bash, tcsh,...):

.. code:: bash

   conda init {SHELL}


2. Create environments
++++++++++++++++++++++

First update the conda base environment.

.. code:: bash

  conda env update -f environments/env-conda-base.yml


Next create a new environment call "analysis" (this can take 10-15 min).

.. code:: bash

  conda env create -f environments/env-analysis.yml

If you are interested in using Matlab in JupyterLab, consider creating the following environment.

.. code:: bash

  conda env create -f environments/env-matlab.yml

(This requires building the Matlab Python API; see scripts/build-matlab-api.
Scripts are setup to use API's in ~/matlab-python or ~mclong/matlab-python)

Once you've created the above environments, you will need to run the ``post_build``
script in order to build JupyterLab extensions.

.. code:: bash

  conda activate base
  ./environments/post_build


3. Copy configuration file:
+++++++++++++++++++++++++++

.. code:: bash

   cp notebooks/jobqueue.yaml ~/.config/dask/.

4. Start Jupyter Lab
++++++++++++++++++++

To use the Cheyenne compute nodes:

.. code:: bash

  cd scripts
  ./jlab-ch


To use the DAV system:

.. code:: bash

  cd scripts
  ./jlab-dav

These scripts print instructions for how to SSH into the machine with an SSH tunnel that enables connecting to the compute node where JupyterLab is running.

Once you have made this SSH connection, open a browser on you local machine and go to the address: localhost:8888 (or whichever port  specified in the jlab script).

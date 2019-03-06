NCAR-pangeo-tutorial
--------------------

Getting started
~~~~~~~~~~~~~~~

Clone this repository and follow the instructions below.

1. Get miniconda and install
++++++++++++++++++++++++++++

https://docs.conda.io/en/latest/miniconda.html

We suggest manually adding the miniconda path to your dot files. 
  
.. code:: bash

    wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -O miniconda.sh
    bash miniconda.sh

2. Create environments
++++++++++++++++++++++

.. code:: bash

  conda env create -f environments/conda-base.yml
  conda env create -f environments/env-analysis.yml

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
  jlab-ch


To use the DAV system:

.. code:: bash

  cd scripts
  jlab-dav

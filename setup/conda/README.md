
# Creating Additional Environments

If you are interested in using Matlab in JupyterLab, consider creating the following environment using [env-py-matlab.yml](./environments/env-py-matlab.yml).

```bash
  conda env create -f ./setup/environments/env-py-matlab.yml
```

(Using Matlab requires building the Matlab Python API; see [`setup/conda/build-matlab-api`](./build-matlab-api).  Scripts are set up to use API's built in ``~/matlab-python`` or ``~mclong/matlab-python``.)

To use an environment, we need to activate it using the command ``conda activate ENV_NAME``,and to deactivate an environment, we use ``conda deactivate``.

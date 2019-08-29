#!/usr/bin/env python3

import subprocess
from tempfile import TemporaryDirectory as tmpdir
import os


def detect_platform():
    import platform

    p = {}
    p["system"] = platform.system().lower()
    p["node"] = platform.node().lower()
    return p


def detect_existing_executable(name):
    """ Check Wether `name` is on PATH. """
    from distutils.spawn import find_executable

    return find_executable(name)


def install_miniconda3():

    installers = {
        "linux": "https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh",
        "darwin": "https://repo.anaconda.com/miniconda/Miniconda3-latest-MacOSX-x86_64.sh",
    }

    conda_path = detect_existing_executable("conda")
    if conda_path is not None:
        print(f"*********Found an existing Conda installation at: {conda_path} **********")
        print("**********Skipping Conda installation...*************")

    else:
        print("*********** Downloading Miniconda... ****************")
        plat = detect_platform()

        if plat["system"] in installers:
            with tmpdir():

                cmd = ["wget", installers[plat["system"]], "-O", "miniconda.sh"]
                subprocess.check_call(cmd)
                subprocess.call(["chmod", "+x", "miniconda.sh"])

                print("************ Installing Conda... *****************")
                cmd = ["./miniconda.sh", "-b", "-p", "$HOME/miniconda"]
                subprocess.check_call(cmd)

            conda = f"{os.environ['HOME']}/miniconda/bin/conda"
            output = subprocess.Popen(
                f"{conda} init bash; . ~/.bashrc", shell=True, stdout=subprocess.PIPE
            )
            print(output.communicate()[0].strip().decode())
            print("******** Miniconda installation completed successfully. ****************")


def main():

    install_miniconda3()


if __name__ == "__main__":
    main()

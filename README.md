[![CircleCI](https://img.shields.io/circleci/project/github/NCAR/ncar-python-tutorial/master.svg?style=for-the-badge&logo=circleci)](https://circleci.com/gh/NCAR/ncar-python-tutorial/tree/master)

# NCAR Python Tutorial

- [NCAR Python Tutorial](#ncar-python-tutorial)
  - [Setup: Installing Miniconda](#setup-installing-miniconda)
    - [Linux](#linux)
    - [Mac OS X](#mac-os-x)
    - [Windows](#windows)

----

## Setup: Installing Miniconda

This tutorial covers the installation and setup of a Python environment on:

- Cheyenne
- Casper
- Personal laptop/desktop or any other machine

### Linux

After you have logged into Cheyenne, Casper or any machine running linux, download and install Miniconda:

1. Open your shell/terminal program

2. Download the linux installer

   ```bash
   $ wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
   $ chmod +x Miniconda3-latest-Linux-x86_64.sh
   $ ./Miniconda3-latest-Linux-x86_64.sh
   ```

3. Scroll through the license (press the space bar to move through quickly), type **yes** to approve the terms, and then accept all the installation defaults (on Cheyenne and Casper it is recommended to install miniconda in your work space (e.g. `/glade/work/username/miniconda3`) to avoid using up your home space).

4. Close the terminal/shell program. Then, restart it (log back in).
5. Initialize conda for shell interaction by replacing `YOUR_SHELL` with your default/preferred shell. Currently compatible shells are `{bash, fish, powershell, tcsh, xonsh, zsh}`:

   ```bash
   conda init YOUR_SHELL
   ```

6. Within the terminal, type:

   ```bash
   conda update --all
   ```

7. To verify that the setup completed successfully, check conda version with:

   ```console
   conda --version
   ```

### Mac OS X

1. Open your shell/terminal program

2. Download the linux installer

   ```bash
   $ wget https://repo.anaconda.com/miniconda/Miniconda3-latest-MacOSX-x86_64.sh
   $ # OR
   $ # curl -O https://repo.anaconda.com/miniconda/Miniconda3-latest-MacOSX-x86_64.sh
   $ chmod +x Miniconda3-latest-MacOSX-x86_64.sh
   $ ./Miniconda3-latest-MacOSX-x86_64.sh
   ```

3. Scroll through the license (press the space bar to move through quickly), type **yes** to approve the terms, and then accept all the installation defaults.
4. Close the terminal/shell program. Then, restart it (log back in).

5. Initialize conda for shell interaction by replacing `YOUR_SHELL` with your default/preferred shell. Currently compatible shells are `{bash, fish, powershell, tcsh, xonsh, zsh}`:

   ```bash
   conda init YOUR_SHELL
   ```

6. Within the terminal, type:

   ```bash
   conda update --all
   ```

7. To verify that the setup completed successfully, check conda version with:

   ```console
   conda --version
   ```

### Windows

1. Click on https://repo.anaconda.com/miniconda/Miniconda3-latest-Windows-x86_64.exe
   1. Wait for it to download. It will place a file called `Miniconda3-latest-Windows-x86_64.exe` in your downloads folder.

2. Click on the downloaded file to start the installation. When the     installer window appears:
   - Click Next to get started,
   - Click `I Agree` to accept the     license terms, and
   - Then click Next to accept the defaults for the next several screens.
   - When you reach the screen with the Install button, verify the the two Advanced Options checkboxes to Add Miniconda to my `PATH environment` variable and to Register Miniconda as my default Python 3.7 are both checked. Then click Install.
   - When the install finishes, click Next then Finish. You can ignore the window that pops up in your browser.

3. Press `Windows + R` keys together on the keyboard to open the Run box. Type `powershell` and hit Enter.

4. Initialize conda for shell interaction by replacing `YOUR_SHELL` with your default/preferred shell. Currently compatible shells are `{bash, fish, powershell, tcsh, xonsh, zsh}`

   ```console
   conda init YOUR_SHELL
   ```

5. Within the terminal, type:

   ```bash
   conda update --all
   ```

6. To verify that the setup completed successfully, check conda version with:

   ```console
   conda --version
   ```

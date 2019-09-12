# -*- coding: utf-8 -*-
from __future__ import absolute_import, division, print_function
from ftplib import FTP
import os
import sys

# Ref: https://stackoverflow.com/questions/3173320/text-progress-bar-in-the-console
# https://gist.github.com/aubricus/f91fb55dc6ba5557fbab06119420dd6a
def printProgressBar(iteration, total, prefix="", suffix="", decimals=1, bar_length=100):
    """
    Call in a loop to create terminal progress bar
    @params:
        iteration   - Required  : current iteration (Int)
        total       - Required  : total iterations (Int)
        prefix      - Optional  : prefix string (Str)
        suffix      - Optional  : suffix string (Str)
        decimals    - Optional  : positive number of decimals in percent complete (Int)
        bar_length  - Optional  : character length of bar (Int)
    """
    str_format = "{0:." + str(decimals) + "f}"
    percents = str_format.format(100 * (iteration / float(total)))
    filled_length = int(round(bar_length * iteration / float(total)))
    bar = "█" * filled_length + "-" * (bar_length - filled_length)

    sys.stdout.write("\r%s |%s| %s%s %s" % (prefix, bar, percents, "%", suffix)),
    # sys.stdout.write('%s |%s| %s%s %s\r' % (prefix, bar, percents, '%', suffix)),

    if iteration == total:
        sys.stdout.write("\n")
    sys.stdout.flush()


def ftp_download(
    host="ftp.cgd.ucar.edu",
    directory="archive/aletheia-data/tutorial-data",
    filelist=[],
    output_dir=None,
):
    ftp = FTP()
    ftp.connect(host)
    ftp.login()
    ftp.cwd(directory)
    if not filelist:
        filenames = ftp.nlst()

    else:
        filenames = filelist

    if not output_dir:
        output_dir = os.getcwd()

    try:
        os.makedirs(output_dir)

    except Exception:
        pass

    # Initial call to print 0% progress
    l = len(filenames)
    print("Currently downloading tutorial data")
    printProgressBar(0, l, prefix="Progress:", suffix="", bar_length=50)
    for i, filename in enumerate(filenames):
        local_filename = os.path.join(output_dir, filename)
        if os.path.exists(local_filename):
            # Do nothing if file or symlink exists
            print("{} exists already".format(local_filename))
        else:
            with open(local_filename, "wb") as f:
                cmd = "RETR {}".format(filename)
                ftp.retrbinary(cmd, f.write)

            print(local_filename, " ")
        # Update Progress Bar
        printProgressBar(i + 1, l, prefix="Progress:", suffix="", bar_length=50)

    ftp.quit()


if __name__ == "__main__":
    ftp_download(directory="archive/aletheia-data/", filelist=["test.sh"])

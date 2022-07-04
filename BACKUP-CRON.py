#!/usr/bin/env python3

import sys
import os
import tarfile
import datetime

source = "/home/example.py" #Enter the path of the directory or files you wish to backup here
destination="/home/example-user/Desktop/" #Enter the path of the directory where you wish to save your backup here

if os.path.exists(source):
    print("Starting the backup...")

    tf = tarfile.open(destination + "Backup" + str(datetime.datetime.now()) + ".tar.gz", mode="w:gz")
    tf.add(source)

    print("Backup Completed.")
else:
    print("file/directory does not exist")
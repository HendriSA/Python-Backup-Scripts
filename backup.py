#!/usr/bin/env python3

import os
import tarfile
import datetime

print ("Enter the directory or path you want to backup EX: /home/example.py" )
source = input()

print ("Enter the location to save the backup file EX: /home/example-user/Desktop/" )
destination = input()

if os.path.exists(source):
    print("Starting the backup...")

    tf = tarfile.open(destination + "Backup" + str(datetime.datetime.now()) + ".tar.gz", mode="w:gz")
    tf.add(source)

    print("Backup Completed.")
else:
    print("file/directory does not exist")
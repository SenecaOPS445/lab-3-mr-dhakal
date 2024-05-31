#!/usr/bin/env python3
# Author ID: mrdhakal

import subprocess

def free_space():

    p = subprocess.Popen(['df', '-h'], stdout=subprocess.PIPE)
    pl = subprocess.Popen(['grep', '/$'], stdin=p.stdout, stdout=subprocess.PIPE)
    p2 = subprocess.Popen(['awk', '{print $4}'], stdin=pl.stdout, stdout=subprocess.PIPE)
    p. stdout.close()
    pl.stdout.close()
    output = p2.communicate()[0]
    free_space = output.decode ('utf-8').strip()

    return free_space
if __name__ == "_main_":
    print (free_space())
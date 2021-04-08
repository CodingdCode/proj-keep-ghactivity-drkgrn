#!/usr/bin/env python3

import subprocess as cmd

cmd.run(" sudo git add .",check=True, shell=True)

cmd.run("sudo git commit -m'pi push'", check=True, shell=True)

cmd.run("sudo git push origin master -f", check=True, shell=True)

##


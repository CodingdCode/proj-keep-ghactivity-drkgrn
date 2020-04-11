import subprocess as cmd

cmd.run("git add .",check=True, shell=True)

cmd.run("git commit -m'pi push'", check=True, shell=True)

cmd.run("git push origin master", check=True, shell=True)

#testing pushing with configed credentials again 
#
#
#

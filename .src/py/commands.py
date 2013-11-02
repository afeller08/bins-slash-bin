import os

path = os.environ["CUSTOMPATH"].split(':')

for subpath in path:
    os.system("ls %s" % subpath)

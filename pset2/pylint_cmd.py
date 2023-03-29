import os 

cmds = ["python -m pylint luxserver.py  ",
        "python -m pylint lux.py "]

for cmd in cmds:
    os.system(cmd)
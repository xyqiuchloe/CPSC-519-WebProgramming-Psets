import os 

cmds = ["python -m pylint filters_obj.py",
        "python -m pylint luxdetails.py ",
        "python -m pylint lux.py",
        "python -m pylint filters_detail.py "]

for cmd in cmds:
    os.system(cmd)
import os 
  
# Command to execute
# Using Windows OS command
cmds = ["python -m coverage run -p lux.py -d Yale -c paintings",
"python -m coverage run -p lux.py -a duchamp -l tu",
"python -m coverage run -p lux.py -a gogh",
"python -m coverage run -p lux.py -c \"still life\" -a picass",
"python -m coverage run -p lux.py -d numismatics -a hall -l token -c numismatics",
"python -m coverage run -p lux.py",
"python -m coverage run -p lux.py -l \"Daniel Wad\"",
"python -m coverage run -p lux.py -l \"seal box\"",
"python -m coverage run -p lux.py -l \"chest with drawers\"",
"python -m coverage run -p lux.py -c qrrrrrrrrrrrrrrrrrrrrrr",
"python -m coverage run -p lux.py -z",
"python -m coverage run -p luxdetails.py 9295",
"python -m coverage run -p luxdetails.py 254",
"python -m coverage run -p luxdetails.py 148",
"python -m coverage run -p luxdetails.py 974",
"python -m coverage run -p luxdetails.py 640",
"python -m coverage run -p luxdetails.py 3174",
"python -m coverage run -p luxdetails.py 142",
"python -m coverage run -p luxdetails.py 14",
"python -m coverage run -p luxdetails.py 310215",
"python -m coverage run -p luxdetails.py 9295 123",
"python -m coverage run -p luxdetails.py we",
"python -m coverage combine",
"python -m coverage html"]
  
# Using os.system() method

for cmd in cmds:
    os.system(cmd)
# requirements
# sudo apt install unoconv
# pip install tqdm
# pip install glob
import glob
import tqdm
import os

path = "documents"
files = [f for f in glob.glob(path + "**/*.pptx", recursive=True)]
for f in tqdm.tqdm(files):
    command = 'unoconv -f pdf "{}"'.format(f)
    os.system(command)


## WELL TESTED FOR UBUNTU , WORKS PERFECTLY

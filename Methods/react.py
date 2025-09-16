import os
import subprocess
import json

import commun

def setup_react_project(name):
    subprocess.run(f"pnpm create vite {name} --template react-ts", shell=True)
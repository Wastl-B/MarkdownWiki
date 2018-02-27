#!.venv/bin/python
"""
install bootstrap and node dependencies
"""

import os
import subprocess


PREV_PATH = os.getcwd()
PATH = os.path.join(os.path.dirname(__file__), 'markdown_wiki/static/')

os.chdir(PATH)
subprocess.run(['npm', 'install'])
os.chdir(PREV_PATH)

print('node dependencies installed')
#!.venv/bin/python
"""
build bootstrap-custom
"""
import os
import subprocess

PREV_PATH = os.getcwd()
PATH = os.path.join(os.path.dirname(__file__), 'markdown_wiki/static/')

os.chdir(PATH)
subprocess.run(['./build.sh'])
os.chdir(PREV_PATH)

print('bootstrap-custom compiled')

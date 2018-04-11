#!.venv/bin/python
"""
install node dependencies like bootstrap etc
"""
import argparse
import os
import subprocess


parser = argparse.ArgumentParser(description='Install node_modules')
parser.add_argument(
    '-n', '--npm', help='if npm should be used, instead of yarn', action='store_const', const='npm')


if __name__ == '__main__':
    args = parser.parse_args()
    manager = args.npm or 'yarn'

    PREV_PATH = os.getcwd()
    PATH = os.path.join(os.path.dirname(__file__), 'markdown_wiki/static/')

    os.chdir(PATH)
    subprocess.run([manager, 'install'])
    os.chdir(PREV_PATH)

#!.venv/bin/python
"""
access to gulp tasks in static folder to compile SASS or start watch mode for development
"""
import argparse
import os
import subprocess


parser = argparse.ArgumentParser(description='Compile SASS')
parser.add_argument(
    '-w', '--watch', help='start the SASS watch mode', action='store_const', const='watch')
parser.add_argument(
    '-m', '--minify', help='minify complied CSS', action='store_const', const='minify')
parser.add_argument(
    '-n', '--npm', help='if npm should be used, instead of yarn', action='store_const', const='npm')


if __name__ == '__main__':
    args = parser.parse_args()
    manager = args.npm or 'yarn'
    task = args.watch or args.minify or 'default'

    PREV_PATH = os.getcwd()
    PATH = os.path.join(os.path.dirname(__file__), 'markdown_wiki/static/')

    os.chdir(PATH)
    subprocess.run([manager, 'gulp', task])
    os.chdir(PREV_PATH)

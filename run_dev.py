#!.venv/bin/python
"""
run file for development with debug, IP and port options
"""
from markdown_wiki import MarkdownWiki
import sys
import getopt


def main(argv):
    ip = '127.0.0.1'
    port = 5000
    debug = False
    try:
        opts, args = getopt.getopt(argv, 'hi:p:d', ['ip=', 'port=', 'debug='])
    except getopt.GetoptError:
        print('run.py -i <IP> -p <PORT>')
        sys.exit(2)

    for opt, arg in opts:
        if opt == '-h':
            print('usage:\nrun.py -i <IP> -p <PORT>')
            sys.exit()
        elif opt in ('-i', '--ip'):
            ip = str(arg)
        elif opt in ('-p', '--port'):
            port = int(arg)
        elif opt in ('-d', '--debug'):
            debug = True

    MarkdownWiki.run(debug=debug, host=ip, port=port)


if __name__ == '__main__':
    main(sys.argv[1:])

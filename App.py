"""App.

Usage:
  App.py -h | --help
  App.py --version
  App.py connect <username> <password>

Options:
  -h --help     Show this screen.
  --version     Show version.

"""

from docopt import docopt
import log

if __name__ == '__main__':
    arguments = docopt(__doc__, version="0.0.1")
    if arguments['connect']:
        log.connect(username=arguments['<username>'],password=['<password>'])

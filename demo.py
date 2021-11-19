# author: Tiffany Timbers
# date: 2020-01-15

"""This script prints out docopt args.
Usage: demo.py <arg1> --arg2=<arg2> [--arg3=<arg3>] [<arg4>]

Options:
  <arg>             Takes any value (this is a required positional argument)
  --arg2=<arg2>     Takes any value (this is a required option)
  [--arg3=<arg3>]   Takes any value (this is an optional option)
  [<arg4>]          Takes any value (this is an optional positional argument)
""" 

from docopt import docopt
opt = docopt(__doc__)

def main(d, arg4):
  print(d)
  print(type(d))
  print(arg4)

if __name__ == "__main__":
    main(opt, opt["<arg4>"])

import argparse
import os

'''
parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('integers', metavar='N', type=int, nargs='+',
                   help='an integer for the accumulator')
parser.add_argument('--sum', dest='accumulate', action='store_const',
                   const=sum, default=max,
                   help='sum the integers (default: find the max)')

args = parser.parse_args()
print(args.accumulate(args.integers))
'''

print(os.path.join(os.getcwd(), 'templates', 'nagios'))

print os.getcwd()

print(os.path.dirname(os.path.abspath(__file__)))

print(os.walk('/').next())
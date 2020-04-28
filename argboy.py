import argparse

parser = argparse.ArgumentParser(description='Process some integers')
parser.add_argument('-i', metavar='i', type=str, nargs=1, help='the input file', required=True)
parser.add_argument('-o', metavar='o', type=str, nargs=1, help='the output file', required=True)
parser.add_argument('-t', metavar='t', type=int, nargs=1, help='the threshold', default=[80])
## parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer for the accumulator')
## parser.add_argument('--sum', dest='accumulate', action='store_const', const=sum, default=max, help='sum integers')

args = parser.parse_args()
print(args)
print(args.i[0])
print(args.o[0])
print(args.t)



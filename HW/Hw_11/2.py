import argparse

parser = argparse.ArgumentParser()

parser.add_argument("-g", metavar="N", type=int, nargs="+", help="an integer for the accumulator")
parser.add_argument('-f', help='Determining the decimal place', type=int)

args = parser.parse_args()

count = 0
for i in args.g:
    count += i

grade = round(count / len(args.g), 2)
if args.f:
    print(f"your avg is {round(count / len(args.g), args.f)}")
else:
    print(f" your avg grades is {grade}")

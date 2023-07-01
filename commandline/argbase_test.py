import argparse
# Create the parser
parser = argparse.ArgumentParser(description="this is a training program")
#add args
# Add arguments
parser.add_argument('arg1', type=int, help="Description of argument 1")
parser.add_argument('arg2', type=str, help="Description of argument 2")

#parse command line
args = parser.parse_args()

#access and use args
print("argument 1 : ", args.arg1)
print("argument2: ", args.arg2)
import sys
import numpy

def perform_operation(_f,_opperation):
    data = numpy.loadtxt('data/' + _f, delimiter=',')
    for m in _opperation(data, axis=1):
        print(m)

def main():
    script = sys.argv[0]
    action = sys.argv[1]
    filenames = sys.argv[2:]

    #Test if an operation flag was passed. If true, define revelant function.
    if action.startswith('--'):
        try:
            opperation = getattr(numpy, action[2:])
        except:
            raise ValueError('Flag passed is invalid')
    else:
        raise ValueError('No flag was passed as an input.')

    #Loop over input files
    [perform_operation(f, opperation) for f in filenames]

if __name__ == '__main__':
   main()

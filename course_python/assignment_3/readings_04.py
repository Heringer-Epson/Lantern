import sys
import numpy

def main():
    script = sys.argv[0]
    action = sys.argv[1]
    filenames = sys.argv[2:]

    for f in filenames:
        data = numpy.loadtxt('data/' + f, delimiter=',')
        try:
            opperation = getattr(numpy, action[2:])
            for m in opperation(data, axis=1):
                print(m)
        except:
            raise ValueError('Flag passed is invalid')

if __name__ == '__main__':
   main()

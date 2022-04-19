import sys

def calc(a, b, c, d, e, f):
    return 1*a + 1*b + 1*c + 0.75*d + 0.5*e + 0*f

if __name__ == "__main__":
    with open(sys.argv[1]) as fh:
        [a, b, c, d, e, f] = list(map(int, fh.readline().rstrip().split()))
    print(2*calc(a, b, c, d, e, f))
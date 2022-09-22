import sys
print(sys.getrecursionlimit()) # default Prints 1000
sys.setrecursionlimit(2000)
print(sys.getrecursionlimit())
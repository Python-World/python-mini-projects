import sys
import math
from functools import reduce


def get_factors(n):
  factors = reduce(list.__add__, [[i, n//i] for i in range(1, int(math.sqrt(n))+1) if n % i == 0])
  factors = sorted(list(set(factors)))
  return factors


if __name__ == '__main__':
  if len(sys.argv) > 1:
    n = int(sys.argv[1])
    factors = ' '.join([str(factor) for factor in get_factors(n)])
    print(factors)
  else:
    print('You must enter a number')
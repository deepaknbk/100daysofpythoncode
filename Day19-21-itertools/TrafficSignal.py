import itertools
import sys
import time
signal=itertools.cycle(['Green','Orange','Red'])
for _ in range(20):
  sys.stdout.write('\r'+ next(signal))
  sys.stdout.flush()
  time.sleep(5)
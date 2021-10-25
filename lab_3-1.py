# Author: SCT (ADMG) 10/25/21

import math
import time

time_period = time.process_time()
print(2 ** 2)

time_period2 = time.process_time()
print(math.pow(2, 2))

finaltime = time_period2 - time_period
print(finaltime)

time_period3 = time.perf_counter()
print(2 ** 2)

time_period4 = time.perf_counter()
print(math.pow(2, 2))

finaltime2 = time_period4 - time_period3

print(finaltime2)

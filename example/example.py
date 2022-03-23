
import time 
from winmutex import WinMutex 
from concurrent.futures import ThreadPoolExecutor

mutex = WinMutex()

def example (value):
  with mutex:
    for n in range(3):
      print(value)
      time.sleep(1)

with ThreadPoolExecutor() as executor:
  for n in range(3):
    executor.submit(example, n)

mutex.close()


import time 
from winmutex import WinMutex 
from multiprocessing import freeze_support
from concurrent.futures import ProcessPoolExecutor

def example (value):
  mutex = WinMutex(name="example")
  with mutex:
    for n in range(3):
      print(value)
      time.sleep(1)
  mutex.close()

if __name__ == "__main__": 
  freeze_support()
  with ProcessPoolExecutor() as executor:
    for n in range(3):
      executor.submit(example, n)

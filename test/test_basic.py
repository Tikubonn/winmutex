
import time 
from winmutex import WinMutex 
from unittest import TestCase
from threading import Thread

class TestBasic (TestCase):

  def test_basic1 (self):

    REPEAT_COUNT = 3
    THREAD_COUNT = 3

    mutex = WinMutex()
    stack = list()

    def example (value):
      with mutex:
        for n in range(REPEAT_COUNT):
          stack.append(value)
          time.sleep(1)

    threads = list()
    for n in range(THREAD_COUNT):
      thread = Thread(target=example, args=(n,))
      threads.append(thread)
    for thread in threads:
      thread.start()
    for thread in threads:
      thread.join()    

    for index in range(0, REPEAT_COUNT * THREAD_COUNT, 3):
      for ind in range(index, index +3):
        self.assertEqual(stack[index], stack[ind])

    mutex.close()

  def test_basic2 (self):

    REPEAT_COUNT = 3
    THREAD_COUNT = 3

    mutex = WinMutex()
    stack = list()

    def example (value):
      while not mutex.acquire(blocking=False, timeout=0): 
        time.sleep(0)
      for n in range(REPEAT_COUNT):
        stack.append(value)
        time.sleep(1)
      mutex.release()

    threads = list()
    for n in range(THREAD_COUNT):
      thread = Thread(target=example, args=(n,))
      threads.append(thread)
    for thread in threads:
      thread.start()
    for thread in threads:
      thread.join()    

    for index in range(0, REPEAT_COUNT * THREAD_COUNT, 3):
      for ind in range(index, index +3):
        self.assertEqual(stack[index], stack[ind])

    mutex.close()


import time 
from winmutex import WinMutex 
from unittest import TestCase
from threading import Thread

class TestNamedMutex (TestCase):

  def test_named_mutex1 (self):

    REPEAT_COUNT = 3
    THREAD_COUNT = 3

    stack = list()

    def example (value):
      mutex = WinMutex(name="example")
      with mutex:
        for n in range(REPEAT_COUNT):
          stack.append(value)
          time.sleep(1)
      mutex.close()

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

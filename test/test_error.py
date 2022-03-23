
import time 
from winmutex import WinMutex, WinMutexAbandonedError
from unittest import TestCase
from threading import Thread

class TestError (TestCase):

  def test_abandoned_error1 (self):

    mutex = WinMutex()

    def example ():
      mutex.acquire(blocking=True)

    thread = Thread(target=example)
    thread.start()
    thread.join()

    self.assertRaises(WinMutexAbandonedError, mutex.acquire, blocking=True)

    mutex.close()

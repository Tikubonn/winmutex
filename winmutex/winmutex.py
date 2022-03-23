
from ctypes import windll

def raise_os_error ():
  lasterror = windll.Kernel32.GetLastError()
  raise OSError(-1, "Error was caused in OS. GetLastError's value is {}".format(lasterror), lasterror)

class WinMutexAbandonedError (Exception):

  pass

class WinMutex:

  def __init__ (self, *, mutexAttributes=None, name=None):
    self.mutexAttributes = mutexAttributes
    self.name = name
    self.mutex = self.create_mutex(mutexAttributes, name)

  def create_mutex (self, mutexAttributes, name):
    mutex = windll.Kernel32.CreateMutexA(mutexAttributes, False, name)
    if mutex is None:
      raise_os_error()
    return mutex

  def __enter__ (self):
    self.acquire(blocking=True)
    return self

  def __exit__ (self, errortype, errorvalue, backtrace):
    self.release()
    return False 

  def close (self):
    returncode = windll.Kernel32.CloseHandle(self.mutex)
    if returncode == 0:
      raise_os_error()

  def acquire (self, blocking=True, timeout=-1):
    tmout = 0
    if blocking:
      tmout = timeout
    returncode = windll.Kernel32.WaitForSingleObject(self.mutex, tmout)
    if returncode == 0x00000080: #WAIT_ABANDONED
      raise WinMutexAbandonedError("Mutex has never been released until owner die.") #error
    elif returncode == 0x00000000: #WAIT_OBJECT_0
      return True 
    elif returncode == 0x00000102: #WAIT_TIMEOUT
      return False 
    elif returncode == 0xffffffff: #WAIT_FAILED #-1 is better?
      raise_os_error()
    else:
      raise ValueError("WaitForSingleObject returned unknown value. <= {}".format(returncode)) #error

  def release (self):
    returncode = windll.Kernel32.ReleaseMutex(self.mutex)
    if returncode == 0:
      raise_os_error()

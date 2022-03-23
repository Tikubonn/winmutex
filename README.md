
# winmutex 

PythonにWindowsAPIのミューテックスを提供するライブラリです。
もともとは自家製ソフトの多重起動防止用に書いたものなので最低限の機能しか含まれていません。

## Usage 

WinMutexインスタンスを作成することでWindowsAPIのミューテックスを使用することができます。
ただし、後述する名前付きミューテックスを利用しない場合には素直に`threading.Lock`を使用したほうがよいでしょう。
`locked`関数がない以外はほとんど`threading.Lock`と同じです。

```py
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
```

WinMutexインスタンス作成時、引数`name`に文字列をあたえることで名前付きミューテックスを作成することができます。
名前付きミューテックスはプロセスを跨いで共有されるようなので、例えばプログラムの多重起動を防止する場合などに利用できます。

https://docs.microsoft.com/ja-jp/windows/win32/api/synchapi/nf-synchapi-createmutexa

```py
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
```

##

## Install 

```sh
python setup.py install test
````

## License 

winmutex released under [MIT License](LICENSE).

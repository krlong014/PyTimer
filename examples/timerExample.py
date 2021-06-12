from PyTimer import Timer
from PyTab import Tab
import time

def f1():
  timer = Timer('f1')
  tab = Tab()
  tab1 = Tab()
  timer.start()
  print(tab, 'In f1')

  for x in range(4):
      time.sleep(0.3)
      print(tab1, 'x=%g' % x)

  print(tab, 'Calling f2')
  f2()
  timer.stop()

def f2():
  timer = Timer('f2')
  tab = Tab()
  timer.start()
  time.sleep(0.1)
  print(tab, 'In f2')
  timer.stop()

def main():
  tab = Tab()
  timer = Timer('main')
  timer.start()

  print(tab, 'starting test')
  f1()
  print(tab, 'done test')
  timer.stop()

if __name__=='__main__':
  main()
  Timer.report()

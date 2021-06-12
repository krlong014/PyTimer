import time

class Timer:

    _timers = {}

    def __init__(self, name):
        if name not in Timer._timers:
            Timer._timers[name] = 0
        self._name = name

    def start(self):
        self._curStart = time.perf_counter()

    def stop(self):
        Timer._timers[self._name] += time.perf_counter() - self._curStart

    def report():
        print('\n------- Timing summary ------\n')

        # find the maximum name length to set field width
        maxLen = 0
        for k in Timer._timers.keys():
            if len(k) > maxLen: maxLen = len(k)

        f = '%{}s %12.5g'.format(maxLen+4)
        for k,v in Timer._timers.items():
            print(f % (k,v))
        print('\n-----------------------------')

import queue
import threading

import numpy


# e = threading.Event()


class CalculationThread(threading.Thread):
    def __init__(self,
                 initial_data: numpy.ndarray,
                 generations_per_second_change_event: threading.Event,
                 generations_per_second_queue: queue.Queue,
                 finished_world_queue: queue.Queue):
        threading.Thread.__init__(self)

        pass

    def run(self):
        pass
#         print("hi, this is thread #%s and i'm sleeping :)" % self.xxx)
#         event_was_set: bool = e.wait(timeout=self.xxx)
#         print("event was set = %s" % event_was_set)
#
#
# class NotifyThread(threading.Thread):
#     def __init__(self, xxx):
#         threading.Thread.__init__(self)
#         self.xxx = xxx
#
#     def run(self):
#         time.sleep(self.xxx)
#         print("hi, this is thread #%s and after sleeping i wake the other thread up!" % self.xxx)
#         e.set()
#
#
# list = [4, 3, 2, 1, 2, 3, 4]
#
#
# def foo(row, column) -> bool:
#     return list[row] == column
#
#
# func_foo: function = foo
#
# CalculationThread(20).start()
# NotifyThread(25).start()
#
# x = numpy.zeros((3, 4))
#
# print(x)

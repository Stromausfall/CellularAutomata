import queue
import threading

import numpy

from cellularautomata.logic import calculationthread


class CalculationInteraction:
    def __init__(self, initial_world: numpy.ndarray):
        # create the event that allows to communicate with the thread that the generations per seconds should be changed
        self.__generations_per_second_change_event: threading.Event = threading.Event()
        # create the queues that allow to move data between the main thread and the CalculationThread
        self.__generations_per_second_queue: queue.Queue = queue.Queue()
        self.__finished_world_queue: queue.Queue = queue.Queue()
        self.__newest_world = initial_world

        # instantiate the CalculationThread
        self.__calculation_thread = calculationthread.CalculationThread(initial_world,
                                                                        self.__generations_per_second_change_event,
                                                                        self.__generations_per_second_queue,
                                                                        self.__finished_world_queue)

        # and start the calculation thread
        self.__calculation_thread.start()

    def change_generations_per_second(self, generations_per_second: float) -> None:
        # add generations per second to the queue
        self.__generations_per_second_queue.put_nowait(generations_per_second)

        # notify the event
        self.__generations_per_second_change_event.set()

    def get_newest_world(self) -> numpy.ndarray:
        # get the newest world data from the queue (if any new one was created)
        while not self.__finished_world_queue.empty():
            self.__newest_world = self.__finished_world_queue.get_nowait()

        return self.__newest_world

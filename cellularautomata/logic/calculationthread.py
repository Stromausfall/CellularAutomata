import queue
import threading

import numpy


class CalculationThread(threading.Thread):
    def __init__(self,
                 initial_data: numpy.ndarray,
                 generations_per_second_change_event: threading.Event,
                 generations_per_second_queue: queue.Queue,
                 finished_world_queue: queue.Queue):
        # this should be a daemon tread (it alone doesn't keep the program alive)
        threading.Thread.__init__(self, daemon=True)

        self.__current_world: numpy.ndarray = initial_data
        self.__generations_per_second_change_event: threading.Event = generations_per_second_change_event
        self.__generations_per_second_queue: queue.Queue = generations_per_second_queue
        self.__finished_world_queue: queue.Queue = finished_world_queue
        self.__wait_time: int = 0

    def __pause_until_next_generation(self):
        # get the latest wait time
        while not self.__generations_per_second_queue.empty():
            self.__wait_time = self.__generations_per_second_queue.get_nowait()

        disrupted_wait: bool = False

        if self.__wait_time == 0:
            disrupted_wait = self.__generations_per_second_change_event.wait()
        else:
            disrupted_wait = self.__generations_per_second_change_event.wait(1 / self.__wait_time)

        # finished waiting - clear the event
        self.__generations_per_second_change_event.clear()

        # if the wait was disrupted - wait again !
        if disrupted_wait:
            self.__pause_until_next_generation()

    def run(self):
        while True:
            # wait
            self.__pause_until_next_generation()

            # calculate the new world
            self.__current_world = self.calculate_new_world(self.__current_world)

            # push the new world into the queue
            self.__finished_world_queue.put_nowait(self.__current_world)

    def get_cell_wrapped_around(self, world: numpy.ndarray, x: int, y: int) -> bool:
        # handle wrap around for x
        if x == world.shape[0]:
            x = 0
        if x == -1:
            x = world.shape[0] - 1

        # handle wrap around for y
        if y == world.shape[1]:
            y = 0
        if y == -1:
            y = world.shape[1] - 1

        return world[x][y]

    def get_neighbor_coordinates(self, x: int, y: int) -> list:
        result = []

        for neighbor_x in range(x - 1, x + 2):
            for neighbor_y in range(y - 1, y + 2):
                result += [(neighbor_x, neighbor_y)]

        result.remove((x, y))

        return result

    def calculate_number_of_live_cells(self, world: numpy.ndarray, x: int, y: int) -> int:
        neighbor_coordinates = self.get_neighbor_coordinates(x, y)
        neighbor_alive = [self.get_cell_wrapped_around(world, coordinates[0], coordinates[1]) for coordinates in
                          neighbor_coordinates]

        return neighbor_alive.count(True)

    def is_cell_alive(self, world: numpy.ndarray, x: int, y: int):
        alive_neighbors: int = self.calculate_number_of_live_cells(world, x, y)
        is_currently_alive: bool = world[x][y]

        if is_currently_alive:
            if alive_neighbors < 2:
                # cell dies of starvation
                return False
            elif alive_neighbors in [2, 3]:
                # with 2 or 3 alive neighbors the cell continues to live
                return True
            else:
                # the cell dies of overpopulation (more than 3 alive neighbors
                return False
        else:
            if alive_neighbors == 3:
                # cell becomes alive through reproduction
                return True
            else:
                # cell stays dead
                return False

    def calculate_new_world(self, old_world: numpy.ndarray) -> numpy.ndarray:
        new_world: numpy.ndarray = numpy.empty(shape=old_world.shape)
        new_world.fill(False)

        for x in range(new_world.shape[0]):
            for y in range(new_world.shape[1]):
                new_world[x][y] = self.is_cell_alive(old_world, x, y)

        return new_world

import queue
import threading
from unittest import mock
from unittest.mock import MagicMock

import numpy

from cellularautomata.logic.calculationinteraction import CalculationInteraction


@mock.patch("cellularautomata.logic.calculationthread.CalculationThread")
def test_that_the_constructor_creates_and_starts_a_calculationthread(calculation_thread_constructor_call: MagicMock):
    ## given
    calculation_thread_start_call = MagicMock()
    initial_world: numpy.ndarray = numpy.array(([0, 1], [0, 0]))
    calculation_thread: MagicMock = MagicMock()
    calculation_thread.start = calculation_thread_start_call

    calculation_thread_constructor_call.return_value = calculation_thread

    ## when
    CalculationInteraction(initial_world)

    ## then
    # - test that the constructor was called
    calculation_thread_constructor_call.assert_called()

    # - test that the constructor arguments are correct

    # get the arguments the constructor was called with
    constructor_call_args: tuple = calculation_thread_constructor_call.call_args[0]

    # check the arguments
    assert constructor_call_args[0] is initial_world
    assert type(constructor_call_args[1]) == threading.Event
    assert type(constructor_call_args[2]) == queue.Queue
    assert type(constructor_call_args[3]) == queue.Queue

    # - test that the constructed CalculationThread is started
    calculation_thread_start_call.assert_called()


@mock.patch("cellularautomata.logic.calculationthread.CalculationThread")
def test_that_the_get_newest_world_method_first_returns_the_initial_world(
        calculation_thread_constructor_call: MagicMock):
    ## given
    calculation_thread_start_call = MagicMock()
    initial_world: numpy.ndarray = numpy.array(([0, 1], [0, 0]))
    calculation_thread: MagicMock = MagicMock()
    calculation_thread.start = calculation_thread_start_call

    calculation_thread_constructor_call.return_value = calculation_thread
    class_under_test: CalculationInteraction = CalculationInteraction(initial_world)

    ## when
    result1: numpy.ndarray = class_under_test.get_newest_world()
    result2: numpy.ndarray = class_under_test.get_newest_world()
    result3: numpy.ndarray = class_under_test.get_newest_world()

    ## then
    assert result1 is initial_world
    assert result2 is initial_world
    assert result3 is initial_world


@mock.patch("cellularautomata.logic.calculationthread.CalculationThread")
def test_that_new_world_data_created_by_the_thread_is_used(calculation_thread_constructor_call: MagicMock):
    ## given
    calculation_thread_start_call = MagicMock()
    initial_world: numpy.ndarray = numpy.array(([0, 1], [0, 0]))
    calculation_thread: MagicMock = MagicMock()
    calculation_thread.start = calculation_thread_start_call

    calculation_thread_constructor_call.return_value = calculation_thread
    class_under_test: CalculationInteraction = CalculationInteraction(initial_world)

    constructor_call_args: tuple = calculation_thread_constructor_call.call_args[0]
    # get the new_world_queue that is passed to the CalculationThread
    new_world_queue:queue.Queue = constructor_call_args[3]
    new_world: numpy.ndarray = numpy.array(([1, 1], [0, 0]))

    ## when simulating that the thread finished calculating a new world - we should be able to retrieve it
    result_before_calculation: numpy.ndarray = class_under_test.get_newest_world()
    new_world_queue.put_nowait(new_world)
    result_after_calculation: numpy.ndarray = class_under_test.get_newest_world()

    ## then
    assert result_before_calculation is initial_world
    assert result_after_calculation is new_world

@mock.patch("cellularautomata.logic.calculationthread.CalculationThread")
def test_that_only_ever_the_newest_new_world_data_created_by_the_thread_is_used(calculation_thread_constructor_call: MagicMock):
    ## given
    calculation_thread_start_call = MagicMock()
    initial_world: numpy.ndarray = numpy.array(([0, 1], [0, 0]))
    calculation_thread: MagicMock = MagicMock()
    calculation_thread.start = calculation_thread_start_call

    calculation_thread_constructor_call.return_value = calculation_thread
    class_under_test: CalculationInteraction = CalculationInteraction(initial_world)

    constructor_call_args: tuple = calculation_thread_constructor_call.call_args[0]
    # get the new_world_queue that is passed to the CalculationThread
    new_world_queue:queue.Queue = constructor_call_args[3]
    new_world_1: numpy.ndarray = numpy.array(([1, 1], [0, 0]))
    new_world_2: numpy.ndarray = numpy.array(([1, 1], [0, 1]))

    ## when simulating that the thread finished calculating a new world - we should be able to retrieve it
    result_before_calculation: numpy.ndarray = class_under_test.get_newest_world()
    new_world_queue.put_nowait(new_world_1)
    new_world_queue.put_nowait(new_world_2)
    result_after_calculation: numpy.ndarray = class_under_test.get_newest_world()

    ## then
    assert result_before_calculation is initial_world
    assert result_after_calculation is new_world_2

@mock.patch("cellularautomata.logic.calculationthread.CalculationThread")
def test_that_generations_per_second_is_correctly_forwarded_to_the_thread_via_the_queue_and_the_event_is_set(calculation_thread_constructor_call: MagicMock):
    ## given
    calculation_thread_start_call = MagicMock()
    initial_world: numpy.ndarray = numpy.array(([0, 1], [0, 0]))
    calculation_thread: MagicMock = MagicMock()
    calculation_thread.start = calculation_thread_start_call

    calculation_thread_constructor_call.return_value = calculation_thread
    class_under_test: CalculationInteraction = CalculationInteraction(initial_world)

    constructor_call_args: tuple = calculation_thread_constructor_call.call_args[0]
    # get the new_world_queue that is passed to the CalculationThread
    new_world_queue:queue.Queue = constructor_call_args[3]
    new_world_1: numpy.ndarray = numpy.array(([1, 1], [0, 0]))
    new_world_2: numpy.ndarray = numpy.array(([1, 1], [0, 1]))

    ## when simulating that the thread finished calculating a new world - we should be able to retrieve it
    result_before_calculation: numpy.ndarray = class_under_test.get_newest_world()
    new_world_queue.put_nowait(new_world_1)
    new_world_queue.put_nowait(new_world_2)
    result_after_calculation: numpy.ndarray = class_under_test.get_newest_world()

    ## then
    assert result_before_calculation is initial_world
    assert result_after_calculation is new_world_2

@mock.patch("cellularautomata.logic.calculationthread.CalculationThread")
def test_that_generations_per_second_is_correctly_forwarded_to_the_thread_via_the_queue_and_the_event_is_set_accordingly(calculation_thread_constructor_call: MagicMock):
    ## given
    calculation_thread_start_call = MagicMock()
    initial_world: numpy.ndarray = numpy.array(([0, 1], [0, 0]))
    calculation_thread: MagicMock = MagicMock()
    calculation_thread.start = calculation_thread_start_call

    calculation_thread_constructor_call.return_value = calculation_thread
    class_under_test: CalculationInteraction = CalculationInteraction(initial_world)

    constructor_call_args: tuple = calculation_thread_constructor_call.call_args[0]
    generations_per_second_event:threading.Event = constructor_call_args[1]
    generations_per_second_queue:queue.Queue = constructor_call_args[2]
    generations_per_second:float = 0.4

    ## prerequisites
    assert not generations_per_second_event.is_set()
    assert generations_per_second_queue.empty()

    ## when
    class_under_test.change_generations_per_second(generations_per_second)

    ## then
    assert generations_per_second_event.is_set()
    assert generations_per_second_queue.get_nowait() is generations_per_second

# actuator
import logging
logging.basicConfig()
log = logging.getLogger()
log.setLevel(logging.DEBUG)

from enum import Enum
class ActStatus(Enum):
    OFF = 1
    ON = 2

from threading import Timer
import numpy as np
class Actuators():
    def __init__(self, num):
        self.actuator_num = num
        self.status = ActStatus.OFF
        self.values = np.zeros(num, dtype=float)

    def __timer_tick(self):
        if self.status is ActStatus.ON:

            print('tick')
            for idx in range(self.values.shape[0]):
                self.values[idx] += 1
                print('idx: {0} with value: {1}'.format(idx, self.values[idx]))

            timer = Timer(2, self.__timer_tick)
            timer.start()

    def start(self) -> bool:
        if self.status is ActStatus.ON:
            log.debug('timer already exist')
            return False

        print('start')
        timer = Timer(2, self.__timer_tick)
        self.status = ActStatus.ON
        timer.start()
        return True

    def stop(self) -> bool:
        self.status = ActStatus.OFF
        return True

    def get_actuator_value(self):
        return self.values

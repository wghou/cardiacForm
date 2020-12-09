# io module
# modbus 模拟量采集输入输出4-20mA0-10v转485模块232串口PLC扩展IO
# 标控电气

import logging
logging.basicConfig()
log = logging.getLogger()
log.setLevel(logging.DEBUG)

from enum import Enum
class RelayOut(Enum):
    Rely_1 = 1
    Rely_2 = 2
    Rely_3 = 3
    Rely_4 = 4

class DA_Out(Enum):
    DA_1 = 1
    DA_2 = 2


UNIT = 0x01

from pymodbus.client.sync import ModbusSerialClient as ModbusClient
class IOModeule():
    def __init__(self):
        self.port = None
        self.client = None
        self.initialized = False

    def __del__(self):
        if self.client is not None:
            self.client.close()
            self.client = None

    def init(self, port):
        self.port = port
        self.initialized = False

        if self.client is not None:
            self.client.close()
            self.client = None

        self.client = ModbusClient(method='rtu', port=self.port, baudrate=9600, timeout=0.5)

        import serial
        try:
            self.client.connect()
        except serial.SerialException as msg:
            log.error("cannot open the serial port: {0}".format(msg))
            self.client = None
            self.initialized = False
            return False

        self.initialized = True
        return True

    def write_relay(self, relay: RelayOut, status: bool):

        if self.initialized is False:
            log.debug("IO Module un intialized.")
            return False

        rlt = self.client.write_coil(relay, status, unit=UNIT)
        log.debug(rlt)
        return True

    def write_analogy_signal(self, channel: DA_Out, value: float):

        if self.initialized is False:
            log.debug("IO Module un intialized.")
            return False

        rlt = self.client.write_register()
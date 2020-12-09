# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
import mainForm
from IOMoudle import *
from Actuator import Actuators

module = IOModeule()
act = Actuators(2)


def click_success(checked):
    print('checked = {0}'.format(checked))
    try:
        module.write_relay(relay=RelayOut.Rely_1, status=checked)
    except:
        print('exception when write relay status to io module')


def click_suspend(checked):
    print('checked = {0}'.format(checked))
    act.start()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    rlt = module.init(port='COM1')
    if rlt is not True:
        print('error when init io module')
        exit(-1)

    app = QApplication(sys.argv)
    mainWindow = QMainWindow()
    ui = mainForm.Ui_MainWindow()
    ui.setupUi(MainWindow=mainWindow)
    mainWindow.show()
    ui.pushButton_start.clicked.connect(click_success)
    ui.pushButton_suspend.clicked.connect(click_suspend)
    while app.exec_():
        pass
    act.stop()
    sys.exit(0)
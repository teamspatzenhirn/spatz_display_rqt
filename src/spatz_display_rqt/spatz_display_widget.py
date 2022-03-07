import os

from PyQt5.QtCore import (pyqtSlot)
from PyQt5.QtWidgets import QWidget
from PyQt5.uic import loadUi
from ament_index_python import get_resource


class DisplayWidget(QWidget):

    def __init__(self):
        super(DisplayWidget, self).__init__()
        _, package_path = get_resource('packages', 'spatz_display_rqt')
        ui_file = os.path.join(package_path, 'share', 'spatz_display_rqt', 'resource', 'display.ui')
        loadUi(ui_file, self)

    @pyqtSlot()
    def on_go_button_clicked(self):
        print("Go!")

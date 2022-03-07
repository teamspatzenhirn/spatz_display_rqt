import os
from typing import Dict

import spatz_display_rqt.generated.hwhealth_pb2 as hwhealth_pb2
from PyQt5.QtCore import pyqtSlot, Qt
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QCheckBox
from PyQt5.uic import loadUi
from ament_index_python import get_resource


class DisplayWidget(QWidget):

    def __init__(self):
        super(DisplayWidget, self).__init__()
        _, package_path = get_resource('packages', 'spatz_display_rqt')
        ui_file = os.path.join(package_path, 'share', 'spatz_display_rqt', 'resource', 'display.ui')
        loadUi(ui_file, self)
        self.hw_health_checkboxes: Dict[str, QCheckBox] = {}
        hwhealth = hwhealth_pb2.HwHealth()
        hwhealth.indicator_front = True
        hwhealth.gyro = False
        hwhealth.vesc_tx_rear_right = False
        hwhealth.vesc_rx_rear_right = True
        print(hwhealth.SerializeToString())
        self.update_hw_status(b'8\x01')

    @pyqtSlot()
    def on_go_button_clicked(self):
        print("Go!")
        self.update_hw_status(b'8\x01\xa0\x01\x01')

    def update_hw_status(self, data):
        hw_health = hwhealth_pb2.HwHealth()
        hw_health.ParseFromString(data)

        fields = [fd.name for fd in hw_health.DESCRIPTOR.fields]
        layout: QVBoxLayout = self.hardware_status_layout
        for field_name in fields:
            value = getattr(hw_health, field_name)
            if not isinstance(value, bool):
                print(f"Field {field_name} in hw status message is not boolean! Value: {value}")
                continue
            if field_name in self.hw_health_checkboxes:
                checkbox = self.hw_health_checkboxes[field_name]
            else:
                checkbox = QCheckBox(field_name)
                checkbox.setAttribute(Qt.WA_TransparentForMouseEvents)
                checkbox.setFocusPolicy(Qt.NoFocus)
                layout.insertWidget(layout.count() - 1, checkbox)
                self.hw_health_checkboxes[field_name] = checkbox

            checkbox.setChecked(value)

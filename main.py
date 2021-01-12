# -*- coding: utf-8 -*-
"""
A demo Bluetooth BLE communication program based on Bluepy and Pyqt5.

The Bluetooth BLE board is Silicon Labs ThunderBoard BG22.

Project is created by QuanQuan-BG3MDO

24 Dec 2020 in Cambridge UK. Merry XMas!
"""
import sys
from PyQt5 import QtCore, QtWidgets
from bluepy import btle
import time
import struct
from smartblue_ui import Ui_SmartBlueForm


class BlueBase:
    def __init__(self, mac_add=None, msg=0):
        print("Quanquan: BlueBase is started!")
        self.mac_add = mac_add
        self.msg = msg
        if msg:
            print(" - Board MAC is set as: " + mac_add)

        print(" - Now waiting for Bluetooth board...")

        self.board = btle.Peripheral(mac_add)

        self.loop_work = False
        self.led_status = 0

        self.temp_val = 0
        self.hum_val = 0
        self.lux_val = 0

    def disp_services(self):
        print(" - Services as follows:")
        for svc in self.board.getServices():
            print(str(svc))

    def disp_descriptors(self):
        print(" - Descriptors as follows:")
        for desc in self.board.getDescriptors():
            print(str(desc))

    def set_led(self, led_status=0):
        self.led_status = led_status

    def get_env_data(self):
        return self.temp_val, self.hum_val, self.lux_val

    def stop_proc(self):
        self.loop_work = False

    def is_proc(self):
        return self.loop_work

    def proc_data_loop(self, period=2):
        if self.msg:
            print(" - Deal with data from BLE Characteristics...")
        self.loop_work = True
        self.led_status = 0
        while self.loop_work:
            if self.msg:
                print("-" * 50)
            for k in self.board.getCharacteristics():
                if str(k.uuid) == "00002a6e-0000-1000-8000-00805f9b34fb":
                    temp_val = struct.unpack('<H', k.read())[0] / 100
                    if self.msg:
                        print("   - Received temperature reading: "
                              + str(temp_val) + " C")
                    self.temp_val = temp_val

                if str(k.uuid) == "c8546913-bfd9-45eb-8dde-9f8754f4a32e":
                    lux_val = struct.unpack('<L', k.read())[0] / 100
                    if self.msg:
                        print("   - Received ambient light reading: "
                              + str(lux_val) + " Lux")
                    self.lux_val = lux_val

                if str(k.uuid) == "00002a6f-0000-1000-8000-00805f9b34fb":
                    hum_val = struct.unpack('<H', k.read())[0] / 100
                    if self.msg:
                        print("   - Received humidity reading: "
                              + str(hum_val) + " %RH")
                    self.hum_val = hum_val

                if str(k.uuid) == "00002a56-0000-1000-8000-00805f9b34fb":
                    try:
                        if self.led_status:
                            k.write(struct.pack('<B', 1), True)
                        else:
                            k.write(struct.pack('<B', 0), True)
                        if self.msg:
                            print("   - Setting LED status")
                    except:
                        pass

            time.sleep(period)


class BlueThread(QtCore.QThread):
    def __init__(self, blue_base, parent=None):
        super(BlueThread, self).__init__(parent)
        self.blue_base = blue_base

    def run(self):
        self.blue_base.proc_data_loop()


class UiSmartBlue(QtWidgets.QDialog, Ui_SmartBlueForm):
    def __init__(self, ble_mac="84:2e:14:31:b3:84", parent=None):
        super(UiSmartBlue, self).__init__(parent)
        self.setupUi(self)
        self.ble_mac = ble_mac
        self.gui_init()

        self.blue_base = None
        self.blue_thread = None

    def gui_init(self):
        self.buttonStart.clicked.connect(self.start_event)
        self.buttonStop.clicked.connect(self.stop_event)
        self.buttonStop.setDisabled(True)

    def start_event(self):
        if self.blue_base is None:
            self.blue_base = BlueBase(self.ble_mac, msg=0)
            self.blue_thread = BlueThread(blue_base=self.blue_base)
            self.blue_thread.start()
        else:
            self.blue_thread.start()

        self.buttonStart.setDisabled(True)
        self.buttonStop.setEnabled(True)

        print(" - Data collection started.")

        while True:
            QtWidgets.QApplication.processEvents()
            temp_val, hum_val, lux_val = self.blue_base.get_env_data()
            self.lineEditTemp.setText(str(temp_val))
            self.lineEditLight.setText(str(lux_val))
            self.lineEditHumidity.setText(str(hum_val))

            temp_th = int(self.spinBoxTemp.text())

            if temp_val >= temp_th:
                self.lineEditTempLED.setText("ON")
                self.blue_base.set_led(led_status=1)
            else:
                self.lineEditTempLED.setText("OFF")
                self.blue_base.set_led(led_status=0)

            time.sleep(0.1)

            if not self.blue_base.is_proc():
                break

    def stop_event(self):
        self.blue_base.stop_proc()
        self.buttonStop.setDisabled(True)
        self.buttonStart.setEnabled(True)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    ui = UiSmartBlue(ble_mac="84:2e:14:31:b3:84")
    ui.move(100, 100)
    ui.show()
    sys.exit(app.exec_())

'''
This module is the client side of our program.
'''
import argparse
import sys
from socket import socket, error as socket_error

import pickle
from PySide6.QtWidgets import QApplication, QPushButton, QMainWindow, QFrame
from PySide6.QtWidgets import QVBoxLayout, QLineEdit, QLabel, QGridLayout, QErrorMessage
from list_widget import MegaList

MAX_PORT = 0xffff
MIN_PORT = 0
class LabelLayout(QGridLayout):
    """ Customied widget extend from QGridLayout.
        This widget contains serval label and entry with organized position.
        Each entry can use 'enter' key as to click the submit button 
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.line_l = QLineEdit()
        self.label_l = QLabel("Label")
        self.line_c = QLineEdit()
        self.label_c = QLabel('Classifier')
        self.line_a = QLineEdit()
        self.label_a = QLabel("Agent")
        self.line_d = QLineEdit()
        self.label_d = QLabel("Department")

        self.addWidget(self.label_l, 0, 0)
        self.addWidget(self.line_l, 0, 1)
        self.addWidget(self.label_c, 0, 2)
        self.addWidget(self.line_c, 0, 3)
        self.addWidget(self.label_a, 1, 0)
        self.addWidget(self.line_a, 1, 1)
        self.addWidget(self.label_d, 1, 2)
        self.addWidget(self.line_d, 1, 3)

        self.type_list = [self.line_l, self.line_c, self.line_a, self.line_d]
        self.label_list = [self.label_l, self.label_c, self.label_a, self.label_d]

class Gui(QMainWindow):
    """ Main gui window
    
        NOTICE: For button, please press 'space' or mouse click to trigger the event.
                For entry, please press 'enter' to submit and 'tab' to cycle if keyboard 
                allowed only. 
    """
    def __init__(self):
        super().__init__()

        parser = argparse.ArgumentParser(allow_abbrev=False,
                                         description = "Client for the YUAG application")
        parser.add_argument("string",metavar = "host",
                            help = "the host on which the server is running")
        parser.add_argument("integer",metavar = "port",
                            help = "the port at which the server is listening")
        args = parser.parse_args()
        if len(sys.argv) != 3:
            print(f'Usage: python {sys.argv[0]} host port' )
            sys.exit(1)
        try:
            port_num = int(args.integer)
        except ValueError:
            print("Invalid port number, make sure it is an integer")
            sys.exit(1)
        else:
            if port_num > MAX_PORT or port_num < MIN_PORT:
                print("Invalid port number, out of bound", file =sys.stderr)
                sys.exit(1)
        self._options_dict = {}
        self._option_list = []
        self._dat = None

        self._my_list_widget = MegaList(self)
        self._mybutton = QPushButton('Submit Query')
        self._my_layout = LabelLayout()

        self._l1 = QVBoxLayout()
        self._l1.addLayout(self._my_layout)
        self._l1.addWidget(self._mybutton)
        self._l1.addWidget(self._my_list_widget)

        self._frame = QFrame()
        self._frame.setLayout(self._l1)

        self.setWindowTitle("Lux")
        self.setCentralWidget(self._frame)
        self.show()

        col = 0
        for item in self._my_layout.type_list:
            item.returnPressed.connect(self._submit_callback)
            col += 1
        # use 'space' keyboard or mouse click to trigger callback
        self._mybutton.clicked.connect(self._submit_callback)


    # --------------------------------------------------------
    def _submit_callback(self):
        """ Button call back function """
        if len(self._my_layout.line_l.text()) > 0:
            self._options_dict["label"] = self._my_layout.line_l.text()
        if len(self._my_layout.line_c.text()) > 0:
            self._options_dict["cls"] = self._my_layout.line_c.text()
        if len(self._my_layout.line_a.text()) > 0:
            self._options_dict["agt"] = self._my_layout.line_a.text()
        if len(self._my_layout.line_d.text()) > 0:
            self._options_dict["dep"] = self._my_layout.line_d.text()
        for key, value in self._options_dict.items():
            if key is not None:
                self._option_list.append([key, value])
        self._options_dict.clear()

        try:
            host = sys.argv[1]
            port = int(sys.argv[2])

            with socket() as sock:
                # send msg to server
                try:
                    sock.connect((host, port)) #
                except socket_error:
                    err = QErrorMessage(self)
                    err.setWindowTitle("error")
                    err.showMessage("Something wrong with the connection, try later")
                    err.exec()
                flo = sock.makefile(mode = 'wb')
                pickle.dump(["object", self._option_list], flo)
                self._option_list.clear()
                # get msg from server, race condition?
                flo = sock.makefile(mode = "rb")
                self._dat = pickle.load(flo)

                self._my_list_widget.clear()
                row_ind = 0
                for row in self._dat:
                    self._my_list_widget.insertItem(row_ind, row[0])
                    row_ind += 1
                flo.flush()

        except Exception as ex:
            print(ex, file=sys.stderr)
            sys.exit(1)


# ------------------------------------------------------------
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Gui()
    screen_size = app.primaryScreen().availableGeometry()
    window.resize(screen_size.width()//2, screen_size.height()//2)
    sys.exit(app.exec())

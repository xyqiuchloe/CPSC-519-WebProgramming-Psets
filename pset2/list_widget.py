from PySide6.QtWidgets import QListWidget
from socket import socket
import pickle
import sys
import dialog
from dialog import FixedWidthMessageDialog
class MegaList(QListWidget):
    """ This is a mega widget which can show dialog while clicking on the list entry"""
    def __init__(self, window, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._window = window
        self.setFont(dialog.FW_FONT)
        self.setMinimumWidth(self.sizeHintForColumn(0))
        self.setWordWrap(False)
        self.selected = None

        self.itemActivated.connect(self.show_dialog)

    def show_dialog(self):
        """ call back for list entry"""
        try:
            host = sys.argv[1]
            port = int(sys.argv[2])

            with socket() as sock:
            # send msg to server
                self.selected = self.currentItem().text().split(" ", 1)[0]
                sock.connect((host, port))
                flo = sock.makefile(mode = 'wb')
                pickle.dump(["detail", self.selected], flo)
                # get msg from server, race condition?
                flo = sock.makefile(mode = "rb")
                self._dat = pickle.load(flo)

                # self.my_list_widget.clear()
                dlg = FixedWidthMessageDialog(f"Details for object {self.selected}", self._dat, parent = self._window)
                dlg.exec()  
                flo.flush()
        except Exception as ex:
            print(ex, file=sys.stderr)
            exit(1)

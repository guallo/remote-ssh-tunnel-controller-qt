import sys

from PySide2.QtCore import QTimer
from PySide2.QtWidgets import QApplication

from . import config

sys.path.extend(config.EXTRA_PATH)

from . import util
from .views import RSSHTControllerWindow


def main(argv):
    try:
        util.load_config()
    except IOError:
        pass
    app = QApplication(argv)
    window = RSSHTControllerWindow()
    window.show()
    QTimer.singleShot(0, lambda: window.startUpdater())
    status = app.exec_()
    return status

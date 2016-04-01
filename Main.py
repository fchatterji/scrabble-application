#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
from PyQt4 import QtGui
from GUI import Main


# ----------------------------#
# Main scrabble loop          # 
# ----------------------------#

def main():
    app = QtGui.QApplication(sys.argv)
    main = Main()
    main.show()

    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
    
#!/usr/bin/python
# -*- coding: utf-8 -*-

# ----------------------------#
# GUI interface               # 
# ----------------------------#

import sys
from PyQt4 import QtGui
from functions import BOARD, POINTS, on_click



class Main(QtGui.QMainWindow):
    
    def __init__(self):
        super(Main, self).__init__()
        self.filename = ""
        self.initUI()

    def initToolbar(self):
        self.newAction = QtGui.QAction(QtGui.QIcon("icons/new.png"),"New",self)
        self.newAction.setStatusTip("Create a new document from scratch.")
        self.newAction.setShortcut("Ctrl+N")
        self.newAction.triggered.connect(self.new)

        self.openAction = QtGui.QAction(QtGui.QIcon("icons/open.png"),"Open file",self)
        self.openAction.setStatusTip("Open existing document")
        self.openAction.setShortcut("Ctrl+O")
        self.openAction.triggered.connect(self.open)

        self.saveAction = QtGui.QAction(QtGui.QIcon("icons/save.png"),"Save",self)
        self.saveAction.setStatusTip("Save document")
        self.saveAction.setShortcut("Ctrl+S")
        self.saveAction.triggered.connect(self.save)

        self.printAction = QtGui.QAction(QtGui.QIcon("icons/print.png"),"Print document", self)
        self.printAction.setStatusTip("Print document")
        self.printAction.setShortcut("Ctrl+P")
        self.printAction.triggered.connect(self._print)

        self.previewAction = QtGui.QAction(QtGui.QIcon("icons/preview.png"),"Page view",self)
        self.previewAction.setStatusTip("Preview page before printing")
        self.previewAction.setShortcut("Ctrl+Shift+P")
        self.previewAction.triggered.connect(self.preview)

        
        self.toolbar = self.addToolBar("Options")

        self.toolbar.addAction(self.newAction)
        self.toolbar.addAction(self.openAction)
        self.toolbar.addAction(self.saveAction)
        self.toolbar.addSeparator()

        self.toolbar.addAction(self.printAction)
        self.toolbar.addAction(self.previewAction)
        self.toolbar.addSeparator()

        
    def initMenubar(self):
        menubar = self.menuBar()
        file = menubar.addMenu("File")
        edit = menubar.addMenu("Edit")
        view = menubar.addMenu("View")
        
        file.addAction(self.newAction)
        file.addAction(self.openAction)
        file.addAction(self.saveAction)
        file.addAction(self.printAction)
        file.addAction(self.previewAction)
        
    def initStatusbar(self):
        self.statusbar = self.statusBar()

    def initLayout(self):
        self.centralWidget = QtGui.QWidget()
        self.setCentralWidget(self.centralWidget)

        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setSpacing(0)

       
        self.centralWidget.setLayout(self.gridLayout)

        # setup the board and the different styles
        self.setStyleSheet(
            """
            QLineEdit
            {
            background: green;
            color:green;
            font-size:20px;
            margin: 0;
            padding: 0;
            border-width: 5px;
            }
            """)
     
        # extract names and positions from global variable board
        #(by default scrabble board)
        board = [(name, (i,j))
                for j, line in enumerate(BOARD)
                for i, name in enumerate(line)]

        for name, position in board:
            self.button = QtGui.QPushButton(name)
            self.button.clicked.connect(on_click(position))





            if name is "3":
                self.button.setStyleSheet(
                    "background-color: red;"
                    )
                
            elif name is "2":
                self.button.setStyleSheet(
                    "background-color: orange;"
                    )

            elif name is ";":
                self.button.setStyleSheet(
                    "background-color: darkblue;"
                    )

            elif name is ":":
                self.button.setStyleSheet(
                    "background-color: blue;"
                    )

            elif name is "*":
                self.button.setStyleSheet(
                    "background-color: yellow;"
                    )

            elif name is "|":
                self.button.setStyleSheet(
                    "background-color: brown;"
                    )
                
            self.gridLayout.addWidget(self.button, *position)
            



    def initUI(self):
        self.setWindowTitle("Scrabble")
        self.setWindowIcon(QtGui.QIcon("icons/icon.png"))
        
        self.initLayout()
        self.initToolbar()
        self.initMenubar()
        self.initStatusbar()


        

    def new(self):

        spawn = Main()
        spawn.show()

    def open(self):

        # Get filename and show only .scrabble files
        self.filename = QtGui.QFileDialog.getOpenFileName(self, 'Open File',".","(*.scrabble)")

        if self.filename:
            with open(self.filename,"rt") as file:
                pass

    def save(self):

        # Only open dialog if there is no filename yet
        if not self.filename:
            self.filename = QtGui.QFileDialog.getSaveFileName(self, 'Save File')

        # Append extension if not there yet
        if not self.filename.endsWith(".scrabble"):
            self.filename += ".scrabble"

        # We just store the contents of the text file along with the
        # format in html, which Qt does in a very nice way for us
        with open(self.filename,"wt") as file:
            for line in BOARD:
                file.write("{}\n".format(line) )


    def preview(self):

        # Open preview dialog
        preview = QtGui.QPrintPreviewDialog()

        # If a print is requested, open print dialog
        preview.paintRequested.connect(lambda p: self.text.print_(p))

        preview.exec_()

    def _print(self):

        # Open printing dialog
        dialog = QtGui.QPrintDialog()

        if dialog.exec_() == QtGui.QDialog.Accepted:
            self.text.document().print_(dialog.printer())

        

# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_main_black_jackOmlccD.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

import files_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(500, 500)
        MainWindow.setMinimumSize(QSize(500, 500))
        MainWindow.setStyleSheet(u"background-color: rgb(45, 45, 45);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.central_layout = QVBoxLayout(self.centralwidget)
        self.central_layout.setSpacing(0)
        self.central_layout.setObjectName(u"central_layout")
        self.central_layout.setContentsMargins(0, 0, 0, 0)
        self.top_bar = QFrame(self.centralwidget)
        self.top_bar.setObjectName(u"top_bar")
        self.top_bar.setMaximumSize(QSize(16777215, 50))
        self.top_bar.setAutoFillBackground(False)
        self.top_bar.setStyleSheet(u"\n"
"background-color: rgb(35, 35, 35);")
        self.top_bar.setFrameShape(QFrame.NoFrame)
        self.top_bar.setFrameShadow(QFrame.Raised)
        self.top_bar_layout = QHBoxLayout(self.top_bar)
        self.top_bar_layout.setSpacing(0)
        self.top_bar_layout.setObjectName(u"top_bar_layout")
        self.top_bar_layout.setContentsMargins(0, 0, 0, 0)
        self.frame_title = QFrame(self.top_bar)
        self.frame_title.setObjectName(u"frame_title")
        self.frame_title.setMinimumSize(QSize(0, 50))
        self.frame_title.setMaximumSize(QSize(16777215, 50))
        self.frame_title.setFrameShape(QFrame.NoFrame)
        self.frame_title.setFrameShadow(QFrame.Raised)
        self.frame_title_layout = QVBoxLayout(self.frame_title)
        self.frame_title_layout.setSpacing(0)
        self.frame_title_layout.setObjectName(u"frame_title_layout")
        self.frame_title_layout.setContentsMargins(0, 0, 0, 0)
        self.frame_title_top = QFrame(self.frame_title)
        self.frame_title_top.setObjectName(u"frame_title_top")
        self.frame_title_top.setMaximumSize(QSize(16777215, 30))
        self.frame_title_top.setFrameShape(QFrame.NoFrame)
        self.frame_title_top.setFrameShadow(QFrame.Raised)
        self.frame_title_top_layout = QHBoxLayout(self.frame_title_top)
        self.frame_title_top_layout.setSpacing(0)
        self.frame_title_top_layout.setObjectName(u"frame_title_top_layout")
        self.frame_title_top_layout.setContentsMargins(0, 0, 0, 0)
        self.frame_title_text = QFrame(self.frame_title_top)
        self.frame_title_text.setObjectName(u"frame_title_text")
        self.frame_title_text.setFrameShape(QFrame.NoFrame)
        self.frame_title_text.setFrameShadow(QFrame.Raised)
        self.frame_title_text_layout = QHBoxLayout(self.frame_title_text)
        self.frame_title_text_layout.setSpacing(0)
        self.frame_title_text_layout.setObjectName(u"frame_title_text_layout")
        self.frame_title_text_layout.setContentsMargins(0, 0, 0, 0)
        self.icon_title = QPushButton(self.frame_title_text)
        self.icon_title.setObjectName(u"icon_title")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.icon_title.sizePolicy().hasHeightForWidth())
        self.icon_title.setSizePolicy(sizePolicy)
        self.icon_title.setMaximumSize(QSize(30, 16777215))
        self.icon_title.setStyleSheet(u"border:0px solid;")
        icon = QIcon()
        icon.addFile(u":/icons/icons/16x16/cil-terminal.png", QSize(), QIcon.Normal, QIcon.Off)
        self.icon_title.setIcon(icon)

        self.frame_title_text_layout.addWidget(self.icon_title)

        self.label_title = QLabel(self.frame_title_text)
        self.label_title.setObjectName(u"label_title")
        font = QFont()
        font.setFamily(u"Segoe UI")
        self.label_title.setFont(font)
        self.label_title.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.frame_title_text_layout.addWidget(self.label_title)


        self.frame_title_top_layout.addWidget(self.frame_title_text)

        self.frame_buttons = QFrame(self.frame_title_top)
        self.frame_buttons.setObjectName(u"frame_buttons")
        self.frame_buttons.setMaximumSize(QSize(100, 16777215))
        self.frame_buttons.setFrameShape(QFrame.NoFrame)
        self.frame_buttons.setFrameShadow(QFrame.Raised)
        self.frame_buttons_layout = QHBoxLayout(self.frame_buttons)
        self.frame_buttons_layout.setSpacing(0)
        self.frame_buttons_layout.setObjectName(u"frame_buttons_layout")
        self.frame_buttons_layout.setContentsMargins(0, 0, 5, 0)
        self.button_minimize = QPushButton(self.frame_buttons)
        self.button_minimize.setObjectName(u"button_minimize")
        sizePolicy.setHeightForWidth(self.button_minimize.sizePolicy().hasHeightForWidth())
        self.button_minimize.setSizePolicy(sizePolicy)
        self.button_minimize.setStyleSheet(u"QPushButton{\n"
"	color: rgb(255, 255, 255);\n"
"	border:0px solid;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(200, 200, 200);\n"
"}\n"
"QPushButton:pressed{\n"
"	background-color: rgb(85, 170, 255);\n"
"}\n"
"")
        icon1 = QIcon()
        icon1.addFile(u":/icons/icons/16x16/cil-window-minimize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.button_minimize.setIcon(icon1)

        self.frame_buttons_layout.addWidget(self.button_minimize)

        self.button_close = QPushButton(self.frame_buttons)
        self.button_close.setObjectName(u"button_close")
        sizePolicy.setHeightForWidth(self.button_close.sizePolicy().hasHeightForWidth())
        self.button_close.setSizePolicy(sizePolicy)
        self.button_close.setStyleSheet(u"QPushButton{\n"
"	color: rgb(255, 255, 255);\n"
"	border:0px solid;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(200, 200, 200);\n"
"}\n"
"QPushButton:pressed{\n"
"	background-color: rgb(85, 170, 255);\n"
"}\n"
"")
        icon2 = QIcon()
        icon2.addFile(u":/icons/icons/16x16/cil-x.png", QSize(), QIcon.Normal, QIcon.Off)
        self.button_close.setIcon(icon2)

        self.frame_buttons_layout.addWidget(self.button_close)


        self.frame_title_top_layout.addWidget(self.frame_buttons)


        self.frame_title_layout.addWidget(self.frame_title_top)

        self.frame_title_bottom = QFrame(self.frame_title)
        self.frame_title_bottom.setObjectName(u"frame_title_bottom")
        self.frame_title_bottom.setMaximumSize(QSize(16777215, 20))
        self.frame_title_bottom.setStyleSheet(u"background-color: rgb(40, 40, 40);")
        self.frame_title_bottom.setFrameShape(QFrame.NoFrame)
        self.frame_title_bottom.setFrameShadow(QFrame.Raised)
        self.frame_title_bottom_layout = QVBoxLayout(self.frame_title_bottom)
        self.frame_title_bottom_layout.setSpacing(0)
        self.frame_title_bottom_layout.setObjectName(u"frame_title_bottom_layout")
        self.frame_title_bottom_layout.setContentsMargins(0, 0, 5, 0)
        self.label_page = QLabel(self.frame_title_bottom)
        self.label_page.setObjectName(u"label_page")
        font1 = QFont()
        font1.setFamily(u"Segoe UI")
        font1.setPointSize(7)
        self.label_page.setFont(font1)
        self.label_page.setStyleSheet(u"color: rgba(255, 255, 255, 155);")
        self.label_page.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.frame_title_bottom_layout.addWidget(self.label_page)


        self.frame_title_layout.addWidget(self.frame_title_bottom)


        self.top_bar_layout.addWidget(self.frame_title)


        self.central_layout.addWidget(self.top_bar)

        self.content = QFrame(self.centralwidget)
        self.content.setObjectName(u"content")
        self.content.setFrameShape(QFrame.NoFrame)
        self.content.setFrameShadow(QFrame.Raised)
        self.content_layout = QHBoxLayout(self.content)
        self.content_layout.setSpacing(0)
        self.content_layout.setObjectName(u"content_layout")
        self.content_layout.setContentsMargins(0, 0, 0, 0)
        self.frame_pages = QFrame(self.content)
        self.frame_pages.setObjectName(u"frame_pages")
        self.frame_pages.setFrameShape(QFrame.NoFrame)
        self.frame_pages.setFrameShadow(QFrame.Raised)
        self.frame_page_layout = QVBoxLayout(self.frame_pages)
        self.frame_page_layout.setSpacing(10)
        self.frame_page_layout.setObjectName(u"frame_page_layout")
        self.frame_page_layout.setContentsMargins(23, 9, 23, 9)
        self.daler_page = QFrame(self.frame_pages)
        self.daler_page.setObjectName(u"daler_page")
        self.daler_page.setStyleSheet(u"background-color: rgb(0, 170, 127);\n"
"border-radius:12px;\n"
"")
        self.daler_page.setFrameShape(QFrame.NoFrame)
        self.daler_page.setFrameShadow(QFrame.Raised)
        self.daler_page_layout = QHBoxLayout(self.daler_page)
        self.daler_page_layout.setObjectName(u"daler_page_layout")

        self.frame_page_layout.addWidget(self.daler_page)

        self.table_page = QFrame(self.frame_pages)
        self.table_page.setObjectName(u"table_page")
        self.table_page.setStyleSheet(u"background-color: rgb(0, 170, 127);border-radius:12px;\n"
"")
        self.table_page.setFrameShape(QFrame.NoFrame)
        self.table_page.setFrameShadow(QFrame.Raised)
        self.table_page_layout = QHBoxLayout(self.table_page)
        self.table_page_layout.setObjectName(u"table_page_layout")
        self.hit = QPushButton(self.table_page)
        self.hit.setObjectName(u"hit")
        self.hit.setMaximumSize(QSize(200, 300))
        self.hit.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(25, 25, 25);\n"
"color: rgb(255, 255, 255);\n"
"border:0px solid;\n"
"}\n"
"QPushButton:hover{background-color: rgb(200, 200, 200);}\n"
"QPushButton:pressed{	background-color: rgb(85, 170, 255);}")

        self.table_page_layout.addWidget(self.hit)

        self.stand = QPushButton(self.table_page)
        self.stand.setObjectName(u"stand")
        self.stand.setEnabled(True)
        self.stand.setMaximumSize(QSize(200, 300))
        self.stand.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(25, 25, 25);\n"
"color: rgb(255, 255, 255);\n"
"border:0px solid;\n"
"}\n"
"QPushButton:hover{background-color: rgb(200, 200, 200);}\n"
"QPushButton:pressed{	background-color: rgb(85, 170, 255);}")

        self.table_page_layout.addWidget(self.stand)

        self.simulate = QPushButton(self.table_page)
        self.simulate.setObjectName(u"simulate")
        self.simulate.setMaximumSize(QSize(200, 300))
        self.simulate.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(25, 25, 25);\n"
"color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton:hover{background-color: rgb(200, 200, 200);}\n"
"QPushButton:pressed{	background-color: rgb(85, 170, 255);}")

        self.table_page_layout.addWidget(self.simulate)


        self.frame_page_layout.addWidget(self.table_page)

        self.player_page = QFrame(self.frame_pages)
        self.player_page.setObjectName(u"player_page")
        self.player_page.setStyleSheet(u"background-color: rgb(0, 170, 127);border-radius:12px;\n"
"")
        self.player_page.setFrameShape(QFrame.NoFrame)
        self.player_page.setFrameShadow(QFrame.Raised)
        self.player_page_layout = QHBoxLayout(self.player_page)
        self.player_page_layout.setObjectName(u"player_page_layout")

        self.frame_page_layout.addWidget(self.player_page)


        self.content_layout.addWidget(self.frame_pages)


        self.central_layout.addWidget(self.content)

        self.bottom_bar = QFrame(self.centralwidget)
        self.bottom_bar.setObjectName(u"bottom_bar")
        self.bottom_bar.setMinimumSize(QSize(0, 20))
        self.bottom_bar.setMaximumSize(QSize(16777215, 20))
        self.bottom_bar.setStyleSheet(u"background-color: rgb(25, 25, 25);")
        self.bottom_bar.setFrameShape(QFrame.NoFrame)
        self.bottom_bar.setFrameShadow(QFrame.Raised)
        self.bottom_bar_layout = QHBoxLayout(self.bottom_bar)
        self.bottom_bar_layout.setSpacing(0)
        self.bottom_bar_layout.setObjectName(u"bottom_bar_layout")
        self.bottom_bar_layout.setContentsMargins(0, 0, 0, 0)

        self.central_layout.addWidget(self.bottom_bar)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.icon_title.setText("")
        self.label_title.setText(QCoreApplication.translate("MainWindow", u"BLACK-JACK", None))
        self.button_minimize.setText("")
        self.button_close.setText("")
        self.label_page.setText(QCoreApplication.translate("MainWindow", u"SINGLE-PLAYER", None))
        self.hit.setText(QCoreApplication.translate("MainWindow", u"HIT", None))
        self.stand.setText(QCoreApplication.translate("MainWindow", u"STAND", None))
        self.simulate.setText(QCoreApplication.translate("MainWindow", u"SIMULATE 100 MATCHS", None))
    # retranslateUi


# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_BBDialog(object):
    def __init__(self, BBDialog):
        if not BBDialog.objectName():
            BBDialog.setObjectName(u"BBDialog")
        BBDialog.resize(397, 232)
        self.verticalLayout = QVBoxLayout(BBDialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.createGroupBox = QGroupBox(BBDialog)
        self.createGroupBox.setObjectName(u"createGroupBox")
        self.createGroupBox.setEnabled(True)
        self.createGroupBox.setMinimumSize(QSize(0, 0))
        self.gridLayout = QGridLayout(self.createGroupBox)
        self.gridLayout.setObjectName(u"gridLayout")
        self.createButton = QPushButton(self.createGroupBox)
        self.createButton.setObjectName(u"createButton")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.createButton.sizePolicy().hasHeightForWidth())
        self.createButton.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.createButton, 0, 0, 1, 1)


        self.verticalLayout.addWidget(self.createGroupBox)

        self.visibilityGroupBox = QGroupBox(BBDialog)
        self.visibilityGroupBox.setObjectName(u"visibilityGroupBox")
        self.gridLayout_2 = QGridLayout(self.visibilityGroupBox)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.controllerAllOnButton = QPushButton(self.visibilityGroupBox)
        self.controllerAllOnButton.setObjectName(u"controllerAllOnButton")

        self.gridLayout_2.addWidget(self.controllerAllOnButton, 2, 3, 1, 1)

        self.ballVisibilityButton = QPushButton(self.visibilityGroupBox)
        self.ballVisibilityButton.setObjectName(u"ballVisibilityButton")

        self.gridLayout_2.addWidget(self.ballVisibilityButton, 0, 0, 1, 2)

        self.controllerAllOffButton = QPushButton(self.visibilityGroupBox)
        self.controllerAllOffButton.setObjectName(u"controllerAllOffButton")

        self.gridLayout_2.addWidget(self.controllerAllOffButton, 2, 4, 1, 1)

        self.controllerVisibilityButton = QPushButton(self.visibilityGroupBox)
        self.controllerVisibilityButton.setObjectName(u"controllerVisibilityButton")

        self.gridLayout_2.addWidget(self.controllerVisibilityButton, 0, 3, 1, 2)

        self.ballAllOnButton = QPushButton(self.visibilityGroupBox)
        self.ballAllOnButton.setObjectName(u"ballAllOnButton")

        self.gridLayout_2.addWidget(self.ballAllOnButton, 2, 0, 1, 1)

        self.ballAllOffButton = QPushButton(self.visibilityGroupBox)
        self.ballAllOffButton.setObjectName(u"ballAllOffButton")

        self.gridLayout_2.addWidget(self.ballAllOffButton, 2, 1, 1, 1)

        self.ButtonsHorizontalSpacer = QSpacerItem(35, 20, QSizePolicy.MinimumExpanding, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.ButtonsHorizontalSpacer, 2, 2, 1, 1)


        self.verticalLayout.addWidget(self.visibilityGroupBox)


        self.retranslateUi(BBDialog)

        QMetaObject.connectSlotsByName(BBDialog)
    # setupUi

    def retranslateUi(self, BBDialog):
        BBDialog.setWindowTitle(QCoreApplication.translate("BBDialog", u"Bouncing Ball Visualizer", None))
        self.createGroupBox.setTitle(QCoreApplication.translate("BBDialog", u"Create Bouncing ball", None))
        self.createButton.setText(QCoreApplication.translate("BBDialog", u"View as bouncing ball", None))
        self.visibilityGroupBox.setTitle(QCoreApplication.translate("BBDialog", u"Toggle Visibility", None))
        self.controllerAllOnButton.setText(QCoreApplication.translate("BBDialog", u"All on", None))
        self.ballVisibilityButton.setText(QCoreApplication.translate("BBDialog", u"Ball visibility", None))
        self.controllerAllOffButton.setText(QCoreApplication.translate("BBDialog", u"All off", None))
        self.controllerVisibilityButton.setText(QCoreApplication.translate("BBDialog", u"Controller visibility", None))
        self.ballAllOnButton.setText(QCoreApplication.translate("BBDialog", u"All on", None))
        self.ballAllOffButton.setText(QCoreApplication.translate("BBDialog", u"All off", None))
    # retranslateUi


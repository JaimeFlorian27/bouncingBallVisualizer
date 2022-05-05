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
        BBDialog.resize(357, 220)
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
        self.horizontalLayout = QHBoxLayout(self.visibilityGroupBox)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.ballVisibilityButton = QPushButton(self.visibilityGroupBox)
        self.ballVisibilityButton.setObjectName(u"ballVisibilityButton")

        self.horizontalLayout.addWidget(self.ballVisibilityButton)

        self.controllerVisibilityButton = QPushButton(self.visibilityGroupBox)
        self.controllerVisibilityButton.setObjectName(u"controllerVisibilityButton")

        self.horizontalLayout.addWidget(self.controllerVisibilityButton)


        self.verticalLayout.addWidget(self.visibilityGroupBox)


        self.retranslateUi(BBDialog)

        QMetaObject.connectSlotsByName(BBDialog)
    # setupUi

    def retranslateUi(self, BBDialog):
        BBDialog.setWindowTitle(QCoreApplication.translate("BBDialog", u"Dialog", None))
        self.createGroupBox.setTitle(QCoreApplication.translate("BBDialog", u"Create Bouncing ball", None))
        self.createButton.setText(QCoreApplication.translate("BBDialog", u"View as bouncing ball", None))
        self.visibilityGroupBox.setTitle(QCoreApplication.translate("BBDialog", u"Toggle Visibility", None))
        self.ballVisibilityButton.setText(QCoreApplication.translate("BBDialog", u"Ball visibility", None))
        self.controllerVisibilityButton.setText(QCoreApplication.translate("BBDialog", u"Controller visibility", None))
    # retranslateUi


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
        BBDialog.resize(403, 333)
        self.verticalLayout = QVBoxLayout(BBDialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.createGroupBox = QGroupBox(BBDialog)
        self.createGroupBox.setObjectName(u"createGroupBox")
        self.createGroupBox.setEnabled(True)
        self.createGroupBox.setMinimumSize(QSize(0, 0))
        self.gridLayout = QGridLayout(self.createGroupBox)
        self.gridLayout.setObjectName(u"gridLayout")
        self.radiusFrame = QFrame(self.createGroupBox)
        self.radiusFrame.setObjectName(u"radiusFrame")
        self.radiusFrame.setEnabled(True)
        self.radiusFrame.setHidden(True)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.radiusFrame.sizePolicy().hasHeightForWidth())
        self.radiusFrame.setSizePolicy(sizePolicy)
        self.radiusFrame.setFrameShape(QFrame.StyledPanel)
        self.radiusFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.radiusFrame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.labelRadius = QLabel(self.radiusFrame)
        self.labelRadius.setObjectName(u"labelRadius")

        self.horizontalLayout.addWidget(self.labelRadius)

        self.radiusSpinBox = QDoubleSpinBox(self.radiusFrame)
        self.radiusSpinBox.setObjectName(u"radiusSpinBox")
        self.radiusSpinBox.setMinimum(0.020000000000000)
        self.radiusSpinBox.setMaximum(98.989999999999995)
        self.radiusSpinBox.setSingleStep(0.100000000000000)
        self.radiusSpinBox.setValue(1.000000000000000)

        self.horizontalLayout.addWidget(self.radiusSpinBox)

        self.radiusSlider = QSlider(self.radiusFrame)
        self.radiusSlider.setObjectName(u"radiusSlider")
        self.radiusSlider.setMinimum(2)
        self.radiusSlider.setMaximum(10000)
        self.radiusSlider.setSingleStep(1)
        self.radiusSlider.setPageStep(1)
        self.radiusSlider.setValue(100)
        self.radiusSlider.setSliderPosition(100)
        self.radiusSlider.setTracking(True)
        self.radiusSlider.setOrientation(Qt.Horizontal)
        self.radiusSlider.setInvertedAppearance(False)
        self.radiusSlider.setInvertedControls(False)

        self.horizontalLayout.addWidget(self.radiusSlider)


        self.gridLayout.addWidget(self.radiusFrame, 1, 0, 1, 1)

        self.createButton = QPushButton(self.createGroupBox)
        self.createButton.setObjectName(u"createButton")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Maximum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.createButton.sizePolicy().hasHeightForWidth())
        self.createButton.setSizePolicy(sizePolicy1)
        self.createButton.setMinimumSize(QSize(0, 52))

        self.gridLayout.addWidget(self.createButton, 0, 0, 1, 1)


        self.verticalLayout.addWidget(self.createGroupBox)

        self.visibilityGroupBox = QGroupBox(BBDialog)
        self.visibilityGroupBox.setObjectName(u"visibilityGroupBox")
        self.gridLayout_2 = QGridLayout(self.visibilityGroupBox)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.ballAllOnButton = QPushButton(self.visibilityGroupBox)
        self.ballAllOnButton.setObjectName(u"ballAllOnButton")

        self.gridLayout_2.addWidget(self.ballAllOnButton, 2, 2, 1, 1)

        self.controllerAllOnButton = QPushButton(self.visibilityGroupBox)
        self.controllerAllOnButton.setObjectName(u"controllerAllOnButton")

        self.gridLayout_2.addWidget(self.controllerAllOnButton, 2, 5, 1, 1)

        self.controllerVisibilityButton = QPushButton(self.visibilityGroupBox)
        self.controllerVisibilityButton.setObjectName(u"controllerVisibilityButton")

        self.gridLayout_2.addWidget(self.controllerVisibilityButton, 0, 4, 1, 2)

        self.isolateViewButton = QPushButton(self.visibilityGroupBox)
        self.isolateViewButton.setObjectName(u"isolateViewButton")
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.isolateViewButton.sizePolicy().hasHeightForWidth())
        self.isolateViewButton.setSizePolicy(sizePolicy2)

        self.gridLayout_2.addWidget(self.isolateViewButton, 3, 0, 1, 6)

        self.controllerAllOffButton = QPushButton(self.visibilityGroupBox)
        self.controllerAllOffButton.setObjectName(u"controllerAllOffButton")

        self.gridLayout_2.addWidget(self.controllerAllOffButton, 2, 4, 1, 1)

        self.ButtonsHorizontalSpacer = QSpacerItem(35, 20, QSizePolicy.MinimumExpanding, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.ButtonsHorizontalSpacer, 2, 3, 1, 1)

        self.ballAllOffButton = QPushButton(self.visibilityGroupBox)
        self.ballAllOffButton.setObjectName(u"ballAllOffButton")

        self.gridLayout_2.addWidget(self.ballAllOffButton, 2, 0, 1, 1)

        self.ballVisibilityButton = QPushButton(self.visibilityGroupBox)
        self.ballVisibilityButton.setObjectName(u"ballVisibilityButton")

        self.gridLayout_2.addWidget(self.ballVisibilityButton, 0, 0, 1, 3)


        self.verticalLayout.addWidget(self.visibilityGroupBox)

        self.deleteGroupBox = QGroupBox(BBDialog)
        self.deleteGroupBox.setObjectName(u"deleteGroupBox")
        self.horizontalLayout_2 = QHBoxLayout(self.deleteGroupBox)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.deleteSelectedButton = QPushButton(self.deleteGroupBox)
        self.deleteSelectedButton.setObjectName(u"deleteSelectedButton")

        self.horizontalLayout_2.addWidget(self.deleteSelectedButton)

        self.deleteAllButton = QPushButton(self.deleteGroupBox)
        self.deleteAllButton.setObjectName(u"deleteAllButton")

        self.horizontalLayout_2.addWidget(self.deleteAllButton)


        self.verticalLayout.addWidget(self.deleteGroupBox)

        QWidget.setTabOrder(self.createButton, self.radiusSlider)
        QWidget.setTabOrder(self.radiusSlider, self.controllerVisibilityButton)
        QWidget.setTabOrder(self.controllerVisibilityButton, self.isolateViewButton)
        QWidget.setTabOrder(self.isolateViewButton, self.deleteSelectedButton)
        QWidget.setTabOrder(self.deleteSelectedButton, self.deleteAllButton)

        self.retranslateUi(BBDialog)

        QMetaObject.connectSlotsByName(BBDialog)
    # setupUi

    def retranslateUi(self, BBDialog):
        BBDialog.setWindowTitle(QCoreApplication.translate("BBDialog", u"Bouncing Ball Visualizer", None))
        self.createGroupBox.setTitle(QCoreApplication.translate("BBDialog", u"Create Bouncing ball", None))
        self.labelRadius.setText(QCoreApplication.translate("BBDialog", u"Radius", None))
        self.createButton.setText(QCoreApplication.translate("BBDialog", u"View as bouncing ball", None))
        self.visibilityGroupBox.setTitle(QCoreApplication.translate("BBDialog", u"Toggle Visibility", None))
        self.ballAllOnButton.setText(QCoreApplication.translate("BBDialog", u"All on", None))
        self.controllerAllOnButton.setText(QCoreApplication.translate("BBDialog", u"All on", None))
        self.controllerVisibilityButton.setText(QCoreApplication.translate("BBDialog", u"nurbsCurve visibility", None))
        self.isolateViewButton.setText(QCoreApplication.translate("BBDialog", u"Isolate view on Controllers", None))
        self.controllerAllOffButton.setText(QCoreApplication.translate("BBDialog", u"All off", None))
        self.ballAllOffButton.setText(QCoreApplication.translate("BBDialog", u"All off", None))
        self.ballVisibilityButton.setText(QCoreApplication.translate("BBDialog", u"Ball visibility", None))
        self.deleteGroupBox.setTitle(QCoreApplication.translate("BBDialog", u"Delete Bouncing ball", None))
        self.deleteSelectedButton.setText(QCoreApplication.translate("BBDialog", u"Delete from selected", None))
        self.deleteAllButton.setText(QCoreApplication.translate("BBDialog", u"Delete all", None))
    # retranslateUi

if __name__ == "__main__":
    pass
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'shoreline_extractor_dialog_base.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_AutomaticShorelineExtractionDialogBase(object):
    def setupUi(self, AutomaticShorelineExtractionDialogBase):
        AutomaticShorelineExtractionDialogBase.setObjectName("AutomaticShorelineExtractionDialogBase")
        AutomaticShorelineExtractionDialogBase.resize(646, 473)
        self.button_box = QtWidgets.QDialogButtonBox(AutomaticShorelineExtractionDialogBase)
        self.button_box.setGeometry(QtCore.QRect(470, 430, 171, 32))
        self.button_box.setOrientation(QtCore.Qt.Horizontal)
        self.button_box.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.button_box.setCenterButtons(False)
        self.button_box.setObjectName("button_box")
        self.shorelineExtractionWidget = QtWidgets.QTabWidget(AutomaticShorelineExtractionDialogBase)
        self.shorelineExtractionWidget.setGeometry(QtCore.QRect(10, 10, 631, 361))
        self.shorelineExtractionWidget.setObjectName("shorelineExtractionWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.shorelineExtractionWidget.addTab(self.tab, "")
        self.ExtractShorelineTab = QtWidgets.QWidget()
        self.ExtractShorelineTab.setObjectName("ExtractShorelineTab")
        self.shorlineChangTabWidget = QtWidgets.QTabWidget(self.ExtractShorelineTab)
        self.shorlineChangTabWidget.setGeometry(QtCore.QRect(0, 0, 631, 331))
        self.shorlineChangTabWidget.setObjectName("shorlineChangTabWidget")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.horizontalLayoutWidget_3 = QtWidgets.QWidget(self.tab_3)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(10, 50, 611, 41))
        self.horizontalLayoutWidget_3.setObjectName("horizontalLayoutWidget_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_2 = QtWidgets.QLabel(self.horizontalLayoutWidget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_3.addWidget(self.label_2)
        spacerItem = QtWidgets.QSpacerItem(62, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.inputRasterASECombobox = QtWidgets.QComboBox(self.horizontalLayoutWidget_3)
        self.inputRasterASECombobox.setObjectName("inputRasterASECombobox")
        self.horizontalLayout_3.addWidget(self.inputRasterASECombobox)
        self.horizontalLayoutWidget_4 = QtWidgets.QWidget(self.tab_3)
        self.horizontalLayoutWidget_4.setGeometry(QtCore.QRect(10, 140, 611, 41))
        self.horizontalLayoutWidget_4.setObjectName("horizontalLayoutWidget_4")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_4)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_3 = QtWidgets.QLabel(self.horizontalLayoutWidget_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_4.addWidget(self.label_3)
        spacerItem1 = QtWidgets.QSpacerItem(30, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem1)
        self.rasterBandASEComboBox = QgsRasterBandComboBox(self.horizontalLayoutWidget_4)
        self.rasterBandASEComboBox.setObjectName("rasterBandASEComboBox")
        self.horizontalLayout_4.addWidget(self.rasterBandASEComboBox)
        self.horizontalLayoutWidget_7 = QtWidgets.QWidget(self.tab_3)
        self.horizontalLayoutWidget_7.setGeometry(QtCore.QRect(10, 230, 571, 41))
        self.horizontalLayoutWidget_7.setObjectName("horizontalLayoutWidget_7")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_7)
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_6 = QtWidgets.QLabel(self.horizontalLayoutWidget_7)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_7.addWidget(self.label_6)
        spacerItem2 = QtWidgets.QSpacerItem(69, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem2)
        self.outputASElineEdit = QtWidgets.QLineEdit(self.horizontalLayoutWidget_7)
        self.outputASElineEdit.setObjectName("outputASElineEdit")
        self.horizontalLayout_7.addWidget(self.outputASElineEdit)
        self.gridLayoutWidget = QtWidgets.QWidget(self.tab_3)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(590, 230, 31, 41))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.openFolder = QtWidgets.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.openFolder.sizePolicy().hasHeightForWidth())
        self.openFolder.setSizePolicy(sizePolicy)
        self.openFolder.setObjectName("openFolder")
        self.gridLayout.addWidget(self.openFolder, 0, 0, 1, 1)
        self.shorlineChangTabWidget.addTab(self.tab_3, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.tab_2)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(10, 170, 611, 41))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        spacerItem3 = QtWidgets.QSpacerItem(28, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem3)
        self.comboBox = QtWidgets.QComboBox(self.horizontalLayoutWidget_2)
        self.comboBox.setObjectName("comboBox")
        self.horizontalLayout_2.addWidget(self.comboBox)
        self.horizontalLayoutWidget_5 = QtWidgets.QWidget(self.tab_2)
        self.horizontalLayoutWidget_5.setGeometry(QtCore.QRect(10, 30, 611, 41))
        self.horizontalLayoutWidget_5.setObjectName("horizontalLayoutWidget_5")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_5)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_4 = QtWidgets.QLabel(self.horizontalLayoutWidget_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_5.addWidget(self.label_4)
        spacerItem4 = QtWidgets.QSpacerItem(57, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem4)
        self.baselineSCRasterCombobox = QtWidgets.QComboBox(self.horizontalLayoutWidget_5)
        self.baselineSCRasterCombobox.setObjectName("baselineSCRasterCombobox")
        self.horizontalLayout_5.addWidget(self.baselineSCRasterCombobox)
        self.horizontalLayoutWidget_6 = QtWidgets.QWidget(self.tab_2)
        self.horizontalLayoutWidget_6.setGeometry(QtCore.QRect(10, 100, 611, 41))
        self.horizontalLayoutWidget_6.setObjectName("horizontalLayoutWidget_6")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_6)
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_5 = QtWidgets.QLabel(self.horizontalLayoutWidget_6)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_6.addWidget(self.label_5)
        spacerItem5 = QtWidgets.QSpacerItem(45, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem5)
        self.inputSCrasterBandComboBox = QgsRasterBandComboBox(self.horizontalLayoutWidget_6)
        self.inputSCrasterBandComboBox.setObjectName("inputSCrasterBandComboBox")
        self.horizontalLayout_6.addWidget(self.inputSCrasterBandComboBox)
        self.horizontalLayoutWidget_8 = QtWidgets.QWidget(self.tab_2)
        self.horizontalLayoutWidget_8.setGeometry(QtCore.QRect(10, 240, 571, 41))
        self.horizontalLayoutWidget_8.setObjectName("horizontalLayoutWidget_8")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_8)
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_7 = QtWidgets.QLabel(self.horizontalLayoutWidget_8)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_8.addWidget(self.label_7)
        spacerItem6 = QtWidgets.QSpacerItem(84, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem6)
        self.outputSClineEdit = QtWidgets.QLineEdit(self.horizontalLayoutWidget_8)
        self.outputSClineEdit.setObjectName("outputSClineEdit")
        self.horizontalLayout_8.addWidget(self.outputSClineEdit)
        self.gridLayoutWidget_2 = QtWidgets.QWidget(self.tab_2)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(590, 240, 31, 41))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.openFolder_2 = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.openFolder_2.sizePolicy().hasHeightForWidth())
        self.openFolder_2.setSizePolicy(sizePolicy)
        self.openFolder_2.setObjectName("openFolder_2")
        self.gridLayout_2.addWidget(self.openFolder_2, 0, 0, 1, 1)
        self.shorlineChangTabWidget.addTab(self.tab_2, "")
        self.shorelineExtractionWidget.addTab(self.ExtractShorelineTab, "")
        self.aboutTab = QtWidgets.QWidget()
        self.aboutTab.setObjectName("aboutTab")
        self.shorelineExtractionWidget.addTab(self.aboutTab, "")
        self.horizontalLayoutWidget = QtWidgets.QWidget(AutomaticShorelineExtractionDialogBase)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 380, 631, 41))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.progressBar = QtWidgets.QProgressBar(self.horizontalLayoutWidget)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.horizontalLayout.addWidget(self.progressBar)
        self.cancelprogress = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.cancelprogress.setObjectName("cancelprogress")
        self.horizontalLayout.addWidget(self.cancelprogress)

        self.retranslateUi(AutomaticShorelineExtractionDialogBase)
        self.shorelineExtractionWidget.setCurrentIndex(1)
        self.shorlineChangTabWidget.setCurrentIndex(0)
        self.button_box.accepted.connect(AutomaticShorelineExtractionDialogBase.accept)
        self.button_box.rejected.connect(AutomaticShorelineExtractionDialogBase.reject)
        QtCore.QMetaObject.connectSlotsByName(AutomaticShorelineExtractionDialogBase)

    def retranslateUi(self, AutomaticShorelineExtractionDialogBase):
        _translate = QtCore.QCoreApplication.translate
        AutomaticShorelineExtractionDialogBase.setWindowTitle(_translate("AutomaticShorelineExtractionDialogBase", "CoGEOS "))
        self.shorelineExtractionWidget.setTabText(self.shorelineExtractionWidget.indexOf(self.tab), _translate("AutomaticShorelineExtractionDialogBase", "Image Downloader"))
        self.label_2.setText(_translate("AutomaticShorelineExtractionDialogBase", "Input Raster"))
        self.label_3.setText(_translate("AutomaticShorelineExtractionDialogBase", "Select Band \'NIR\'"))
        self.label_6.setText(_translate("AutomaticShorelineExtractionDialogBase", "Output File"))
        self.openFolder.setText(_translate("AutomaticShorelineExtractionDialogBase", "..."))
        self.shorlineChangTabWidget.setTabText(self.shorlineChangTabWidget.indexOf(self.tab_3), _translate("AutomaticShorelineExtractionDialogBase", "Automatic Shoreline Extraction"))
        self.label.setText(_translate("AutomaticShorelineExtractionDialogBase", " Comparison Raster"))
        self.label_4.setText(_translate("AutomaticShorelineExtractionDialogBase", "Baseline Raster"))
        self.label_5.setText(_translate("AutomaticShorelineExtractionDialogBase", "Select Band \'NIR\'"))
        self.label_7.setText(_translate("AutomaticShorelineExtractionDialogBase", "Output File"))
        self.openFolder_2.setText(_translate("AutomaticShorelineExtractionDialogBase", "..."))
        self.shorlineChangTabWidget.setTabText(self.shorlineChangTabWidget.indexOf(self.tab_2), _translate("AutomaticShorelineExtractionDialogBase", "Shoreline Change"))
        self.shorelineExtractionWidget.setTabText(self.shorelineExtractionWidget.indexOf(self.ExtractShorelineTab), _translate("AutomaticShorelineExtractionDialogBase", "Extract Shoreline"))
        self.shorelineExtractionWidget.setTabText(self.shorelineExtractionWidget.indexOf(self.aboutTab), _translate("AutomaticShorelineExtractionDialogBase", "About"))
        self.cancelprogress.setText(_translate("AutomaticShorelineExtractionDialogBase", "Cancel"))

from qgsrasterbandcombobox import QgsRasterBandComboBox

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    AutomaticShorelineExtractionDialogBase = QtWidgets.QDialog()
    ui = Ui_AutomaticShorelineExtractionDialogBase()
    ui.setupUi(AutomaticShorelineExtractionDialogBase)
    AutomaticShorelineExtractionDialogBase.show()
    sys.exit(app.exec_())

# -*- coding: utf-8 -*-


# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!
#importer des bibliothèques python
import csv

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon
import sys
import warnings
import os.path

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split , cross_val_score, validation_curve,learning_curve
from sklearn.compose import ColumnTransformer
from sklearn.ensemble import RandomForestClassifier
warnings.filterwarnings("ignore")

class Ui_cancer(object):
    def setupUi(self, cancer):
        cancer.setObjectName("cancer")
        cancer.resize(1368, 768)
        icon = QtGui.QIcon("icon.ico")
        icon.addPixmap(QtGui.QPixmap("icon.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        cancer.setWindowIcon(icon)
        cancer.setStyleSheet("background-color: rgb(255,192,203);")
        cancer.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        cancer.setDocumentMode(False)
        cancer.setDockNestingEnabled(False)
        cancer.setUnifiedTitleAndToolBarOnMac(False)
        self.centralwidget = QtWidgets.QWidget(cancer)
        self.centralwidget.setObjectName("centralwidget")
        self.titre = QtWidgets.QWidget(self.centralwidget)
        self.titre.setGeometry(QtCore.QRect(50, 10, 1268, 80))
        self.titre.setStyleSheet("background-image: url(er.png);\n"
"border-radius: 15px;")
        self.titre.setObjectName("titre")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(970, 120, 361, 571))
        self.widget.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"\n"
"border-radius: 15px;")
        self.widget.setObjectName("widget")
        self.pushButton = QtWidgets.QPushButton(self.widget)
        self.pushButton.setGeometry(QtCore.QRect(130, 470, 91, 31))
        self.pushButton.setStyleSheet("QPushButton{\n"
"    background: #FFFFFF;\n"
"    background-color: rgb(255,192,203);\n"
"    border: 2px solid #FFFFFF; \n"
"    border-radius: 10px; \n"
"    font-family: Arial;\n"
"    font-size:15px;\n"
"    color: #19060f;\n"
"\n"
"}\n"
"QPushButton:hover{\n"
"     border: 2px solid #000000; \n"
"     background: #FFFFFF;\n"
"}\n"
"")
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setIcon(QIcon('test.png'))
        self.textBrowser = QtWidgets.QTextBrowser(self.widget)
        self.textBrowser.setGeometry(QtCore.QRect(10, 510, 341, 61))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.textBrowser.setFont(font)
        self.textBrowser.setObjectName("textBrowser")
        self.result = QtWidgets.QWidget(self.widget)
        self.result.setGeometry(QtCore.QRect(0, 0, 371, 81))
        self.result.setStyleSheet("background-image: url(result.png);")
        self.result.setObjectName("result")
        self.label_7 = QtWidgets.QLabel(self.result)
        self.label_7.setGeometry(QtCore.QRect(120, 20, 131, 31))
        self.label_7.setStyleSheet("\n"
"font: 75 25pt \"Liberation Serif\";\n"
"\n"
"background-color: rgba(191, 64, 64, 0);\n"
"color: rgb(255, 255, 255);")
        self.label_7.setObjectName("label_7")
        self.score = QtWidgets.QTextEdit(self.widget)
        self.score.setGeometry(QtCore.QRect(100, 200, 160, 130))
        self.score.setStyleSheet("background-image: url(res.png);")
        self.score.setObjectName("score")
        self.lineEdit_19 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_19.setGeometry(QtCore.QRect(120, 390, 181, 25))
        self.lineEdit_19.setStyleSheet("font-family:URW Bookman;margin:center; font-size:18px; color: rgb(0, 0, 0);")
        self.lineEdit_19.setObjectName("lineEdit_19")
        self.widget_4 = QtWidgets.QWidget(self.widget)
        self.widget_4.setGeometry(QtCore.QRect(100, 130, 160, 61))
        self.widget_4.setStyleSheet("background-image: url(scor.png);")
        self.widget_4.setObjectName("widget_4")
        self.lineEdit_20 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_20.setGeometry(QtCore.QRect(120, 250, 130, 31))
        self.lineEdit_20.setStyleSheet("font-family:URW Bookman;margin:center; font-size:18px; color: rgb(0, 0, 0);")
        self.lineEdit_20.setObjectName("lineEdit_20")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(459, 391, 236, 331))
        font = QtGui.QFont()
        font.setFamily("Fira Code")
        font.setPointSize(13)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.layoutWidget.setFont(font)
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.fractal_dimension_mean = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Fira Code")
        font.setPointSize(13)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.fractal_dimension_mean.setFont(font)
        self.fractal_dimension_mean.setStyleSheet("color: rgb(255, 255, 255);")
        self.fractal_dimension_mean.setObjectName("fractal_dimension_mean")
        self.verticalLayout_2.addWidget(self.fractal_dimension_mean)
        self.radius_se = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Fira Code")
        font.setPointSize(13)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.radius_se.setFont(font)
        self.radius_se.setStyleSheet("color: rgb(255, 255, 255);")
        self.radius_se.setObjectName("radius_se")
        self.verticalLayout_2.addWidget(self.radius_se)
        self.texture_se = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Fira Code")
        font.setPointSize(13)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.texture_se.setFont(font)
        self.texture_se.setStyleSheet("color: rgb(255, 255, 255);")
        self.texture_se.setObjectName("texture_se")
        self.verticalLayout_2.addWidget(self.texture_se)
        self.perimeter_se = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Fira Code")
        font.setPointSize(13)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.perimeter_se.setFont(font)
        self.perimeter_se.setStyleSheet("color: rgb(255, 255, 255);")
        self.perimeter_se.setObjectName("perimeter_se")
        self.verticalLayout_2.addWidget(self.perimeter_se)
        self.area_se = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Fira Code")
        font.setPointSize(13)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.area_se.setFont(font)
        self.area_se.setStyleSheet("color: rgb(255, 255, 255);")
        self.area_se.setObjectName("area_se")
        self.verticalLayout_2.addWidget(self.area_se)
        self.smoothness_se = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Fira Code")
        font.setPointSize(13)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.smoothness_se.setFont(font)
        self.smoothness_se.setStyleSheet("color: rgb(255, 255, 255);")
        self.smoothness_se.setObjectName("smoothness_se")
        self.verticalLayout_2.addWidget(self.smoothness_se)
        self.compactness_se = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Fira Code")
        font.setPointSize(13)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.compactness_se.setFont(font)
        self.compactness_se.setStyleSheet("color: rgb(255, 255, 255);")
        self.compactness_se.setObjectName("compactness_se")
        self.verticalLayout_2.addWidget(self.compactness_se)
        self.concavity_se = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Fira Code")
        font.setPointSize(13)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.concavity_se.setFont(font)
        self.concavity_se.setStyleSheet("color: rgb(255, 255, 255);")
        self.concavity_se.setObjectName("concavity_se")
        self.verticalLayout_2.addWidget(self.concavity_se)
        self.concave_points_se = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Fira Code")
        font.setPointSize(13)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.concave_points_se.setFont(font)
        self.concave_points_se.setStyleSheet("color: rgb(255, 255, 255);")
        self.concave_points_se.setObjectName("concave_points_se")
        self.verticalLayout_2.addWidget(self.concave_points_se)
        self.layoutWidget1 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget1.setGeometry(QtCore.QRect(49, 391, 205, 341))
        font = QtGui.QFont()
        font.setFamily("Fira Code")
        font.setPointSize(13)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.layoutWidget1.setFont(font)
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget1)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setFamily("Fira Code")
        font.setPointSize(13)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(255, 255, 255);")
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setFamily("Fira Code")
        font.setPointSize(13)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.label_3 = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setFamily("Fira Code")
        font.setPointSize(13)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.label_4 = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setFamily("Fira Code")
        font.setPointSize(13)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)
        self.smoothness_mean = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setFamily("Fira Code")
        font.setPointSize(13)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.smoothness_mean.setFont(font)
        self.smoothness_mean.setStyleSheet("color: rgb(255, 255, 255);")
        self.smoothness_mean.setObjectName("smoothness_mean")
        self.verticalLayout.addWidget(self.smoothness_mean)
        self.compactness_mean = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setFamily("Fira Code")
        font.setPointSize(13)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.compactness_mean.setFont(font)
        self.compactness_mean.setStyleSheet("color: rgb(255, 255, 255);")
        self.compactness_mean.setObjectName("compactness_mean")
        self.verticalLayout.addWidget(self.compactness_mean)
        self.concavity_mean = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setFamily("Fira Code")
        font.setPointSize(13)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.concavity_mean.setFont(font)
        self.concavity_mean.setStyleSheet("color: rgb(255, 255, 255);")
        self.concavity_mean.setObjectName("concavity_mean")
        self.verticalLayout.addWidget(self.concavity_mean)
        self.concave_points_mean = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setFamily("Fira Code")
        font.setPointSize(13)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.concave_points_mean.setFont(font)
        self.concave_points_mean.setStyleSheet("color: rgb(255, 255, 255);")
        self.concave_points_mean.setObjectName("concave_points_mean")
        self.verticalLayout.addWidget(self.concave_points_mean)
        self.symmetry_mean = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setFamily("Fira Code")
        font.setPointSize(13)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.symmetry_mean.setFont(font)
        self.symmetry_mean.setStyleSheet("color: rgb(255, 255, 255);")
        self.symmetry_mean.setObjectName("symmetry_mean")
        self.verticalLayout.addWidget(self.symmetry_mean)
        self.layoutWidget2 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget2.setGeometry(QtCore.QRect(185, 190, 101, 101))
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.layoutWidget2)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.Nom = QtWidgets.QLabel(self.layoutWidget2)
        self.Nom.setStyleSheet("font: 75 13pt \"C059\";\n"
"color: rgb(255, 255, 255);")
        self.Nom.setObjectName("Nom")
        self.verticalLayout_5.addWidget(self.Nom)
        self.Prnom = QtWidgets.QLabel(self.layoutWidget2)
        self.Prnom.setStyleSheet("font: 75 13pt \"C059\";\n"
"color: rgb(255, 255, 255);")
        self.Prnom.setObjectName("Prnom")
        self.verticalLayout_5.addWidget(self.Prnom)
        self.layoutWidget3 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget3.setGeometry(QtCore.QRect(270, 390, 146, 351))
        self.layoutWidget3.setObjectName("layoutWidget3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.layoutWidget3)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.lineEdit = QtWidgets.QLineEdit(self.layoutWidget3)
        self.lineEdit.setStyleSheet("QLineEdit{\n"
"    background: rgb(255,192,203);\n"
"    border: 2px solid #666666; \n"
"    border-radius: 10px;  \n"
"    font-family: Arial;\n"
"    font-size:15px;\n"
"   color: #19060f;\n"
"\n"
"}\n"
"QLineEdit:focus{\n"
"     border: 2px solid #FF439F; \n"
"    background: #FFFFFF;\n"
"    \n"
"}\n"
"QLineEdit:hover{\n"
"     border: 2px solid #000000; \n"
"     background: #FFFFFF;\n"
"    \n"
"}")
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout_3.addWidget(self.lineEdit)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.layoutWidget3)
        self.lineEdit_2.setStyleSheet("QLineEdit{\n"
"    background: rgb(255,192,203);\n"
"    border: 2px solid #666666; \n"
"    border-radius: 10px;  \n"
"    font-family: Arial;\n"
"    font-size:15px;\n"
"   color: #19060f;\n"
"\n"
"}\n"
"QLineEdit:focus{\n"
"     border: 2px solid #FF439F; \n"
"    background: #FFFFFF;\n"
"    \n"
"}\n"
"QLineEdit:hover{\n"
"     border: 2px solid #000000; \n"
"     background: #FFFFFF;\n"
"    \n"
"}")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.verticalLayout_3.addWidget(self.lineEdit_2)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.layoutWidget3)
        self.lineEdit_3.setStyleSheet("QLineEdit{\n"
"    background: rgb(255,192,203);\n"
"    border: 2px solid #666666; \n"
"    border-radius: 10px;  \n"
"    font-family: Arial;\n"
"    font-size:15px;\n"
"   color: #19060f;\n"
"\n"
"}\n"
"QLineEdit:focus{\n"
"     border: 2px solid #FF439F; \n"
"    background: #FFFFFF;\n"
"    \n"
"}\n"
"QLineEdit:hover{\n"
"     border: 2px solid #000000; \n"
"     background: #FFFFFF;\n"
"    \n"
"}")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.verticalLayout_3.addWidget(self.lineEdit_3)
        self.lineEdit_4 = QtWidgets.QLineEdit(self.layoutWidget3)
        self.lineEdit_4.setStyleSheet("QLineEdit{\n"
"    background: rgb(255,192,203);\n"
"    border: 2px solid #666666; \n"
"    border-radius: 10px;  \n"
"    font-family: Arial;\n"
"    font-size:15px;\n"
"   color: #19060f;\n"
"\n"
"}\n"
"QLineEdit:focus{\n"
"     border: 2px solid #FF439F; \n"
"    background: #FFFFFF;\n"
"    \n"
"}\n"
"QLineEdit:hover{\n"
"     border: 2px solid #000000; \n"
"     background: #FFFFFF;\n"
"    \n"
"}")
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.verticalLayout_3.addWidget(self.lineEdit_4)
        self.lineEdit_5 = QtWidgets.QLineEdit(self.layoutWidget3)
        self.lineEdit_5.setStyleSheet("QLineEdit{\n"
"    background: rgb(255,192,203);\n"
"    border: 2px solid #666666; \n"
"    border-radius: 10px;  \n"
"    font-family: Arial;\n"
"    font-size:15px;\n"
"   color: #19060f;\n"
"\n"
"}\n"
"QLineEdit:focus{\n"
"     border: 2px solid #FF439F; \n"
"    background: #FFFFFF;\n"
"    \n"
"}\n"
"QLineEdit:hover{\n"
"     border: 2px solid #000000; \n"
"     background: #FFFFFF;\n"
"    \n"
"}")
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.verticalLayout_3.addWidget(self.lineEdit_5)
        self.lineEdit_6 = QtWidgets.QLineEdit(self.layoutWidget3)
        self.lineEdit_6.setStyleSheet("QLineEdit{\n"
"    background: rgb(255,192,203);\n"
"    border: 2px solid #666666; \n"
"    border-radius: 10px;  \n"
"    font-family: Arial;\n"
"    font-size:15px;\n"
"   color: #19060f;\n"
"\n"
"}\n"
"QLineEdit:focus{\n"
"     border: 2px solid #FF439F; \n"
"    background: #FFFFFF;\n"
"    \n"
"}\n"
"QLineEdit:hover{\n"
"     border: 2px solid #000000; \n"
"     background: #FFFFFF;\n"
"    \n"
"}")
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.verticalLayout_3.addWidget(self.lineEdit_6)
        self.lineEdit_7 = QtWidgets.QLineEdit(self.layoutWidget3)
        self.lineEdit_7.setStyleSheet("QLineEdit{\n"
"    background: rgb(255,192,203);\n"
"    border: 2px solid #666666; \n"
"    border-radius: 10px;  \n"
"    font-family: Arial;\n"
"    font-size:15px;\n"
"   color: #19060f;\n"
"\n"
"}\n"
"QLineEdit:focus{\n"
"     border: 2px solid #FF439F; \n"
"    background: #FFFFFF;\n"
"    \n"
"}\n"
"QLineEdit:hover{\n"
"     border: 2px solid #000000; \n"
"     background: #FFFFFF;\n"
"    \n"
"}")
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.verticalLayout_3.addWidget(self.lineEdit_7)
        self.lineEdit_8 = QtWidgets.QLineEdit(self.layoutWidget3)
        self.lineEdit_8.setStyleSheet("QLineEdit{\n"
"    background: rgb(255,192,203);\n"
"    border: 2px solid #666666; \n"
"    border-radius: 10px;  \n"
"    font-family: Arial;\n"
"    font-size:15px;\n"
"   color: #19060f;\n"
"\n"
"}\n"
"QLineEdit:focus{\n"
"     border: 2px solid #FF439F; \n"
"    background: #FFFFFF;\n"
"    \n"
"}\n"
"QLineEdit:hover{\n"
"     border: 2px solid #000000; \n"
"     background: #FFFFFF;\n"
"    \n"
"}")
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.verticalLayout_3.addWidget(self.lineEdit_8)
        self.lineEdit_9 = QtWidgets.QLineEdit(self.layoutWidget3)
        self.lineEdit_9.setStyleSheet("QLineEdit{\n"
"    background: rgb(255,192,203);\n"
"    border: 2px solid #666666; \n"
"    border-radius: 10px;  \n"
"    font-family: Arial;\n"
"    font-size:15px;\n"
"   color: #19060f;\n"
"\n"
"}\n"
"QLineEdit:focus{\n"
"     border: 2px solid #FF439F; \n"
"    background: #FFFFFF;\n"
"    \n"
"}\n"
"QLineEdit:hover{\n"
"     border: 2px solid #000000; \n"
"     background: #FFFFFF;\n"
"    \n"
"}")
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.verticalLayout_3.addWidget(self.lineEdit_9)
        self.layoutWidget4 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget4.setGeometry(QtCore.QRect(720, 390, 146, 341))
        self.layoutWidget4.setObjectName("layoutWidget4")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.layoutWidget4)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.lineEdit_10 = QtWidgets.QLineEdit(self.layoutWidget4)
        self.lineEdit_10.setStyleSheet("QLineEdit{\n"
"    background: rgb(255,192,203);\n"
"    border: 2px solid #666666; \n"
"    border-radius: 10px;  \n"
"    font-family: Arial;\n"
"    font-size:15px;\n"
"   color: #19060f;\n"
"\n"
"}\n"
"QLineEdit:focus{\n"
"     border: 2px solid #FF439F; \n"
"    background: #FFFFFF;\n"
"    \n"
"}\n"
"QLineEdit:hover{\n"
"     border: 2px solid #000000; \n"
"     background: #FFFFFF;\n"
"    \n"
"}")
        self.lineEdit_10.setObjectName("lineEdit_10")
        self.verticalLayout_4.addWidget(self.lineEdit_10)
        self.lineEdit_11 = QtWidgets.QLineEdit(self.layoutWidget4)
        self.lineEdit_11.setStyleSheet("QLineEdit{\n"
"    background: rgb(255,192,203);\n"
"    border: 2px solid #666666; \n"
"    border-radius: 10px;  \n"
"    font-family: Arial;\n"
"    font-size:15px;\n"
"   color: #19060f;\n"
"\n"
"}\n"
"QLineEdit:focus{\n"
"     border: 2px solid #FF439F; \n"
"    background: #FFFFFF;\n"
"    \n"
"}\n"
"QLineEdit:hover{\n"
"     border: 2px solid #000000; \n"
"     background: #FFFFFF;\n"
"    \n"
"}")
        self.lineEdit_11.setObjectName("lineEdit_11")
        self.verticalLayout_4.addWidget(self.lineEdit_11)
        self.lineEdit_12 = QtWidgets.QLineEdit(self.layoutWidget4)
        self.lineEdit_12.setStyleSheet("QLineEdit{\n"
"    background: rgb(255,192,203);\n"
"    border: 2px solid #666666; \n"
"    border-radius: 10px;  \n"
"    font-family: Arial;\n"
"    font-size:15px;\n"
"   color: #19060f;\n"
"\n"
"}\n"
"QLineEdit:focus{\n"
"     border: 2px solid #FF439F; \n"
"    background: #FFFFFF;\n"
"    \n"
"}\n"
"QLineEdit:hover{\n"
"     border: 2px solid #000000; \n"
"     background: #FFFFFF;\n"
"    \n"
"}")
        self.lineEdit_12.setObjectName("lineEdit_12")
        self.verticalLayout_4.addWidget(self.lineEdit_12)
        self.lineEdit_13 = QtWidgets.QLineEdit(self.layoutWidget4)
        self.lineEdit_13.setStyleSheet("QLineEdit{\n"
"    background: rgb(255,192,203);\n"
"    border: 2px solid #666666; \n"
"    border-radius: 10px;  \n"
"    font-family: Arial;\n"
"    font-size:15px;\n"
"   color: #19060f;\n"
"\n"
"}\n"
"QLineEdit:focus{\n"
"     border: 2px solid #FF439F; \n"
"    background: #FFFFFF;\n"
"    \n"
"}\n"
"QLineEdit:hover{\n"
"     border: 2px solid #000000; \n"
"     background: #FFFFFF;\n"
"    \n"
"}")
        self.lineEdit_13.setObjectName("lineEdit_13")
        self.verticalLayout_4.addWidget(self.lineEdit_13)
        self.lineEdit_14 = QtWidgets.QLineEdit(self.layoutWidget4)
        self.lineEdit_14.setStyleSheet("QLineEdit{\n"
"    background: rgb(255,192,203);\n"
"    border: 2px solid #666666; \n"
"    border-radius: 10px;  \n"
"    font-family: Arial;\n"
"    font-size:15px;\n"
"   color: #19060f;\n"
"\n"
"}\n"
"QLineEdit:focus{\n"
"     border: 2px solid #FF439F; \n"
"    background: #FFFFFF;\n"
"    \n"
"}\n"
"QLineEdit:hover{\n"
"     border: 2px solid #000000; \n"
"     background: #FFFFFF;\n"
"    \n"
"}")
        self.lineEdit_14.setObjectName("lineEdit_14")
        self.verticalLayout_4.addWidget(self.lineEdit_14)
        self.lineEdit_15 = QtWidgets.QLineEdit(self.layoutWidget4)
        self.lineEdit_15.setStyleSheet("QLineEdit{\n"
"    background: rgb(255,192,203);\n"
"    border: 2px solid #666666; \n"
"    border-radius: 10px;  \n"
"    font-family: Arial;\n"
"    font-size:15px;\n"
"   color: #19060f;\n"
"\n"
"}\n"
"QLineEdit:focus{\n"
"     border: 2px solid #FF439F; \n"
"    background: #FFFFFF;\n"
"    \n"
"}\n"
"QLineEdit:hover{\n"
"     border: 2px solid #000000; \n"
"     background: #FFFFFF;\n"
"    \n"
"}")
        self.lineEdit_15.setObjectName("lineEdit_15")
        self.verticalLayout_4.addWidget(self.lineEdit_15)
        self.lineEdit_16 = QtWidgets.QLineEdit(self.layoutWidget4)
        self.lineEdit_16.setStyleSheet("QLineEdit{\n"
"    background: rgb(255,192,203);\n"
"    border: 2px solid #666666; \n"
"    border-radius: 10px;  \n"
"    font-family: Arial;\n"
"    font-size:15px;\n"
"   color: #19060f;\n"
"\n"
"}\n"
"QLineEdit:focus{\n"
"     border: 2px solid #FF439F; \n"
"    background: #FFFFFF;\n"
"    \n"
"}\n"
"QLineEdit:hover{\n"
"     border: 2px solid #000000; \n"
"     background: #FFFFFF;\n"
"    \n"
"}")
        self.lineEdit_16.setObjectName("lineEdit_16")
        self.verticalLayout_4.addWidget(self.lineEdit_16)
        self.lineEdit_17 = QtWidgets.QLineEdit(self.layoutWidget4)
        self.lineEdit_17.setStyleSheet("QLineEdit{\n"
"    background: rgb(255,192,203);\n"
"    border: 2px solid #666666; \n"
"    border-radius: 10px;  \n"
"    font-family: Arial;\n"
"    font-size:15px;\n"
"   color: #19060f;\n"
"\n"
"}\n"
"QLineEdit:focus{\n"
"     border: 2px solid #FF439F; \n"
"    background: #FFFFFF;\n"
"    \n"
"}\n"
"QLineEdit:hover{\n"
"     border: 2px solid #000000; \n"
"     background: #FFFFFF;\n"
"    \n"
"}")
        self.lineEdit_17.setObjectName("lineEdit_17")
        self.verticalLayout_4.addWidget(self.lineEdit_17)
        self.lineEdit_18 = QtWidgets.QLineEdit(self.layoutWidget4)
        self.lineEdit_18.setStyleSheet("QLineEdit{\n"
"    background: rgb(255,192,203);\n"
"    border: 2px solid #666666; \n"
"    border-radius: 10px;  \n"
"    font-family: Arial;\n"
"    font-size:15px;\n"
"   color: #19060f;\n"
"\n"
"}\n"
"QLineEdit:focus{\n"
"     border: 2px solid #FF439F; \n"
"    background: #FFFFFF;\n"
"    \n"
"}\n"
"QLineEdit:hover{\n"
"     border: 2px solid #000000; \n"
"     background: #FFFFFF;\n"
"    \n"
"}")
        self.lineEdit_18.setObjectName("lineEdit_18")
        self.verticalLayout_4.addWidget(self.lineEdit_18)
        self.layoutWidget5 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget5.setGeometry(QtCore.QRect(290, 180, 121, 121))
        self.layoutWidget5.setObjectName("layoutWidget5")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.layoutWidget5)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.lineEdit_23 = QtWidgets.QLineEdit(self.layoutWidget5)
        self.lineEdit_23.setStyleSheet("QLineEdit{\n"
"    background: #FFFFFF;\n"
"    border: 2px solid #666666; \n"
"    border-radius: 10px;  \n"
"    font-family: Arial;\n"
"    font-size:15px;\n"
"   color: #19060f;\n"
"\n"
"}\n"
"QLineEdit:focus{\n"
"     border: 2px solid #FF439F; \n"
"    background: #FFFFFF;\n"
"    \n"
"}\n"
"QLineEdit:hover{\n"
"     border: 2px solid #000000; \n"
"     background: #FFFFFF;\n"
"    \n"
"}")
        self.lineEdit_23.setObjectName("lineEdit_23")
        self.verticalLayout_6.addWidget(self.lineEdit_23)
        self.lineEdit_24 = QtWidgets.QLineEdit(self.layoutWidget5)
        self.lineEdit_24.setStyleSheet("QLineEdit{\n"
"    background: #FFFFFF;\n"
"    border: 2px solid #666666; \n"
"    border-radius: 10px;  \n"
"    font-family: Arial;\n"
"    font-size:15px;\n"
"   color: #19060f;\n"
"\n"
"}\n"
"QLineEdit:focus{\n"
"     border: 2px solid #FF439F; \n"
"    background: #FFFFFF;\n"
"    \n"
"}\n"
"QLineEdit:hover{\n"
"     border: 2px solid #000000; \n"
"     background: #FFFFFF;\n"
"    \n"
"}")
        self.lineEdit_24.setObjectName("lineEdit_24")
        self.verticalLayout_6.addWidget(self.lineEdit_24)
        self.layoutWidget6 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget6.setGeometry(QtCore.QRect(443, 190, 81, 101))
        self.layoutWidget6.setObjectName("layoutWidget6")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.layoutWidget6)
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.nid = QtWidgets.QLabel(self.layoutWidget6)
        self.nid.setStyleSheet("font: 75 13pt \"C059\";\n"
"color: rgb(255, 255, 255);")
        self.nid.setObjectName("nid")
        self.verticalLayout_7.addWidget(self.nid)
        self.age = QtWidgets.QLabel(self.layoutWidget6)
        self.age.setStyleSheet("font: 75 13pt \"C059\";\n"
"color: rgb(255, 255, 255);")
        self.age.setObjectName("age")
        self.verticalLayout_7.addWidget(self.age)
        self.layoutWidget7 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget7.setGeometry(QtCore.QRect(530, 190, 141, 111))
        self.layoutWidget7.setObjectName("layoutWidget7")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.layoutWidget7)
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.lineEdit_21 = QtWidgets.QLineEdit(self.layoutWidget7)
        self.lineEdit_21.setStyleSheet("QLineEdit{\n"
"    background: #FFFFFF;\n"
"    border: 2px solid #666666; \n"
"    border-radius: 10px;  \n"
"    font-family: Arial;\n"
"    font-size:15px;\n"
"   color: #19060f;\n"
"\n"
"}\n"
"QLineEdit:focus{\n"
"     border: 2px solid #FF439F; \n"
"    background: #FFFFFF;\n"
"    \n"
"}\n"
"QLineEdit:hover{\n"
"     border: 2px solid #000000; \n"
"     background: #FFFFFF;\n"
"    \n"
"}")
        self.lineEdit_21.setObjectName("lineEdit_21")
        self.verticalLayout_8.addWidget(self.lineEdit_21)
        self.lineEdit_22 = QtWidgets.QLineEdit(self.layoutWidget7)
        self.lineEdit_22.setStyleSheet("QLineEdit{\n"
"    background: #FFFFFF;\n"
"    border: 2px solid #666666; \n"
"    border-radius: 10px;  \n"
"    font-family: Arial;\n"
"    font-size:15px;\n"
"   color: #19060f;\n"
"\n"
"}\n"
"QLineEdit:focus{\n"
"     border: 2px solid #FF439F; \n"
"    background: #FFFFFF;\n"
"    \n"
"}\n"
"QLineEdit:hover{\n"
"     border: 2px solid #000000; \n"
"     background: #FFFFFF;\n"
"    \n"
"}")
        self.lineEdit_22.setObjectName("lineEdit_22")
        self.verticalLayout_8.addWidget(self.lineEdit_22)
        self.widget_2 = QtWidgets.QWidget(self.centralwidget)
        self.widget_2.setGeometry(QtCore.QRect(270, 310, 361, 71))
        self.widget_2.setStyleSheet("background-image: url(info.png);")
        self.widget_2.setObjectName("widget_2")
        self.label_5 = QtWidgets.QLabel(self.widget_2)
        self.label_5.setGeometry(QtCore.QRect(50, 20, 271, 31))
        self.label_5.setStyleSheet("background-color: rgba(191, 64, 64, 0);\n"
"font: 63 italic 14pt \"URW Bookman\";")
        self.label_5.setObjectName("label_5")
        self.widget_3 = QtWidgets.QWidget(self.centralwidget)
        self.widget_3.setGeometry(QtCore.QRect(260, 100, 361, 81))
        self.widget_3.setStyleSheet("background-image: url(info.png);")
        self.widget_3.setObjectName("widget_3")
        self.label_6 = QtWidgets.QLabel(self.widget_3)
        self.label_6.setGeometry(QtCore.QRect(90, 10, 211, 41))
        self.label_6.setStyleSheet("background-color: rgba(191, 64, 64, 0);\n"
"font: 63 italic 14pt \"URW Bookman\";")
        self.label_6.setObjectName("label_6")
        self.clear = QtWidgets.QPushButton(self.centralwidget)
        self.clear.setGeometry(QtCore.QRect(1100, 710, 89, 25))
        self.clear.setStyleSheet("QPushButton{\n"
"    background: #FFFFFF;\n"
"   background-color:#FFFFFF;\n"
"    border: 2px solid #FFFFFF; \n"
"    border-radius: 10px; \n"
"    font-family: Arial;\n"
"    font-size:15px;\n"
"    color: #19060f;\n"
"\n"
"}\n"
"QPushButton:hover{\n"
"     border: 2px solid #000000; \n"
"     background: #FFFFFF;\n"
"}\n"
"")
        self.clear.setObjectName("clear")
        self.clear.setIcon(QIcon('clear.png'))
        cancer.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(cancer)
        self.statusbar.setObjectName("statusbar")
        cancer.setStatusBar(self.statusbar)

        self.retranslateUi(cancer)
        QtCore.QMetaObject.connectSlotsByName(cancer)

    def retranslateUi(self, cancer):
        _translate = QtCore.QCoreApplication.translate
        cancer.setWindowTitle(_translate("cancer", "breast cancer"))
        self.pushButton.setText(_translate("cancer", "TEST"))
        self.pushButton.clicked.connect(self.execution)
        self.textBrowser.setHtml(_translate("cancer", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'URW Bookman\';\">this result remains an expectaion,so please see your doctor</span></p></body></html>"))
        self.label_7.setText(_translate("cancer", "RESULT"))
        self.lineEdit_20.setToolTip(_translate("cancer", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self.fractal_dimension_mean.setText(_translate("cancer", "fractal_dimension_mean"))
        self.radius_se.setText(_translate("cancer", "radius_se"))
        self.texture_se.setText(_translate("cancer", "texture_se"))
        self.perimeter_se.setText(_translate("cancer", "perimeter_se"))
        self.area_se.setText(_translate("cancer", "area_se"))
        self.smoothness_se.setText(_translate("cancer", "smoothness_se"))
        self.compactness_se.setText(_translate("cancer", "compactness_se"))
        self.concavity_se.setText(_translate("cancer", "concavity_se"))
        self.concave_points_se.setText(_translate("cancer", "concave_points_se"))
        self.label.setText(_translate("cancer", "radius_mean"))
        self.label_2.setText(_translate("cancer", "texture_mean"))
        self.label_3.setText(_translate("cancer", "perimeter_mean"))
        self.label_4.setText(_translate("cancer", "area_mean"))
        self.smoothness_mean.setText(_translate("cancer", "smoothness_mean"))
        self.compactness_mean.setText(_translate("cancer", "compactness_mean"))
        self.concavity_mean.setText(_translate("cancer", "concavity_mean"))
        self.concave_points_mean.setText(_translate("cancer", "concave_points_mean"))
        self.symmetry_mean.setText(_translate("cancer", "symmetry_mean"))
        self.Nom.setText(_translate("cancer", "Name"))
        self.Prnom.setText(_translate("cancer", "First name"))
        self.nid.setText(_translate("cancer", "N° id"))
        self.age.setText(_translate("cancer", "Age"))
        self.label_5.setText(_translate("cancer", "Values for the test procedure"))
        self.label_6.setText(_translate("cancer", "Patient information\'s"))
        self.clear.setText(_translate("cancer", "Clear"))
        self.clear.clicked.connect(self.clears)

    def prog(self):
            #---------------importer les données----------------------
            Data = pd.read_csv("data.csv")
            Data = Data.drop(columns=["id"])
            # print(Data)
            # print(Data.describe())
            # print(Data.shape)
            # print(Data.columns)
            # print(Data.isna().sum())
            #---------------vérifier si les colonnes sont de type float64
            Columns = [column for column in Data.columns if Data[column].dtype == 'float64']
            # print(Columns)

            #_______________affichage histogramme de diagnosis
            plt.figure(figsize=(20, 10))
            sns.countplot(x=Data["diagnosis"])
            # plt.show()

            # print(Data["diagnosis"].value_counts())
            #---------------affichage de tous les graphes
            sns.pairplot(Data.iloc[:, :6], hue='diagnosis')
            # plt.show()

            #---------------Analyse de corrélation
            plt.figure(figsize=(20, 10))
            corr = Data.corr()
            sns.heatmap(corr, annot=True, cmap="YlGnBu")
            # plt.show()

            #---------------traitement des données
            y_train = Data["diagnosis"]
            X_train = Data.drop(columns=["diagnosis"])
            X_train, X_test, y_train, y_test = train_test_split(X_train, y_train, test_size=0.2)

            #----------------Renvoie un sous-ensemble des colonnes du DataFrame en fonction des dtypes de colonne
            Columns = X_train.select_dtypes(exclude='object').columns
            # print(Columns)

            #------Méthodes génériques pour la préparation de modèles et l'évaluation
            model = RandomForestClassifier()
            model.fit(X_train, y_train)
            # print(model.score(X_train,y_train))
            # print(model.score(X_test,y_test))

            #---------fonction de test le model
            def test(model, radius_mean, texture_mean, perimeter_mean, area_mean, smoothness_mean, compactness_mean,
                     concavity_mean, concave_points_mean, symmetry_mean, fractal_dimension_mean, radius_se, texture_se,
                     perimeter_se, area_se, smoothness_se, compactness_se, concavity_se, concave_points_se):
                    x = np.array(
                            [radius_mean, texture_mean, perimeter_mean, area_mean, smoothness_mean, compactness_mean,
                             concavity_mean, concave_points_mean, symmetry_mean, fractal_dimension_mean, radius_se,
                             texture_se, perimeter_se, area_se, smoothness_se, compactness_se, concavity_se,
                             concave_points_se]).reshape(1, 18)
                    r = model.predict(x)
                    m = model.predict_proba(x)
                    if r == 0:
                            self.lineEdit_19.setText("bénigne ")
                            d=str(m[0, 0] * 100)+'%'
                            self.lineEdit_20.setText(str(d))
                            return r
                    else:
                            self.lineEdit_19.setText("maligne ")
                            d = str(m[0, 1] * 100) + '%'
                            self.lineEdit_20.setText(str(d))
                            return r
            #-------recouper les données saisies
            k= test(model, float(self.lineEdit.text()), float(self.lineEdit_2.text()), float(self.lineEdit_3.text()),
                 float(self.lineEdit_4.text()),float(self.lineEdit_5.text()), float(self.lineEdit_6.text()), float(self.lineEdit_7.text()),
                 float(self.lineEdit_8.text()), float(self.lineEdit_9.text()),
                 float(self.lineEdit_10.text()), float(self.lineEdit_11.text()), float(self.lineEdit_12.text()),
                 float(self.lineEdit_13.text()), float(self.lineEdit_14.text()),
                float(self.lineEdit_15.text()), float(self.lineEdit_16.text()), float(self.lineEdit_17.text()),
                 float(self.lineEdit_18.text()))
            path = 'dataP.csv'
            # Vérifier si le fichier csv existe si no en créer un fichier de saisies
            if os.path.exists(path):
                    print("")
            else:
                    datatest = "dataP.csv"
                    header = ["id", "diagnosis", "radius_mean", "texture_mean", "perimeter_mean", "area_mean",
                              "smoothness_mean", "compactness_mean",
                              "concavity_mean", "concave_points_mean", "symmetry_mean", "fractal_dimension_mean",
                              "radius_se",
                              "texture_se", "perimeter_se", "area_se", "smoothness_se", "compactness_se",
                              "concavity_se",
                              "concave_points_se"]

                    with open(datatest, "a", newline="") as csv_file:
                            writer = csv.writer(csv_file)
                            writer.writerow(header)
            datatest = "dataP.csv"
            with open(datatest, "a", newline="") as csv_file:
                    writer = csv.writer(csv_file)
                    writer.writerow([int(self.lineEdit_21.text()),int(k),float(self.lineEdit.text()), float(self.lineEdit_2.text()), float(self.lineEdit_3.text()),
                 float(self.lineEdit_4.text()),float(self.lineEdit_5.text()), float(self.lineEdit_6.text()), float(self.lineEdit_7.text()),
                float(self.lineEdit_8.text()), float(self.lineEdit_9.text()),
                float(self.lineEdit_10.text()), float(self.lineEdit_11.text()), float(self.lineEdit_12.text()),
                 float(self.lineEdit_13.text()), float(self.lineEdit_14.text()),
                float(self.lineEdit_15.text()), float(self.lineEdit_16.text()), float(self.lineEdit_17.text()),
                 float(self.lineEdit_18.text())])


            #####################################################"
            # Vérifier si le fichier csv existe si no en créer un fichier de saisies le nom et le prenom et id
            path = 'maladP.csv'
            # Vérifier si le fichier existe ou non
            if os.path.exists(path):
                    print("")
            else:
                    datatest = "maladP.csv"
                    header = ["id", "Name", "First name", "Age","diagnosis"]

                    with open(datatest, "a", newline="") as csv_file:
                            writer = csv.writer(csv_file)
                            writer.writerow(header)
            datatest = "maladP.csv"
            with open(datatest, "a", newline="") as csv_file:
                    writer = csv.writer(csv_file)
                    writer.writerow([int(self.lineEdit_21.text()),self.lineEdit_23.text(),self.lineEdit_24.text(),int(self.lineEdit_22.text()), int(k) ])

    # la fonction pour execution le test
    def execution(self):
            self.prog()
    #fonction vidier  le saisies de donnes
    def clears(self):
            ui.setupUi(MainWindow)

app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui = Ui_cancer()
ui.setupUi(MainWindow)
MainWindow.show()
sys.exit(app.exec_())

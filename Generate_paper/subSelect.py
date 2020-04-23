#!/usr/bin/env python
# -*- coding: utf-8 -*-
from PyQt5 import QtWidgets, QtCore, QtGui



class subSelectWindow(QtWidgets.QWidget):
    semsub = QtCore.pyqtSignal(str, str)

    def __init__(self):
        super(subSelectWindow, self).__init__()
        self.resize(800, 600)
        self.selectSem = QtWidgets.QComboBox(self)
        self.selectSem.setGeometry(QtCore.QRect(175, 100, 450, 80))
        self.selectSem.setObjectName("selectSem")
        font = self.selectSem.font()
        font.setPointSize(15)
        self.selectSem.setFont(font)
        self.selectSubject = QtWidgets.QComboBox(self)
        self.selectSubject.setGeometry(QtCore.QRect(175, 220, 450, 80))
        self.selectSubject.setObjectName("selectSubject")
        font = self.selectSubject.font()
        font.setPointSize(12)
        self.selectSubject.setFont(font)
        self.selectBtn = QtWidgets.QPushButton(self)
        self.selectBtn.setGeometry(QtCore.QRect(225, 350, 350, 90))
        self.selectBtn.setObjectName("selectBtn")
        self.selectBtn.setText("Confirm and close")
        self.selectBtn.setStyleSheet("#selectBtn{\n"
                                     "display: inline-block;\n"
                                     "  padding: 15px 25px;\n"
                                     "  cursor: pointer;\n"
                                     "  text-align: center;\n"
                                     "  text-decoration: none;\n"
                                     "  outline: none;\n"
                                     "  color: #fff;\n"
                                     "  background-color: #4da6ff;\n"
                                     "  border: none;\n"
                                     "  border-radius: 45px;\n"
                                     "  box-shadow: 0 9px #999;\n"
                                     "}\n"
                                     )
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.selectBtn.setFont(font)
        self.selectSem.addItems(
            [" SEM I", " SEM II", " SEM III", " SEM IV", " SEM V", " SEM VI", " SEM VII", " SEM VIII"])
        self.selectSem.activated[str].connect(self.onSemSelected)
        self.selectBtn.clicked.connect(self.send_clicked)
        self.setWindowTitle("Select Subject")

    def send_clicked(self):

        self.semsub.emit(self.selectSem.currentText(), self.selectSubject.currentText())
        self.close()

    def onSemSelected(self, text):

        if (text == ' SEM I'):
            self.selectSubject.clear()
            self.selectSubject.addItems([" Applied Mathematics 1", " Applied Chemistry 1", " Applied Physics 1",
                                         " Basic Electrical and Electronic Engineering", " Engineering Mechanics",
                                         " Environmental Studies"])
        elif (text == ' SEM II'):
            self.selectSubject.clear()
            self.selectSubject.addItems(
                [" Applied Mathematics 2", " Applied Chemistry 2", " Applied Physics 2", " Engineering Drawing",
                 " Structured Programming Approach", " Communication Skills"])
        elif (text == ' SEM III'):
            self.selectSubject.clear()
            self.selectSubject.addItems(
                [" Data Structure and Analysis", " Logic Design", " Principle of Communications",
                 " Database Managemnet System", " Applied Mathematics 3"])
        elif (text == ' SEM IV'):
            self.selectSubject.clear()
            self.selectSubject.addItems([" Automata Theory", " Operating Systems", " Computer Networks",
                                         " Computer Organizations and Architecture", " Applied Mathematics 4"])
        elif (text == ' SEM V'):
            self.selectSubject.clear()
            self.selectSubject.addItems(
                [" Microcontroller and Embedded Programming", " Cryptography and Network Security",
                 " Internet Programming", " E-commerce and E-business", " Advanced Data Management Technology"])
        elif (text == ' SEM VI'):
            self.selectSubject.clear()
            self.selectSubject.addItems(
                [" Software Engineering with\n Project Management", " Data Mining and Business Intelligence",
                 " Cloud Computing and Services", " Digital Forensics", " Wireless Networks"])
        elif (text == ' SEM VII'):
            self.selectSubject.clear()
            self.selectSubject.addItems(
                [" Enterprise Network Design", " Infrastructure Security", " Artificial Intelligence",
                 " Software Testing and\n Quality Assurance", " Management Information System"])
        elif (text == ' SEM VIII'):
            self.selectSubject.clear()
            self.selectSubject.addItems([" Enterprise Resource Managenment", " Big Data Analytics",
                                         " Project Management", " Internet Of Everything"])

#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import random

import mysql.connector
from Generate_paper import selectModules, printQuestion
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtGui import QIcon


class formattWindow(QtWidgets.QWidget):
    listQ = []
    loaded = 0
    questionLoaded = 0

    def __init__(self):
        super(formattWindow, self).__init__()
        self.resize(800, 500)
        self.printQuestion = printQuestion.printQuestion()
        self.selectBtn = QtWidgets.QPushButton(self)
        self.selectBtn.setGeometry(QtCore.QRect(300, 680, 350, 90))
        self.selectBtn.setObjectName("selectBtn")
        self.selectBtn.setText("Next   >>")
        self.selectBtn.setStyleSheet("#selectBtn{\n"
                                     "  padding: 15px 25px;\n"
                                     "  background-color: #47d147;\n"
                                     "  color: #fff;\n"
                                     "  border: none;\n"
                                     "  border-radius: 45px;\n"
                                     "}\n"
                                     )
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.selectBtn.setFont(font)
        self.selectBtn.hide()

        self.loadBtn = QtWidgets.QPushButton(self)
        self.loadBtn.setGeometry(QtCore.QRect(300, 650, 350, 90))
        self.loadBtn.setObjectName("loadBtn")
        self.loadBtn.setText("Next    >>")
        self.loadBtn.setStyleSheet("#loadBtn{\n"
                                   "  outline: none;\n"
                                   "  color: #fff;\n"
                                   "  background-color: #4da6ff;\n"
                                   "  border: none;\n"
                                   "}\n"
                                   )
        self.loadBtn.setFont(font)

        self.generateBtn = QtWidgets.QPushButton(self)
        self.generateBtn.setGeometry(QtCore.QRect(225, 350, 350, 90))
        self.generateBtn.setObjectName("generateBtn")
        self.generateBtn.setText("Generate Paper    >>")
        self.generateBtn.setStyleSheet("#generateBtn{\n"
                                       "  outline: none;\n"
                                       "  color: #fff;\n"
                                       "  background-color: #4da6ff;\n"
                                       "  border: none;\n"
                                       "}\n"
                                       )
        self.generateBtn.setFont(font)
        self.generateBtn.hide()
        self.setWindowTitle("Format")

        self.calendarBtn = QtWidgets.QPushButton(self)
        self.calendarBtn.setGeometry(QtCore.QRect(600, 100, 35, 35))
        self.calendarBtn.setObjectName("calendarBtn")
        self.calendarBtn.setIcon(QtGui.QIcon("C:/Users/harish/PycharmProjects/QPgenerator/calendar.png"))
        self.calendarBtn.setIconSize(QtCore.QSize(35, 35))
        self.calendarBtn.setObjectName("selectBtn")
        self.calendarBtn.clicked.connect(self.showCalWid)

        # Labels
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.marksLabel = QtWidgets.QLabel(self)
        self.marksLabel.setGeometry(QtCore.QRect(120, 30, 170, 40))
        self.marksLabel.setFont(font)
        self.marksLabel.setStyleSheet("")
        self.marksLabel.setText("Total Marks :")
        self.marksLabel.setObjectName("marksLabel")
        self.marksLabel.hide()

        self.dateLabel = QtWidgets.QLabel(self)
        self.dateLabel.setGeometry(QtCore.QRect(120, 100, 170, 40))
        self.dateLabel.setFont(font)
        self.dateLabel.setStyleSheet("")
        self.dateLabel.setText("Date* :")
        self.dateLabel.setObjectName("dateLabel")

        self.timeLabel = QtWidgets.QLabel(self)
        self.timeLabel.setGeometry(QtCore.QRect(120, 170, 170, 40))
        self.timeLabel.setFont(font)
        self.timeLabel.setStyleSheet("")
        self.timeLabel.setText("Duration* :")
        self.timeLabel.setObjectName("timeLabel")

        self.examLabel = QtWidgets.QLabel(self)
        self.examLabel.setGeometry(QtCore.QRect(120, 240, 170, 40))
        self.examLabel.setFont(font)
        self.examLabel.setStyleSheet("")
        self.examLabel.setText("Examination* :")
        self.examLabel.setObjectName("examLabel")

        self.instructionLabel = QtWidgets.QLabel(self)
        self.instructionLabel.setGeometry(QtCore.QRect(120, 310, 170, 40))
        self.instructionLabel.setFont(font)
        self.instructionLabel.setStyleSheet("")
        self.instructionLabel.setText("Instructions :")
        self.instructionLabel.setObjectName("instructionLabel")

        self.question4CountLabel = QtWidgets.QLabel(self)
        self.question4CountLabel.setGeometry(QtCore.QRect(700, 100, 170, 50))
        font.setPointSize(10)
        self.question4CountLabel.setFont(font)
        self.question4CountLabel.setStyleSheet("")
        self.question4CountLabel.setText("4 Marks :")
        self.question4CountLabel.setObjectName("question4CountLabel")

        self.question5CountLabel = QtWidgets.QLabel(self)
        self.question5CountLabel.setGeometry(QtCore.QRect(700, 130, 170, 50))
        self.question5CountLabel.setFont(font)
        self.question5CountLabel.setStyleSheet("")
        self.question5CountLabel.setText("5 Marks :")
        self.question5CountLabel.setObjectName("question5CountLabel")

        self.question6CountLabel = QtWidgets.QLabel(self)
        self.question6CountLabel.setGeometry(QtCore.QRect(700, 160, 170, 50))
        self.question6CountLabel.setFont(font)
        self.question6CountLabel.setStyleSheet("")
        self.question6CountLabel.setText("6 Marks :")
        self.question6CountLabel.setObjectName("question6CountLabel")

        self.question8CountLabel = QtWidgets.QLabel(self)
        self.question8CountLabel.setGeometry(QtCore.QRect(700, 190, 170, 50))
        self.question8CountLabel.setFont(font)
        self.question8CountLabel.setStyleSheet("")
        self.question8CountLabel.setText("8 Marks :")
        self.question8CountLabel.setObjectName("question8CountLabel")

        self.question10CountLabel = QtWidgets.QLabel(self)
        self.question10CountLabel.setGeometry(QtCore.QRect(700, 220, 170, 50))
        self.question10CountLabel.setFont(font)
        self.question10CountLabel.setStyleSheet("")
        self.question10CountLabel.setText("10 Marks :")
        self.question10CountLabel.setObjectName("question10CountLabel")

        self.question4CountLabel.hide()
        self.question5CountLabel.hide()
        self.question6CountLabel.hide()
        self.question8CountLabel.hide()
        self.question10CountLabel.hide()

        self.cb1Label = QtWidgets.QLabel(self)
        self.cb1Label.setGeometry(QtCore.QRect(120, 220, 300, 40))
        font.setPointSize(15)
        self.cb1Label.setFont(font)
        self.cb1Label.setStyleSheet("")
        self.cb1Label.setText("Question no. 1 :")
        self.cb1Label.setObjectName("cb2Label")
        self.cb1Label.hide()

        self.cb2Label = QtWidgets.QLabel(self)
        self.cb2Label.setGeometry(QtCore.QRect(120, 280, 300, 40))
        self.cb2Label.setFont(font)
        self.cb2Label.setStyleSheet("")
        self.cb2Label.setText("Question no. 2 :")
        self.cb2Label.setObjectName("cb2Label")
        self.cb2Label.hide()

        self.cb3Label = QtWidgets.QLabel(self)
        self.cb3Label.setGeometry(QtCore.QRect(120, 340, 300, 40))
        self.cb3Label.setFont(font)
        self.cb3Label.setStyleSheet("")
        self.cb3Label.setText("Question no. 3 :")
        self.cb3Label.setObjectName("cb3Label")
        self.cb3Label.hide()

        self.cb4Label = QtWidgets.QLabel(self)
        self.cb4Label.setGeometry(QtCore.QRect(120, 400, 300, 40))
        self.cb4Label.setFont(font)
        self.cb4Label.setStyleSheet("")
        self.cb4Label.setText("Question no. 4 :")
        self.cb4Label.setObjectName("cb4Label")
        self.cb4Label.hide()

        self.cb5Label = QtWidgets.QLabel(self)
        self.cb5Label.setGeometry(QtCore.QRect(120, 460, 300, 40))
        self.cb5Label.setFont(font)
        self.cb5Label.setStyleSheet("")
        self.cb5Label.setText("Question no. 5 :")
        self.cb5Label.setObjectName("cb5Label")
        self.cb5Label.hide()

        self.cb6Label = QtWidgets.QLabel(self)
        self.cb6Label.setGeometry(QtCore.QRect(120, 520, 300, 40))
        self.cb6Label.setFont(font)
        self.cb6Label.setStyleSheet("")
        self.cb6Label.setText("Question no. 6 :")
        self.cb6Label.setObjectName("cb6Label")
        self.cb6Label.hide()

        self.fileLabel = QtWidgets.QLabel(self)
        self.fileLabel.setGeometry(QtCore.QRect(175, 100, 450, 80))
        self.fileLabel.setFont(font)
        self.fileLabel.setStyleSheet("")
        self.fileLabel.setText("Enter File Name :")
        self.fileLabel.setObjectName("fileLabel")
        self.fileLabel.hide()

        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(60)

        # ERROR LABELS
        self.errorDate = QtWidgets.QLabel(self)
        self.errorDate.setGeometry(QtCore.QRect(640, 100, 300, 60))
        self.errorDate.setFont(font)
        self.errorDate.setObjectName("errorDate")
        self.errorDate.setStyleSheet("#errorDate{\n"
                                     "  color: red;\n"
                                     "}\n")
        self.errorDate.setText("This field cannot be empty")
        self.errorDate.hide()

        self.errorDuration = QtWidgets.QLabel(self)
        self.errorDuration.setGeometry(QtCore.QRect(640, 170, 300, 60))
        self.errorDuration.setFont(font)
        self.errorDuration.setObjectName("errorDuration")
        self.errorDuration.setStyleSheet("#errorDuration{\n"
                                         "  color: red;\n"
                                         "}\n")
        self.errorDuration.setText("This field cannot be empty")
        self.errorDuration.hide()

        self.errorExam = QtWidgets.QLabel(self)
        self.errorExam.setGeometry(QtCore.QRect(710, 240, 300, 60))
        self.errorExam.setFont(font)
        self.errorExam.setObjectName("errorExam")
        self.errorExam.setStyleSheet("#errorExam{\n"
                                     "  color: red;\n"
                                     "}\n")
        self.errorExam.setText("This field cannot be empty")
        self.errorExam.hide()

        self.dateEdit = QtWidgets.QLineEdit(self)
        self.dateEdit.setGeometry(QtCore.QRect(300, 100, 300, 50))
        self.dateEdit.setObjectName("dateEdit")
        font.setPointSize(12)
        font.setWeight(60)
        self.dateEdit.setFont(font)
        self.moduleList = []

        self.timeEdit = QtWidgets.QLineEdit(self)
        self.timeEdit.setGeometry(QtCore.QRect(300, 170, 300, 50))
        self.timeEdit.setObjectName("timeEdit")
        self.timeEdit.setFont(font)

        self.examEdit = QtWidgets.QLineEdit(self)
        self.examEdit.setGeometry(QtCore.QRect(300, 240, 400, 50))
        self.examEdit.setObjectName("examEdit")
        self.examEdit.setFont(font)

        self.instructionEdit = QtWidgets.QPlainTextEdit(self)
        self.instructionEdit.setGeometry(QtCore.QRect(300, 310, 400, 120))
        self.instructionEdit.setObjectName("questionEdit")
        self.instructionEdit.setFont(font)

        self.fileEdit = QtWidgets.QLineEdit(self)
        self.fileEdit.setGeometry(QtCore.QRect(175, 200, 450, 80))
        self.fileEdit.setObjectName("fileEdit")
        self.fileEdit.setFont(font)
        self.fileEdit.hide()

        self.subject = ""
        self.semester = ""
        self.sub = ""
        self.sem = ""

        self.marksCombo = QtWidgets.QComboBox(self)
        self.marksCombo.setGeometry(QtCore.QRect(300, 30, 300, 50))
        self.marksCombo.setObjectName("marksCombo")
        font = self.marksCombo.font()
        font.setPointSize(15)
        self.marksCombo.setFont(font)
        self.marksCombo.addItems([" 10", " 20", " 30", " 40", " 50", " 60", " 70", " 80", " 90", " 100", " 120"])
        self.marksCombo.activated[str].connect(self.onMarksSelected)
        self.marksCombo.hide()

        self.q1 = []
        self.q2 = []
        self.q3 = []
        self.q4 = []
        self.q5 = []
        self.q6 = []

        self.cb1 = QtWidgets.QComboBox(self)
        self.cb1.setGeometry(QtCore.QRect(350, 220, 300, 50))
        self.cb1.setObjectName("cb1")
        font = self.cb1.font()
        font.setPointSize(13)
        self.cb1.setFont(font)
        self.cb1.hide()
        self.cb1.activated[str].connect(self.oncb1Selected)

        self.cb2 = QtWidgets.QComboBox(self)
        self.cb2.setGeometry(QtCore.QRect(350, 280, 300, 50))
        self.cb2.setObjectName("cb2")
        font = self.cb2.font()
        font.setPointSize(13)
        self.cb2.setFont(font)
        self.cb2.hide()
        self.cb2.activated[str].connect(self.oncb2Selected)

        self.cb3 = QtWidgets.QComboBox(self)
        self.cb3.setGeometry(QtCore.QRect(350, 340, 300, 50))
        self.cb3.setObjectName("cb3")
        font = self.cb3.font()
        font.setPointSize(13)
        self.cb3.setFont(font)
        self.cb3.hide()
        self.cb3.activated[str].connect(self.oncb3Selected)

        self.cb4 = QtWidgets.QComboBox(self)
        self.cb4.setGeometry(QtCore.QRect(350, 400, 300, 50))
        self.cb4.setObjectName("cb4")
        font = self.cb4.font()
        font.setPointSize(13)
        self.cb4.setFont(font)
        self.cb4.hide()
        self.cb4.activated[str].connect(self.oncb4Selected)

        self.cb5 = QtWidgets.QComboBox(self)
        self.cb5.setGeometry(QtCore.QRect(350, 460, 300, 50))
        self.cb5.setObjectName("cb5")
        font = self.cb4.font()
        font.setPointSize(13)
        self.cb5.setFont(font)
        self.cb5.hide()
        self.cb5.activated[str].connect(self.oncb5Selected)

        self.cb6 = QtWidgets.QComboBox(self)
        self.cb6.setGeometry(QtCore.QRect(350, 520, 300, 50))
        self.cb6.setObjectName("cb6")
        font = self.cb6.font()
        font.setPointSize(13)
        self.cb6.setFont(font)
        self.cb6.hide()
        self.cb6.activated[str].connect(self.oncb6Selected)

        self.listQ = []
        self.fomarks = []
        self.fmarks = []
        self.smarks = []
        self.emarks = []
        self.tmarks = []

        self.loadBtn.clicked.connect(self.connection)
        self.selectBtn.clicked.connect(self.hideAllElements)
        self.generateBtn.clicked.connect(self.generatePaper)

    def showCalWid(self):
        self.calendar = QtWidgets.QCalendarWidget()
        self.calendar.setMinimumDate(QtCore.QDate(1900, 1, 1))
        self.calendar.setMaximumDate(QtCore.QDate(3000, 1, 1))
        self.calendar.setGridVisible(True)
        self.calendar.clicked.connect(self.updateDate)
        self.calendar.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.calendar.setStyleSheet('background: white; color: black')
        self.calendar.setGridVisible(True)
        pos = QtGui.QCursor.pos()
        self.calendar.setGeometry(pos.x(), pos.y(), 400, 300)
        self.calendar.show()

    def connection(self):
        global questionLoaded
        date = self.dateEdit.text()
        time = self.timeEdit.text()
        exam = self.examEdit.text()
        # self.validate(date, time, exam)
        if (date != "" and time != "" and exam != ""):
            if (len(self.listQ) == 0):
                self.conn = mysql.connector.connect(host="localhost", database=self.semester, user="root", password="")
                temp = ""
                if (len(self.moduleList) > 0):
                    for i in range(len(self.moduleList)):
                        temp = temp + " chapter=" + str(self.moduleList[i])
                        if (i + 1 < len(self.moduleList)):
                            temp = temp + " or"
                    query = "select question, weightage from " + self.subject + " where(" + temp + ") and type='theory'"
                    print(query)

                    cur = self.conn.cursor()
                    cur.execute(query)
                    rows = cur.fetchall()
                    self.conn.commit()
                    self.conn.close()
                    for j in rows:
                        print(j)
                        self.listQ.append(j)
                    for i in range(len(self.listQ)):
                        if (self.listQ[i][1] == 4):
                            self.fomarks.append(self.listQ[i])
                            i += 1

                    for i in range(len(self.listQ)):
                        if (self.listQ[i][1] == 5):
                            self.fmarks.append(self.listQ[i])
                            i += 1

                    for i in range(len(self.listQ)):
                        if (self.listQ[i][1] == 10):
                            self.tmarks.append(self.listQ[i])
                            i += 1
                    for i in range(len(self.listQ)):
                        if (self.listQ[i][1] == 6):
                            self.smarks.append(self.listQ[i])
                            i += 1
                    for i in range(len(self.listQ)):
                        if (self.listQ[i][1] == 8):
                            self.emarks.append(self.listQ[i])
                            i += 1

                random.shuffle(self.fomarks)
                random.shuffle(self.fmarks)
                random.shuffle(self.tmarks)
                random.shuffle(self.smarks)
                random.shuffle(self.emarks)
                self.question4CountLabel.setText(" 4 marks  : " + str(len(self.fomarks)))
                self.question5CountLabel.setText(" 5 marks  : " + str(len(self.fmarks)))
                self.question6CountLabel.setText(" 6 marks  : " + str(len(self.smarks)))
                self.question8CountLabel.setText(" 8 marks  : " + str(len(self.emarks)))
                self.question10CountLabel.setText("10 marks : " + str(len(self.tmarks)))
                self.printQuestion = printQuestion.printQuestion()
                self.printQuestion.subject = self.sub
                self.instructionLabel.hide()
                self.instructionEdit.hide()
                self.examLabel.hide()
                self.examEdit.hide()
                self.timeLabel.hide()
                self.timeEdit.hide()
                self.dateLabel.hide()
                self.dateEdit.hide()
                self.marksCombo.show()
                self.marksLabel.show()
                self.selectBtn.show()
                self.question4CountLabel.show()
                self.question5CountLabel.show()
                self.question6CountLabel.show()
                self.question8CountLabel.show()
                self.question10CountLabel.show()
                self.loadBtn.hide()
                self.errorExam.hide()
                self.errorDuration.hide()
                self.errorDate.hide()

        else:
            self.validate(date, time, exam)

    def validate(self, date, time, exam):
        if (date == ""):
            self.errorDate.show()
        else:
            self.errorDate.hide()
        if (time == ""):
            self.errorDuration.show()
        else:
            self.errorDuration.hide()
        if (exam == ""):
            self.errorExam.show()
        else:
            self.errorExam.hide()

    def updateDate(self, *args):
        getDate = self.calendar.selectedDate().toString(("dd-MM-yyyy"))

        self.dateEdit.setText(getDate)
        self.calendar.deleteLater()

    def updateList(self, text):
        q = []
        if (text == " 5, 5"):
            if (len(self.fmarks) >= 2):
                q = [self.fmarks.pop(), self.fmarks.pop()]
                self.updateCount()
            else:
                print("Out of question 5's")

        if (text == " 10"):
            if (len(self.tmarks) >= 1):
                q = [self.tmarks.pop()]
                self.updateCount()

            else:
                print("Out of question 10's")

        if (text == " 5, 5, 5"):
            if (len(self.fmarks) >= 3):
                q = [self.fmarks.pop(), self.fmarks.pop(), self.fmarks.pop()]
                self.updateCount()
            else:
                print("Out of question 5's")

        if (text == " 5, 10"):
            if (len(self.fmarks) >= 1 and len(self.tmarks) >= 1):
                q = [self.fmarks.pop(), self.tmarks.pop()]
                self.updateCount()
            else:
                print("Out of question 10s or 5s")
        if (text == " 5, 5, 5, 5"):
            if (len(self.fmarks) >= 4):
                q = [self.fmarks.pop(), self.fmarks.pop(), self.fmarks.pop(), self.fmarks.pop()]
                self.updateCount()
            else:
                print("Out of question 5's")
        if (text == " 5, 5, 10"):
            if (len(self.fmarks) >= 2 and len(self.tmarks) >= 1):
                q = [self.fmarks.pop(), self.fmarks.pop(), self.tmarks.pop()]
                self.updateCount()
            else:
                print("Out of question 10s or 5s")
        if (text == " 8, 6, 6"):
            if (len(self.emarks) >= 1 and len(self.smarks) >= 2):
                q = [self.emarks.pop(), self.smarks.pop(), self.smarks.pop()]
                self.updateCount()
            else:
                print("Out of question 8s or 6s")

        if (text == " 8, 8, 4"):
            if (len(self.emarks) >= 2 and len(self.fomarks) >= 1):
                q = [self.emarks.pop(), self.emarks.pop(), self.fomarks.pop()]
                self.updateCount()
            else:
                print("Out of question 8s or 4s")
        if (text == " 10, 10"):
            if (len(self.tmarks) >= 2):
                q = [self.tmarks.pop(), self.tmarks.pop()]
                self.updateCount()
            else:
                print("Out of question 10s")
        return q

    def oncb1Selected(self, text):
        self.q1 = self.updateList(text)

    def oncb2Selected(self, text):
        self.q2 = self.updateList(text)

    def oncb3Selected(self, text):
        self.q3 = self.updateList(text)

    def oncb4Selected(self, text):
        self.q4 = self.updateList(text)

    def oncb5Selected(self, text):
        self.q5 = self.updateList(text)

    def oncb6Selected(self, text):
        self.q6 = self.updateList(text)

    def updateCount(self):
        self.question4CountLabel.setText(" 4 marks  : " + str(len(self.fomarks)))
        self.question5CountLabel.setText(" 5 marks  : " + str(len(self.fmarks)))
        self.question6CountLabel.setText(" 6 marks  : " + str(len(self.smarks)))
        self.question8CountLabel.setText(" 8 marks  : " + str(len(self.emarks)))
        self.question10CountLabel.setText("10 marks : " + str(len(self.tmarks)))

    def hideAllElements(self):
        self.cb1.hide()
        self.cb2.hide()
        self.cb3.hide()
        self.cb4.hide()
        self.cb5.hide()
        self.cb6.hide()
        self.cb1Label.hide()
        self.cb2Label.hide()
        self.cb3Label.hide()
        self.cb4Label.hide()
        self.cb5Label.hide()
        self.cb6Label.hide()
        self.marksLabel.hide()
        self.marksCombo.hide()
        self.selectBtn.hide()
        self.calendarBtn.hide()
        self.question10CountLabel.hide()
        self.question8CountLabel.hide()
        self.question6CountLabel.hide()
        self.question5CountLabel.hide()
        self.question4CountLabel.hide()
        self.resize(800,600)
        self.generateBtn.show()
        self.fileLabel.show()
        self.fileEdit.show()


    def onMarksSelected(self, text):

        def hideAll():
            self.cb1.hide()
            self.cb1Label.hide()
            self.cb2.hide()
            self.cb2Label.hide()
            self.cb3.hide()
            self.cb3Label.hide()
            self.cb4.hide()
            self.cb4Label.hide()
            self.cb5.hide()
            self.cb5Label.hide()
            self.cb6.hide()
            self.cb6Label.hide()

        if (text == ' 10'):
            hideAll()
            self.cb1.clear()
            self.cb1.addItems(["Enter format", " 5, 5", " 10"])
            self.cb1.show()
            self.cb1Label.show()
        elif (text == " 20"):
            hideAll()
            self.cb1.clear()
            self.cb1.addItems(["Enter format", " 5, 5", " 10"])
            self.cb1.show()
            self.cb1Label.show()
            self.cb2.clear()
            self.cb2.addItems(["Enter format", " 5, 5", " 10"])
            self.cb2.show()
            self.cb2Label.show()
        elif (text == " 30"):
            hideAll()
            self.cb1.clear()
            self.cb1.addItems(["Enter format", " 5, 5, 5", " 5, 10"])
            self.cb1.show()
            self.cb1Label.show()
            self.cb2.clear()
            self.cb2.addItems(["Enter format", " 5, 5, 5", " 5, 10"])
            self.cb2.show()
            self.cb2Label.show()
        elif (text == " 40"):
            hideAll()
            self.cb1.clear()
            self.cb1.addItems(["Enter format", " 5, 5, 5, 5", " 5, 5, 10", " 8, 6, 6", " 8, 8, 4", " 10, 10"])
            self.cb1.show()
            self.cb1Label.show()
            self.cb2.clear()
            self.cb2.addItems(["Enter format", " 5, 5, 5, 5", " 5, 5, 10", " 8, 6, 6", " 8, 8, 4", " 10, 10"])
            self.cb2.show()
            self.cb2Label.show()
        elif (text == " 50"):
            hideAll()
            self.cb1.clear()
            self.cb1.addItems(["Enter format", " 5, 5, 5", " 5, 10"])
            self.cb1.show()
            self.cb1Label.show()
            self.cb2.clear()
            self.cb2.addItems(["Enter format", " 5, 5, 5", " 5, 10"])
            self.cb2.show()
            self.cb2Label.show()
            self.cb3.clear()
            self.cb3.addItems(["Enter format", " 5, 5, 5, 5", " 5, 5, 10", " 8, 6, 6", " 8, 8, 4", " 10, 10"])
            self.cb3.show()
            self.cb3Label.show()
        elif (text == " 60"):
            hideAll()
            self.cb1.clear()
            self.cb1.addItems(["Enter format", " 5, 5, 5, 5", " 5, 5, 10", " 8, 6, 6", " 8, 8, 4", " 10, 10"])
            self.cb1.show()
            self.cb1Label.show()
            self.cb2.clear()
            self.cb2.addItems(["Enter format", " 5, 5, 5, 5", " 5, 5, 10", " 8, 6, 6", " 8, 8, 4", " 10, 10"])
            self.cb2.show()
            self.cb2Label.show()
            self.cb3.clear()
            self.cb3.addItems(["Enter format", " 5, 5, 5, 5", " 5, 5, 10", " 8, 6, 6", " 8, 8, 4", " 10, 10"])
            self.cb3.show()
            self.cb3Label.show()
        elif (text == " 70"):
            hideAll()
            self.cb1.clear()
            self.cb1.addItems(["Enter format", " 5, 5, 5", " 5, 10"])
            self.cb1.show()
            self.cb1Label.show()
            self.cb2.clear()
            self.cb2.addItems(["Enter format", " 5, 5, 5", " 5, 10"])
            self.cb2.show()
            self.cb2Label.show()
            self.cb3.clear()
            self.cb3.addItems(["Enter format", " 5, 5, 5, 5", " 5, 5, 10", " 8, 6, 6", " 8, 8, 4", " 10, 10"])
            self.cb3.show()
            self.cb3Label.show()
            self.cb4.clear()
            self.cb4.addItems(["Enter format", " 5, 5, 5, 5", " 5, 5, 10", " 8, 6, 6", " 8, 8, 4", " 10, 10"])
            self.cb4.show()
            self.cb4Label.show()


        elif (text == " 80"):
            hideAll()
            self.cb1.clear()
            self.cb1.addItems(["Enter format", " 5, 5, 5, 5", " 5, 5, 10", " 8, 6, 6", " 8, 8, 4", " 10, 10"])
            self.cb1.show()
            self.cb1Label.show()
            self.cb2.clear()
            self.cb2.addItems(["Enter format", " 5, 5, 5, 5", " 5, 5, 10", " 8, 6, 6", " 8, 8, 4", " 10, 10"])
            self.cb2.show()
            self.cb2Label.show()
            self.cb3.clear()
            self.cb3.addItems(["Enter format", " 5, 5, 5, 5", " 5, 5, 10", " 8, 6, 6", " 8, 8, 4", " 10, 10"])
            self.cb3.show()
            self.cb3Label.show()
            self.cb4.clear()
            self.cb4.addItems(["Enter format", " 5, 5, 5, 5", " 5, 5, 10", " 8, 6, 6", " 8, 8, 4", " 10, 10"])
            self.cb4.show()
            self.cb4Label.show()
        elif (text == " 90"):
            hideAll()
            self.cb1.clear()
            self.cb1.addItems(["Enter format", " 5, 5, 5", " 5, 10"])
            self.cb1.show()
            self.cb1Label.show()
            self.cb2.clear()
            self.cb2.addItems(["Enter format", " 5, 5, 5", " 5, 10"])
            self.cb2.show()
            self.cb2Label.show()
            self.cb3.clear()
            self.cb3.addItems(["Enter format", " 5, 5, 5, 5", " 5, 5, 10", " 8, 6, 6", " 8, 8, 4", " 10, 10"])
            self.cb3.show()
            self.cb3Label.show()
            self.cb4.clear()
            self.cb4.addItems(["Enter format", " 5, 5, 5, 5", " 5, 5, 10", " 8, 6, 6", " 8, 8, 4", " 10, 10"])
            self.cb4.show()
            self.cb4Label.show()
            self.cb5.clear()
            self.cb5.addItems(["Enter format", " 5, 5, 5, 5", " 5, 5, 10", " 8, 6, 6", " 8, 8, 4", " 10, 10"])
            self.cb5.show()
            self.cb5Label.show()
        elif (text == " 100"):
            hideAll()
            self.cb1.clear()
            self.cb1.addItems(["Enter format", " 5, 5, 5, 5", " 5, 5, 10", " 8, 6, 6", " 8, 8, 4", " 10, 10"])
            self.cb1.show()
            self.cb1Label.show()
            self.cb2.clear()
            self.cb2.addItems(["Enter format", " 5, 5, 5, 5", " 5, 5, 10", " 8, 6, 6", " 8, 8, 4", " 10, 10"])
            self.cb2.show()
            self.cb2Label.show()
            self.cb3.clear()
            self.cb3.addItems(["Enter format", " 5, 5, 5, 5", " 5, 5, 10", " 8, 6, 6", " 8, 8, 4", " 10, 10"])
            self.cb3.show()
            self.cb3Label.show()
            self.cb4.clear()
            self.cb4.addItems([" 5, 5, 5, 5", " 5, 5, 10", " 8, 6, 6", " 8, 8, 4", " 10, 10"])
            self.cb4.show()
            self.cb4Label.show()
            self.cb5.clear()
            self.cb5.addItems(["Enter format", " 5, 5, 5, 5", " 5, 5, 10", " 8, 6, 6", " 8, 8, 4", " 10, 10"])
            self.cb5.show()
            self.cb5Label.show()
        elif (text == " 120"):
            hideAll()
            self.cb1.clear()
            self.cb1.addItems(["Enter format", " 5, 5, 5, 5", " 5, 5, 10", " 8, 6, 6", " 8, 8, 4", " 10, 10"])
            self.cb1.show()
            self.cb1Label.show()
            self.cb2.clear()
            self.cb2.addItems(["Enter format", " 5, 5, 5, 5", " 5, 5, 10", " 8, 6, 6", " 8, 8, 4", " 10, 10"])
            self.cb2.show()
            self.cb2Label.show()
            self.cb3.clear()
            self.cb3.addItems(["Enter format", " 5, 5, 5, 5", " 5, 5, 10", " 8, 6, 6", " 8, 8, 4", " 10, 10"])
            self.cb3.show()
            self.cb3Label.show()
            self.cb4.clear()
            self.cb4.addItems(["Enter format", " 5, 5, 5, 5", " 5, 5, 10", " 8, 6, 6", " 8, 8, 4", " 10, 10"])
            self.cb4.show()
            self.cb4Label.show()
            self.cb5.clear()
            self.cb5.addItems(["Enter format", " 5, 5, 5, 5", " 5, 5, 10", " 8, 6, 6", " 8, 8, 4", " 10, 10"])
            self.cb5.show()
            self.cb5Label.show()
            self.cb6.clear()
            self.cb6.addItems(["Enter format", " 5, 5, 5, 5", " 5, 5, 10", " 8, 6, 6", " 8, 8, 4", " 10, 10"])
            self.cb6.show()
            self.cb6Label.show()

    def generatePaper(self):
        if (self.fileEdit.text() != ""):
            self.printQuestion.q1 = self.q1
            self.printQuestion.q1marks = self.cb1.currentText()
            self.printQuestion.q2 = self.q2
            self.printQuestion.q3 = self.q3
            self.printQuestion.q4 = self.q4
            self.printQuestion.q5 = self.q5
            self.printQuestion.q6 = self.q6
            self.printQuestion.date = self.dateEdit.text()
            self.printQuestion.marks = self.marksCombo.currentText()
            self.printQuestion.sem = self.sem
            self.printQuestion.instructions = self.instructionEdit.toPlainText()
            self.printQuestion.time = self.timeEdit.text()
            self.printQuestion.exam = self.examEdit.text()
            self.printQuestion.fileName = self.fileEdit.text()
            self.printQuestion.printQuestions()

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = formattWindow()
    window.show()
    sys.exit(app.exec_())

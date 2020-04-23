import random
import sys

import mysql.connector

from Generate_paper import subSelect, format, printQuestion
from PyQt5 import QtWidgets, QtCore, QtGui

subject = ""
semester = ""

chapter = []
selectedModules = []


class moduleSelect(QtWidgets.QWidget):
    moduleList = QtCore.pyqtSignal(list)

    def __init__(self):
        super(moduleSelect, self).__init__()
        self.resize(1000, 700)
        self.subSelectWindow = subSelect.subSelectWindow()
        self.format = format.formattWindow()
        self.pQ = printQuestion.printQuestion()
        # BUTTONS

        self.subjectBtn = QtWidgets.QPushButton(self)
        self.subjectBtn.setGeometry(QtCore.QRect(330, 350, 350, 90))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.subjectBtn.setFont(font)
        self.subjectBtn.setStyleSheet("#subjectBtn{\n"
                                      "  outline: none;\n"
                                      "  color: #fff;\n"
                                      "  background-color:#66b3ff;\n"
                                      "  border: none;\n"
                                      "\n"
                                      "}")
        self.subjectBtn.setObjectName("subjectBtn")

        self.modulesBtn = QtWidgets.QPushButton(self)
        self.modulesBtn.setGeometry(QtCore.QRect(370, 600, 280, 65))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.modulesBtn.setFont(font)
        self.modulesBtn.setStyleSheet("#questionBtn{\n"
                                      "  outline: none;\n"
                                      "  color: #fff;\n"
                                      "  background-color:#47d147;\n"
                                      "  border: none;\n"
                                      "\n"
                                      "}")
        self.modulesBtn.setObjectName("questionBtn")
        self.modulesBtn.hide()

        # LABELS

        self.subjectLabel = QtWidgets.QLabel(self)
        self.subjectLabel.setGeometry(QtCore.QRect(160, 100, 691, 200))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(30)
        font.setBold(True)
        font.setWeight(75)
        self.subjectLabel.setFont(font)
        font.setWeight(60)
        font.setPointSize(12)
        self.subjectLabel.setStyleSheet("#subjectLabel{\n"
                                        "color :#4b4e4e;\n"
                                        "}")
        self.subjectLabel.setText("WELCOME!!!\n LET'S GET STARTED")
        self.subjectLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.subjectLabel.setObjectName("subjectLabel")

        # Module Checkbox
        self.chp1 = QtWidgets.QCheckBox(self)
        self.chp1.setGeometry(80, 150, 800, 60)
        self.chp1.setFont(font)
        self.chp1.hide()
        self.chp2 = QtWidgets.QCheckBox(self)
        self.chp2.setGeometry(80, 200, 800, 60)
        self.chp2.setFont(font)
        self.chp2.hide()
        self.chp3 = QtWidgets.QCheckBox(self)
        self.chp3.setGeometry(80, 250, 800, 60)
        self.chp3.setFont(font)
        self.chp3.hide()
        self.chp4 = QtWidgets.QCheckBox(self)
        self.chp4.setGeometry(80, 300, 800, 60)
        self.chp4.setFont(font)
        self.chp4.hide()
        self.chp5 = QtWidgets.QCheckBox(self)
        self.chp5.setGeometry(80, 350, 800, 60)
        self.chp5.setFont(font)
        self.chp5.hide()
        self.chp6 = QtWidgets.QCheckBox(self)
        self.chp6.setGeometry(80, 400, 600, 60)
        self.chp6.setFont(font)
        self.chp6.hide()
        self.chp7 = QtWidgets.QCheckBox(self)
        self.chp7.setGeometry(80, 450, 800, 60)
        self.chp7.setFont(font)
        self.chp7.hide()
        self.chp8 = QtWidgets.QCheckBox(self)
        self.chp8.setGeometry(80, 500, 800, 60)
        self.chp8.setFont(font)
        self.chp8.hide()

        self.subSelectWindow.semsub.connect(self.show_chapter)
        self.retranslateUi(self)
        self.subSelectWindow.semsub.connect(self.sendData)
        QtCore.QMetaObject.connectSlotsByName(self)
        self.subjectBtn.clicked.connect(self.select_subject)
        self.modulesBtn.clicked.connect(self.loadQuestions)

    def loadQuestions(self):

        global semester, subject
        selectedModules.clear()
        count = 0
        if self.chp1.isChecked():
            selectedModules.append(1)
            self.format.moduleList.append(1)
            count = count + 1
        if self.chp2.isChecked():
            selectedModules.append(2)
            self.format.moduleList.append(2)
            count = count + 1
        if self.chp3.isChecked():
            selectedModules.append(3)
            self.format.moduleList.append(3)
            count = count + 1
        if self.chp4.isChecked():
            selectedModules.append(4)
            self.format.moduleList.append(4)
            count = count + 1
        if self.chp5.isChecked():
            selectedModules.append(5)
            self.format.moduleList.append(5)
            count = count + 1
        if self.chp6.isChecked():
            selectedModules.append(6)
            self.format.moduleList.append(6)
            count = count + 1
        if self.chp7.isChecked():
            selectedModules.append(7)
            self.format.moduleList.append(7)
            count = count + 1
        if self.chp8.isChecked():
            selectedModules.append(8)
            self.format.moduleList.append(8)
            count = count + 1

        if count != 0:
            self.format.subject = subject
            self.format.semester = semester
            self.format.show()

    def retranslateUi(self, questionDialog):
        _translate = QtCore.QCoreApplication.translate
        questionDialog.setWindowTitle(_translate("questionDialog", "Select Modules"))
        self.subjectBtn.setText(_translate("questionDialog", "Click here to select subject"))
        self.modulesBtn.setText(_translate("questionDialog", "Proceed"))

    def select_subject(self):
        self.subSelectWindow.show()

    def sendData(self, sem, sub):
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.subjectLabel.setFont(font)
        self.subjectLabel.setGeometry(QtCore.QRect(250, 40, 691, 150))
        self.subjectLabel.setText(sub)
        global selectedModules
        global semester, subject

        self.format.sub = sub
        self.format.sem = sem
        semesterSwitcher = {
            " SEM I": "sem1",
            " SEM II": "sem2",
            " SEM III": "sem3",
            " SEM IV": "sem4",
            " SEM V": "sem5",
            " SEM VI": "sem6",
            " SEM VII": "sem7",
            " SEM VIII": "sem8"
        }
        subjectSwitcher = {
            " Applied Mathematics 1": "applied_mathematics1",
            " Applied Chemistry 1": "applied_chemistry1",
            " Applied Physics 1": "applied_physics1",
            " Basic Electrical and Electronic Engineering": "basic_electric_and_electronic_engineering",
            " Environmental Studies": "evs",
            # sem 2
            " Applied Mathematics 2" :"applied_mathematics2",
            " Applied Chemistry 2" : "applied_chemistry2",
            " Applied Physics 2": "applied_physics2",
            " Engineering Drawing": "engineering_drawing",
            " Structured Programming Approach":"structured_programming_approach",
            " Communication Skills":"	communication_skills",
            # sem3
            " Data Structure and Analysis":"data_structure_and_analysis",
            " Logic Design":"logic_design",
            " Principle of Communications": "principle_of_communication",
            " Database Managemnet System":"database_management_system",
            " Applied Mathematics 3":"	applied_mathematics3",

            # sem4
            " Automata Theory":"automata_theory",
            " Operating Systems":"operating_systems",
            " Computer Networks":"computer_networks",
            " Computer Organizations and Architecture":"computer_organization_and_architecture",
            " Applied Mathematics 4":"applied_mathematics4",

            # sem5
            " Microcontroller and Embedded Programming":"microcontroller",
            " Cryptography and Network Security":"cryptography_and_network_security",
            " Internet Programming":"internet_programming",
            " E-commerce and E-business":"ecom",
            " Advanced Data Management Technology":"microcontroller",

            # sem6
            " Software Engineering with\n Project Management":"software_engineering",
            " Data Mining and Business Intelligence":"data_mining",
            " Cloud Computing and Services":"cloud_computing",
            " Digital Forensics":"digital_forensic",
            " Wireless Networks":"wireless_networks",

            # sem7
            " Enterprise Network Design":"enterprise_network_design",
            " Infrastructure Security":"infrastructure_security",
            " Artificial Intelligence":"artificial_intelligence",
            " Software Testing and\n Quality Assurance":"software_testing",
            " Management Information System":"management_information_system",

            # sem8
            " Enterprise Resource Managenment":"enterprise_resource_management",
            " Big Data Analytics":"big_data_analytics",
            " Project Management":"project_management",
            " Internet Of Everything":"internet_of_everyting"

        }
        semester = semesterSwitcher.get(sem)
        subject = subjectSwitcher.get(sub)

    def show_chapter(self, semester, subject):
        self.subjectLabel.setText(subject)
        global chapter
        if (subject == " Applied Mathematics 1"):
            chapter = [" Complex Numbers", " Logarithm of Complex Numbers", " Succesive Differentiation", " Matrices",
                       " Partial Differentiation", " Application of Partial Differentiation", " Expansion of Functions"]
        elif (subject == " Applied Physics 1"):
            chapter = [" Crystal Structure", " Quantum Mechanics", " Semiconductor Physics", " Superconductivity",
                       " Acoustics", " Ultrasonic"]
        elif (subject == " Applied Chemistry 1"):
            chapter = ["Water", "Polymers", "Lubricants", "Phase Rule", "Important Engineering materials"]
        elif (subject == " Basic Electrical and Electronic Engineering"):
            chapter = ["DC Circuits(Only Independent Sources)", "Three Phase Circuits", "Lubricants",
                       "Single Phase Transformer", "DC Machines"]
        elif (subject == " Environmental Studies"):
            chapter = ["Overview of Environmental Aspects",
                       "Aspects of Sustainable Development",
                       "Types of Pollution",
                       "Pollution Control Legislation",
                       "Renewable sources of Energy",
                       "Technological Advances to overcome"]
        elif (subject == " Applied Mathematics 2"):
            chapter = ["Differential Equations of First Order ",
                       "Linear Differential Equations With Constant Coefficients and Variable Coefficients.....",
                       "Numerical Solution of Ordinary Differential Equations of First Order And First order...",
                       "Differentiation under Integral Sign, Numerical Integration and Rectification",
                       "Double Integration",
                       "Triple Integration and Application of Multiple Integrals"]
        elif (subject == " Applied Chemistry 2"):
            chapter = ["Corrosion",
                       "Alloys",
                       "Fuels",
                       "Composite Materials",
                       "Green Chemistry"]
        elif (subject == " Applied Physics 2"):
            chapter = ["Interference and Diffraction of Light",
                       "Laser",
                       "Fibre Optics",
                       "Electrodynamics",
                       "Charged Particles in Electric and Magnetic Fields",
                       "Nano Science"]
        elif (subject == " Structured Programming Approach"):
            chapter = ["Introduction to Computer, Algorithm and Flowchart",
                       "Fundamental of C Programming",
                       "Control Structures",
                       "Functions and Parameter",
                       "Arrays, String, Structures and Union",
                       "Pointers and Files"]
        elif (subject == " Communication Skills"):
            chapter = ["Communication Theory",
                       "Grammar and Vocabulary",
                       "Business Correspondence",
                       "Summarization and Comprehension",
                       "Technical Writing"]
        elif (subject == " Data Structure and Analysis"):
            chapter = ["Introduction to Data Structures and Analysis",
                       "Stacks",
                       "Queues",
                       "Linked List",
                       "Sorting And Searching",
                       "Trees And Graphs"]
        elif (subject == " Logic Design"):
            chapter = ["Biasing of BJT",
                       "Number System & Codes",
                       "Boolean Algebra and Logic Gates",
                       "Design and Analysis of Combinational Circuits",
                       "Sequential Logic Design",
                       "VHDL"]
        elif (subject == " Principle of Communications"):
            chapter = ["Introduction",
                       "Fourier Transform and Noise",
                       "Modulation and Demodulation (AM and FM),",
                       "Pulse Analog Modulation",
                       "Digital Modulation Techniques and Transmission",
                       "Radiation and Propagation of Waves"]
        elif (subject == " Database Managemnet System"):
            chapter = ["Introduction to Database Concepts",
                       "Entity - Relationship Data Model",
                       "Relational Model and Relational Algebra",
                       "Structured Query Language - SQL",
                       "Relational Database Design",
                       "Storage and Indexing"]
        elif (subject == " Applied Mathematics 3"):
            chapter = ["Laplace Transform",
                       "Inverse Laplace Transform",
                       "Fourier series",
                       "Vector Algebra and Vector Differentiation",
                       "Vector Integral",
                       "Complex Variable and Bessel Functionss"]
        elif (subject == " Automata Theory"):
            chapter = ["Introduction and Finite Automata",
                       "Regular Expressions",
                       "Context Free Grammars and Languages",
                       "Push Down Automata",
                       "Turing Theory",
                       "Undecidability and Recursively enumerable languages"]
        elif (subject == " Operating Systems"):
            chapter = ["Overview of Operating System",
                       "Process Management",
                       "Process coordination",
                       "Memory Management",
                       "Storage Management",
                       "Distributed Systems"]
        elif (subject == " Computer Networks"):
            chapter = ["Introduction",
                       "Application Layer",
                       "Session Layer",
                       "Network Layer",
                       "Data Link Layer",
                       "Physical Layer"]
        elif (subject == " Computer Organizations and Architecture"):
            chapter = ["Overview of Computer Architecture and Organization",
                       "Programming 8086",
                       "Process Organization",
                       "Data Representation and Arithemic Algorithms",
                       "Memory Organization",
                       "I/O Organization"]
        elif (subject == " Applied Mathematics 4"):
            chapter = ["Elements of Number Theory I",
                       "Elements of Number Theory II",
                       "Probability",
                       "Sampling theory",
                       "Graph"]
        elif (subject == " Microcontroller and Embedded Programming"):
            chapter = ["Introduction to Embedded System",
                       "The Microcontroller Architecture and Programming of 8051",
                       "Interfacing with 8051 Microcontroller",
                       "ARM 7 Architecture",
                       "Open source RTOS",
                       "Introduction to Embedded target boards"]
        elif (subject == " Cryptography and Network Security"):
            chapter = ["Cryptography and Network Security",
                       "Microntroller and Embedded Programming",
                       "Internet Programming",
                       "Advanced Database Management Systems",
                       "E-commerce and E-business"]
        elif (subject == " Internet Programming"):
            chapter = ["Client Side Programming: HTML, CSS and JavaScript",
                       "HTML 5 and Responsive Web Design with CSS 3",
                       "Rich Internet Application (RIA)",
                       "Server Side Programming: PHP",
                       "Web Extensions and Web Services",
                       "Python Web Framework: Django"]
        elif (subject == " E-commerce and E-business"):
            chapter = ["Introduction to e-commerce",
                       "Overview of hardware and software technologies for e-commerce",
                       "Payment System for e-commerce",
                       "E-Marketing Strategies",
                       "E-Business: Introduction to e business",
                       "Developing e-business models",
                       "E-business strategies",
                       "Design and development of an business website"]
        elif (subject == " Advanced Data Management Technology"):
            chapter = ["Query Processing and Optimization",
                       "Transactions Management and Concurrency",
                       "Advanced Data Management techniques",
                       "Distributed Databases",
                       "Data Warehousing, Dimensional Modeling and OLAP",
                       "ETL Process"]
        elif (subject == " Software Engineering with Project Management"):
            chapter = ["An overview of IT project Management",
                       "Project Integration Management",
                       "Project Scope Management",
                       "Project Time Management",
                       "Project Cost Management",
                       "Project Quality Management",
                       "Project Human Resource Management",
                       "Project Communication Management"]
        elif (subject == " Data Mining and Business Intelligence"):
            chapter = ["Introduction to Data Mining",
                       "Data Exploration and Data Pre-processing",
                       "Classification",
                       "Clustering",
                       "Frequent Pattern Mining Business Intelligence",
                       "Business Intelligence"]
        elif (subject == " Cloud Computing and Services"):
            chapter = [ "Introduction",
                        "Virtualization",
                        "Cloud Computing Services",
                        "Cloud Implementation, Programming and Mobile Cloud Computing",
                        "Exploring the Components of Amazon Web Services",
                        "I Cloud Backup & Solutions "]
        elif (subject == " Wireless Networks"):
            chapter = ["Fundamentals Wireless Communication",
                       "Evolution of Wireless Technologies",
                       "Types of Wireless Networks",
                       "Emerging Wireless Technologies and standards",
                       "Wireless Network Design Considerations",
                       "Wireless Network Security"]
        elif (subject == " Digital Forensics"):
            chapter = [ "Introduction to Cyber Crime and Ethical Hacking",
                        "Introduction to Digital Forensics and Digital Evidences",
                        "Computer Security Incident Response Methodology",
                        "Forensic Duplication and Disk Analysis, and Investigation",
                        "Network Forensics",
                        "Forensic Investigation"]
        elif (subject == " Enterprise Network Design"):
            chapter = [ "Applying a Methodology to Network Design",
                        "Structuring and Modularizing the Network",
                        "Designing Basic Campus and Data Center Networks",
                        "Designing Remote Connectivity",
                        "Designing IP Addressing in the Network & Selecting Routing Protocols",
                        "Software Defined Network"]
        elif (subject == " Infrastructure Security"):
            chapter = ["Introduction",
                       "Software Security",
                       "Wireless Security",
                       "CLoud Security",
                       "Web Security",
                       "Information Security and Risk Management"]
        elif (subject == " Artificial Intelligence"):
            chapter =[ "Introduction to Intelligent Systems and Intelligent Agents",
                       "Search Techniques ",
                       "Knowledge and Reasoning",
                       "Planning",
                       "Uncertain Knowledge and Reasoning",
                       "Natural Language"]
        elif (subject == " Software Testing and\n Quality Assurance"):
            chapter =["Testing Methodology",
                      "Testing Techniques",
                      "Managing the Test Process",
                      "Test Automation",
                      "Testing for specialized environment",
                      "Quality Management"]
        elif (subject == " Management Information System"):
            chapter =[ "Introduction To Information Systems",
                       "Data and Knowledge Management",
                       "Ethical issues and Privacy",
                       "Social Computing (SC)",
                       "Computer Networks Wired and Wireless technology",
                       "Information System within Organization"
                       ]
        elif (subject == " Enterprise Resource Managenment"):
            chapter =[ "Introduction to ERP",
                       "ERP Technologies",
                       "ERP Manufacturing Perspective and ERP Modules",
                       "Benefits of ERP",
                       "ERP Life cycle",
                       "E-Commerce to Ebusiness"]
        elif (subject == " Big Data Analytics"):
            chapter =[   "Introduction to Big Data",
                         "Introduction to Big Data Frameworks",
                         "MapReduce Paradigm",
                         "Mining Big Data Streams",
                         "V Big Data Mining Algorithms",
                         "Big Data Analytics Applications"]
        elif (subject == " Project Management"):
            chapter =["Project Management Foundation",
                      "Initiating Projects",
                      "Project Planning and Scheduling",
                      "Planning Projects",
                      "5.1 Executing Projects"]
        elif (subject == " Internet Of Everything"):
            chapter =[  "Introduction",
                        "RFID Technology",
                        "RFID Applications",
                        "Wireless Sensor Networks",
                        "Mobility and Settings",
                        "Data Analytics for IoE"]
        self.subjectBtn.setText("Change Subject")
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.subjectBtn.setFont(font)
        self.subjectBtn.setGeometry(QtCore.QRect(30, 50, 241, 51))
        self.modulesBtn.show()
        self.chp1.setText(chapter[0])
        self.chp1.show()
        self.chp1.setChecked(False)
        self.chp2.setText(chapter[1])
        self.chp2.show()
        self.chp2.setChecked(False)
        self.chp3.setText(chapter[2])
        self.chp3.show()
        self.chp3.setChecked(False)
        self.chp4.setText(chapter[3])
        self.chp4.show()
        self.chp4.setChecked(False)
        self.chp5.setText(chapter[4])
        self.chp5.show()
        self.chp5.setChecked(False)
        if (len(chapter) > 5):
            self.chp6.setText(chapter[5])
            self.chp6.show()
            self.chp6.setChecked(False)
        if (len(chapter) > 6):
            self.chp7.setText(chapter[6])
            self.chp7.show()
            self.chp7.setChecked(False)
        if (len(chapter) > 7):
            self.chp8.setText(chapter[7])
            self.chp8.show()
            self.chp8.setChecked(False)
            self.chp8.setChecked(False)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = moduleSelect()
    window.show()
    sys.exit(app.exec_())
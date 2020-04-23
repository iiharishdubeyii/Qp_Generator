import sys

import mysql.connector

from Add_questions  import subSelect
from PyQt5 import QtWidgets, QtCore, QtGui

subject = ""
semester = ""


class MyWindow(QtWidgets.QWidget):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.resize(1000, 700)
        self.subSelectWindow = subSelect.subSelectWindow()

        # TEXTBOXES
        self.questionEdit = QtWidgets.QPlainTextEdit(self)
        self.questionEdit.setGeometry(QtCore.QRect(300, 225, 591, 120))
        self.questionEdit.setObjectName("questionEdit")
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        font.setWeight(60)
        self.questionEdit.setFont(font)

        self.weightageEdit = QtWidgets.QLineEdit(self)
        self.weightageEdit.setGeometry(QtCore.QRect(300, 430, 300, 50))
        self.weightageEdit.setObjectName("weightageEdit")
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        font.setWeight(60)
        self.weightageEdit.setFont(font)

        self.repeatEdit = QtWidgets.QLineEdit(self)
        self.repeatEdit.setGeometry(QtCore.QRect(300, 500, 300, 50))
        self.repeatEdit.setObjectName("repeatEdit")
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        font.setWeight(60)
        self.repeatEdit.setFont(font)

        # COMBO BOXES
        self.chapterCombo = QtWidgets.QComboBox(self)
        self.chapterCombo.setGeometry(QtCore.QRect(300, 160, 591, 45))
        self.chapterCombo.setCurrentText("")
        self.chapterCombo.setObjectName("chapterCombo")
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        font.setWeight(60)
        self.chapterCombo.setFont(font)

        self.typeCombo = QtWidgets.QComboBox(self)
        self.typeCombo.setGeometry(QtCore.QRect(300, 365, 300, 45))
        self.typeCombo.setObjectName("typeCombo")
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        font.setWeight(60)
        self.typeCombo.setFont(font)
        self.typeCombo.addItems(["Theory", "Numerical"])

        # BUTTONS
        self.questionBtn = QtWidgets.QPushButton(self)
        self.questionBtn.setGeometry(QtCore.QRect(370, 600, 260, 61))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.questionBtn.setFont(font)
        self.questionBtn.setStyleSheet("#questionBtn{\n"
                                       "  outline: none;\n"
                                       "  color: #fff;\n"
                                       "  background-color:#47d147;\n"
                                       "  border: none;\n"
                                       "\n"
                                       "}")
        self.questionBtn.setObjectName("questionBtn")

        self.subjectBtn = QtWidgets.QPushButton(self)
        self.subjectBtn.setGeometry(QtCore.QRect(30, 50, 241, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
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

        # LABELS

        self.subjectLabel = QtWidgets.QLabel(self)
        self.subjectLabel.setGeometry(QtCore.QRect(270, 20, 691, 61))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.subjectLabel.setFont(font)
        self.subjectLabel.setStyleSheet("#subjectLabel{\n"
                                        "color :#4b4e4e;\n"
                                        "}")
        self.subjectLabel.setText("")
        self.subjectLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.subjectLabel.setObjectName("subjectLabel")

        self.chapterLabel = QtWidgets.QLabel(self)
        self.chapterLabel.setGeometry(QtCore.QRect(120, 160, 170, 40))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.chapterLabel.setFont(font)
        self.chapterLabel.setStyleSheet("")
        self.chapterLabel.setObjectName("chapterLabel")

        self.questionLabel = QtWidgets.QLabel(self)
        self.questionLabel.setGeometry(QtCore.QRect(120, 225, 170, 40))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.questionLabel.setFont(font)
        self.questionLabel.setStyleSheet("")
        self.questionLabel.setObjectName("questionLabel")

        self.typeLabel = QtWidgets.QLabel(self)
        self.typeLabel.setGeometry(QtCore.QRect(120, 365, 170, 40))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.typeLabel.setFont(font)
        self.typeLabel.setStyleSheet("")
        self.typeLabel.setObjectName("typeLabel")

        self.weightageLabel = QtWidgets.QLabel(self)
        self.weightageLabel.setGeometry(QtCore.QRect(120, 430, 170, 40))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.weightageLabel.setFont(font)
        self.weightageLabel.setStyleSheet("")
        self.weightageLabel.setObjectName("weightageLabel")

        self.repeatLabel = QtWidgets.QLabel(self)
        self.repeatLabel.setGeometry(QtCore.QRect(120, 500, 170, 40))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.repeatLabel.setFont(font)
        self.repeatLabel.setStyleSheet("")
        self.repeatLabel.setObjectName("repeatLabel")

        self.verifyLabel = QtWidgets.QLabel(self)
        self.verifyLabel.setGeometry(QtCore.QRect(300, 120, 500, 40))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.verifyLabel.setFont(font)
        self.verifyLabel.setStyleSheet("")
        self.verifyLabel.setObjectName("verifyLabel")
        self.verifyLabel.setStyleSheet("#verifyLabel{\n"
                                       "  color: red;\n"
                                       "}")

        self.subSelectWindow.semsub.connect(self.show_chapter)
        self.retranslateUi(self)

        self.questionBtn.clicked.connect(self.saveToDatabase)
        self.subSelectWindow.semsub.connect(self.sendData)

        QtCore.QMetaObject.connectSlotsByName(self)
        print(self.subjectLabel.text())
        self.subjectBtn.clicked.connect(self.select_subject)

    def retranslateUi(self, questionDialog):
        _translate = QtCore.QCoreApplication.translate
        questionDialog.setWindowTitle(_translate("questionDialog", "Dialog"))
        self.questionBtn.setText(_translate("questionDialog", "ADD QUESTION"))
        self.subjectBtn.setText(_translate("questionDialog", "Click here to select subject"))
        self.chapterLabel.setText(_translate("questionDialog", "Chapter :"))
        self.questionLabel.setText(_translate("questionDialog", "Question :"))
        self.typeLabel.setText(_translate("questionDialog", "Type :"))
        self.weightageLabel.setText(_translate("questionDialog", "Weightage :"))
        self.repeatLabel.setText(_translate("questionDialog", "Repeated :"))

    def saveToDatabase(self):
        global semester, subject
        chapter = self.chapterCombo.currentIndex()
        chapter += 1
        chapter = str(chapter)
        question = self.questionEdit.toPlainText()
        typ = self.typeCombo.currentText()
        repeat = self.repeatEdit.text()
        weightage = self.weightageEdit.text()
        if (question != "" and weightage != "" and repeat != ""):
            if (weightage.isnumeric()):
                if (0 < int(weightage) < 11):
                    conn = mysql.connector.connect(host="localhost", database=semester, user="root", password="")
                    cur = conn.cursor()
                    query = "INSERT INTO " + subject + " (question,weightage,type,chapter,occurance) VALUES('" + question + "','" + weightage + "', '" + typ + "','" + chapter + "','" + repeat + "')"
                    cur.execute(query)
                    conn.commit()
                    conn.close()
                    print("Saved")
                    self.verifyLabel.setText("Successfully saved to Database")
                    self.verifyLabel.setStyleSheet("#verifyLabel{\n"
                                                   "  color: green;\n"
                                                   "}")
                    self.weightageEdit.clear()
                    self.typeCombo.clear()
                    self.questionEdit.clear()
                else:
                    self.verifyLabel.setText("Value of weightage must be between 1 to 10")
            else:
                self.verifyLabel.setText("Weightage field must contain all numeric ")
        else:
            self.verifyLabel.setText("Fill all the fields")

    def select_subject(self):
        self.subSelectWindow.show()

    def sendData(self, sem, sub):
        global semester
        global subject

        self.subjectLabel.setText(sub)
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
        if (subject == " Applied Mathematics 1"):
            self.chapterCombo.clear()
            self.chapterCombo.addItems(
                [" Complex Numbers", " Logarithm of Complex Numbers", " Succesive Differentiation", " Matrices",
                 " Partial Differentiation", " Application of Partial Differentiation", " Expansion of Functions"])
        elif (subject == " Applied Physics 1"):
            self.chapterCombo.clear()
            self.chapterCombo.addItems(
                [" Crystal Structure", " Quantum Mechanics", " Semiconductor Physics", " Superconductivity",
                 " Acoustics", " Ultrasonic"])
        elif (subject == " Applied Chemistry 1"):
            self.chapterCombo.clear()
            self.chapterCombo.addItems(
                [" Water", " Polymers", " Lubricants", " Phase Rule", " Important Engineering materials"])
        elif (subject == " Basic Electrical and Electronic Engineering"):
            self.chapterCombo.clear()
            self.chapterCombo.addItems(
                [" DC Circuits(Only Independent Sources)", " Three Phase Circuits", " Lubricants",
                 " Single Phase Transformer", " DC Machines"])
        elif (subject == " Environmental Studies"):
            self.chapterCombo.clear()
            self.chapterCombo.addItems(
                [" Overview of Environmental Aspects", " Aspects of Sustainable Development", " Types of Pollution",
                 " Pollution Control Legislation", " Renewable sources of Energy",
                 " Technological Advances to overcome"])
        elif (subject == " Applied Mathematics 2"):
            self.chapterCombo.clear()
            self.chapterCombo.addItems(["Differential Equations of First Order ",
                       "Linear Differential Equations With Constant Coefficients and Variable Coefficients.....",
                       "Numerical Solution of Ordinary Differential Equations of First Order And First order...",
                       "Differentiation under Integral Sign, Numerical Integration and Rectification",
                       "Double Integration",
                       "Triple Integration and Application of Multiple Integrals"])
        elif (subject == " Applied Chemistry 2"):
            self.chapterCombo.clear()
            self.chapterCombo.addItems(["Corrosion",
                       "Alloys",
                       "Fuels",
                       "Composite Materials",
                       "Green Chemistry"])
        elif (subject == " Applied Physics 2"):
            self.chapterCombo.clear()
            self.chapterCombo.addItems(["Interference and Diffraction of Light",
                       "Laser",
                       "Fibre Optics",
                       "Electrodynamics",
                       "Charged Particles in Electric and Magnetic Fields",
                       "Nano Science"])
        elif (subject == " Structured Programming Approach"):
            self.chapterCombo.clear()
            self.chapterCombo.addItems( ["Introduction to Computer, Algorithm and Flowchart",
                       "Fundamental of C Programming",
                       "Control Structures",
                       "Functions and Parameter",
                       "Arrays, String, Structures and Union",
                       "Pointers and Files"])
        elif (subject == " Communication Skills"):
            self.chapterCombo.clear()
            self.chapterCombo.addItems(["Communication Theory",
                       "Grammar and Vocabulary",
                       "Business Correspondence",
                       "Summarization and Comprehension",
                       "Technical Writing"])
        elif (subject == " Data Structure and Analysis"):
            self.chapterCombo.clear()
            self.chapterCombo.addItems( ["Introduction to Data Structures and Analysis",
                       "Stacks",
                       "Queues",
                       "Linked List",
                       "Sorting And Searching",
                       "Trees And Graphs"])
        elif (subject == " Logic Design"):
            self.chapterCombo.clear()
            self.chapterCombo.addItems(["Biasing of BJT",
                       "Number System & Codes",
                       "Boolean Algebra and Logic Gates",
                       "Design and Analysis of Combinational Circuits",
                       "Sequential Logic Design",
                       "VHDL"])
        elif (subject == " Principle of Communications"):
            self.chapterCombo.clear()
            self.chapterCombo.addItems( ["Introduction",
                       "Fourier Transform and Noise",
                       "Modulation and Demodulation (AM and FM),",
                       "Pulse Analog Modulation",
                       "Digital Modulation Techniques and Transmission",
                       "Radiation and Propagation of Waves"])
        elif (subject == " Database Managemnet System"):
            self.chapterCombo.clear()
            self.chapterCombo.addItems(["Introduction to Database Concepts",
                       "Entity - Relationship Data Model",
                       "Relational Model and Relational Algebra",
                       "Structured Query Language - SQL",
                       "Relational Database Design",
                       "Storage and Indexing"])
        elif (subject == " Applied Mathematics 3"):
            self.chapterCombo.clear()
            self.chapterCombo.addItems( ["Laplace Transform",
                       "Inverse Laplace Transform",
                       "Fourier series",
                       "Vector Algebra and Vector Differentiation",
                       "Vector Integral",
                       "Complex Variable and Bessel Functionss"])
        elif (subject == " Automata Theory"):
            self.chapterCombo.clear()
            self.chapterCombo.addItems( ["Introduction and Finite Automata",
                       "Regular Expressions",
                       "Context Free Grammars and Languages",
                       "Push Down Automata",
                       "Turing Theory",
                       "Undecidability and Recursively enumerable languages"])
        elif (subject == " Operating Systems"):
            self.chapterCombo.clear()
            self.chapterCombo.addItems( ["Overview of Operating System",
                       "Process Management",
                       "Process coordination",
                       "Memory Management",
                       "Storage Management",
                       "Distributed Systems"])
        elif (subject == " Computer Networks"):
            self.chapterCombo.clear()
            self.chapterCombo.addItems(["Introduction",
                       "Application Layer",
                       "Session Layer",
                       "Network Layer",
                       "Data Link Layer",
                       "Physical Layer"])
        elif (subject == " Computer Organizations and Architecture"):
            self.chapterCombo.clear()
            self.chapterCombo.addItems(["Overview of Computer Architecture and Organization",
                       "Programming 8086",
                       "Process Organization",
                       "Data Representation and Arithemic Algorithms",
                       "Memory Organization",
                       "I/O Organization"])
        elif (subject == " Applied Mathematics 4"):
            self.chapterCombo.clear()
            self.chapterCombo.addItems(["Elements of Number Theory I",
                       "Elements of Number Theory II",
                       "Probability",
                       "Sampling theory",
                       "Graph"])
        elif (subject == " Microcontroller and Embedded Programming"):
            self.chapterCombo.clear()
            self.chapterCombo.addItems(["Introduction to Embedded System",
                       "The Microcontroller Architecture and Programming of 8051",
                       "Interfacing with 8051 Microcontroller",
                       "ARM 7 Architecture",
                       "Open source RTOS",
                       "Introduction to Embedded target boards"])
        elif (subject == " Cryptography and Network Security"):
            self.chapterCombo.clear()
            self.chapterCombo.addItems(["Cryptography and Network Security",
                       "Microntroller and Embedded Programming",
                       "Internet Programming",
                       "Advanced Database Management Systems",
                       "E-commerce and E-business"])
        elif (subject == " Internet Programming"):
            self.chapterCombo.clear()
            self.chapterCombo.addItems(["Client Side Programming: HTML, CSS and JavaScript",
                       "HTML 5 and Responsive Web Design with CSS 3",
                       "Rich Internet Application (RIA)",
                       "Server Side Programming: PHP",
                       "Web Extensions and Web Services",
                       "Python Web Framework: Django"])
        elif (subject == " E-commerce and E-business"):
            self.chapterCombo.clear()
            self.chapterCombo.addItems(["Introduction to e-commerce",
                       "Overview of hardware and software technologies for e-commerce",
                       "Payment System for e-commerce",
                       "E-Marketing Strategies",
                       "E-Business: Introduction to e business",
                       "Developing e-business models",
                       "E-business strategies",
                       "Design and development of an business website"])
        # elif (subject == " Advanced Data Management Technology"):

        elif (subject == " Advanced Data Management Technology"):
            self.chapterCombo.clear()
            self.chapterCombo.addItems(["Query Processing and Optimization",
                        "Transactions Management and Concurrency",
                        "Advanced Data Management techniques",
                        "Distributed Databases",
                        "Data Warehousing, Dimensional Modeling and OLAP",
                        "ETL Process"
            ])
        elif (subject == " Software Engineering with\n Project Management"):
            self.chapterCombo.clear()
            self.chapterCombo.addItems(["An overview of IT project Management",
                       "Project Integration Management",
                       "Project Scope Management",
                       "Project Time Management",
                       "Project Cost Management",
                       "Project Quality Management",
                       "Project Human Resource Management",
                       "Project Communication Management"])
        elif (subject == " Data Mining and Business Intelligence"):
            self.chapterCombo.clear()
            self.chapterCombo.addItems(["Introduction to Data Mining",
                       "Data Exploration and Data Pre-processing",
                       "Classification",
                       "Clustering",
                       "Frequent Pattern Mining Business Intelligence",
                       "Business Intelligence"])
        elif (subject == " Cloud Computing and Services"):
            self.chapterCombo.clear()
            self.chapterCombo.addItems([
                "Introduction",
                "Virtualization",
                "Cloud Computing Services",
                "Cloud Implementation, Programming and Mobile Cloud Computing",
                "Exploring the Components of Amazon Web Services",
                "I Cloud Backup & Solutions "
            ])
        elif (subject == " Wireless Networks"):
            self.chapterCombo.clear()
            self.chapterCombo.addItems([
                "Fundamentals Wireless Communication",
                "Evolution of Wireless Technologies",
                "Types of Wireless Networks",
                "Emerging Wireless Technologies and standards",
                "Wireless Network Design Considerations",
                "Wireless Network Security"
            ])
        elif (subject == " Digital Forensics"):
            self.chapterCombo.clear()
            self.chapterCombo.addItems([
                "Introduction to Cyber Crime and Ethical Hacking",
                "Introduction to Digital Forensics and Digital Evidences",
                "Computer Security Incident Response Methodology",
                "Forensic Duplication and Disk Analysis, and Investigation",
                "Network Forensics",
                "Forensic Investigation"
            ])
        elif (subject == " Enterprise Network Design"):
            self.chapterCombo.clear()
            self.chapterCombo.addItems([
                "Applying a Methodology to Network Design",
                "Structuring and Modularizing the Network",
                "Designing Basic Campus and Data Center Networks",
                "Designing Remote Connectivity",
                "Designing IP Addressing in the Network & Selecting Routing Protocols",
                "Software Defined Network"
            ])
        elif (subject == " Infrastructure Security"):
            self.chapterCombo.clear()
            self.chapterCombo.addItems([
                "Introduction",
                "Software Security",
                "Wireless Security",
                "CLoud Security",
                "Web Security",
                "Information Security and Risk Management"

            ])
        elif (subject == " Artificial Intelligence"):
            self.chapterCombo.clear()
            self.chapterCombo.addItems([
                "Introduction to Intelligent Systems and Intelligent Agents",
                "Search Techniques ",
                "Knowledge and Reasoning",
                "Planning",
                "Uncertain Knowledge and Reasoning",
                "Natural Language"
            ])
        elif (subject == " Software Testing and\n Quality Assurance"):
            self.chapterCombo.clear()
            self.chapterCombo.addItems([
                "Testing Methodology",
                "Testing Techniques",
                "Managing the Test Process",
                "Test Automation",
                "Testing for specialized environment",
                "Quality Management"

            ])
        elif (subject == " Management Information System"):
            self.chapterCombo.clear()
            self.chapterCombo.addItems([
                "Introduction To Information Systems",
                "Data and Knowledge Management",
                "Ethical issues and Privacy",
                "Social Computing (SC)",
                "Computer Networks Wired and Wireless technology",
                "Information System within Organization"

            ])
        elif (subject == " Enterprise Resource Managenment"):
            self.chapterCombo.clear()
            self.chapterCombo.addItems([
                "Introduction to ERP",
                "ERP Technologies",
                "ERP Manufacturing Perspective and ERP Modules",
                "Benefits of ERP",
                "ERP Life cycle",
                "E-Commerce to Ebusiness"

            ])
        elif (subject == " Big Data Analytics"):
            self.chapterCombo.clear()
            self.chapterCombo.addItems([
                "Introduction to Big Data",
                "Introduction to Big Data Frameworks",
                "MapReduce Paradigm",
                "Mining Big Data Streams",
                "V Big Data Mining Algorithms",
                "Big Data Analytics Applications"
            ])
        elif (subject == " Project Management"):
            self.chapterCombo.clear()
            self.chapterCombo.addItems([
                "Project Management Foundation",
                "Initiating Projects",
                "Project Planning and Scheduling",
                "Planning Projects",
                "5.1 Executing Projects"
            ])
        elif (subject == " Internet Of Everything"):
            self.chapterCombo.clear()
            self.chapterCombo.addItems([
                "Introduction",
                "RFID Technology",
                "RFID Applications",
                "Wireless Sensor Networks",
                "Mobility and Settings",
                "Data Analytics for IoE"
            ])



if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())
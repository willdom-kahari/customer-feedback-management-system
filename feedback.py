from PyQt5.QtWidgets import QMainWindow, QMessageBox, QLineEdit,QLabel, QCheckBox, QPushButton, QTextEdit
from PyQt5 import uic,QtWidgets, QtCore, QtGui
from resource import resources
import sys
import os
import csv



class WriteData:

    def __init__(self, data:dict):
        self.data = data



    def write_to_csv(self):

        try:

            with open("customer_feedback.csv", "w", newline="") as file:
                writer = csv.writer(file)
                writer.writerow(["Name", "Rating", "Feedback"])

                for name in self.data['name']:
                    position = self.data['name'].index(name)
                    writer.writerow([name, self.data['rating'][position], self.data['comment'][position]])
            return True
        
        except Exception as error:

            return error
                
            


class FeedBackApp(QMainWindow):
    
    
    def __init__(self):
        super().__init__()
        # Load the UI file
        uic.loadUi('resource/ui/main.ui', self)
        
        self.closebtn = self.findChild(QPushButton, "close")
        self.min = self.findChild(QPushButton, "min")
        self.restor = self.findChild(QPushButton, "restor")
        self.comment = self.findChild(QTextEdit, "comment")
        self.send = self.findChild(QPushButton, "send")
        self.name = self.findChild(QLineEdit, "name")
        self.star1 = self.findChild(QCheckBox, "star1")
        self.star2 = self.findChild(QCheckBox, "star2")
        self.star3 = self.findChild(QCheckBox, "star3")
        self.star4 = self.findChild(QCheckBox, "star4")
        self.star5 = self.findChild(QCheckBox, "star5")
        self.customer_names = []
        self.customer_ratings = []
        self.customer_feedback = []

        self.star1.stateChanged.connect(self.star_1)
        self.star2.stateChanged.connect(self.star_2)
        self.star3.stateChanged.connect(self.star_3)
        self.star4.stateChanged.connect(self.star_4)
        self.star5.stateChanged.connect(self.star_5)
        self.send.clicked.connect(self.grab_feedback)
        self.min.clicked.connect(self.minimiz_application)
        self.restor.clicked.connect(self.full_screen)
        self.closebtn.clicked.connect(self.close_application
                                             )
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        self.full_screen_mod = False
        self.star_count = 0
        self.count = 1
        # Variables for dragging
        self.dragging = False
        self.startPos = None

    def mousePressEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton:
            self.dragging = True
            self.startPos = event.globalPos() - self.frameGeometry().topLeft()
            event.accept()

    def mouseMoveEvent(self, event):
        if self.dragging:
            self.move(event.globalPos() - self.startPos)
            event.accept()



    def star_1(self, state):

        if state == 2:
           self.star1.setChecked(True)
           self.star_count = 1
        else:
            self.star1.setChecked(False)

    def star_2(self, state):

        if state == 2:
            self.star1.setChecked(True)
            self.star2.setChecked(True)
            self.star_count = 2
        else:
            self.star1.setChecked(False)
            self.star2.setChecked(False)
            self.star_count -= 2

    def star_3(self, state):

        if state == 2:
            self.star1.setChecked(True)
            self.star2.setChecked(True)
            self.star3.setChecked(True)
            self.star_count = 3
        else:
            self.star1.setChecked(False)
            self.star2.setChecked(False)
            self.star3.setChecked(False)
            self.star_count -= 3

    def star_4(self, state):

        if state == 2:
            self.star1.setChecked(True)
            self.star2.setChecked(True)
            self.star3.setChecked(True)
            self.star4.setChecked(True)
            self.star_count = 4
        else:
            self.star1.setChecked(False)
            self.star2.setChecked(False)
            self.star3.setChecked(False)
            self.star4.setChecked(False)
            self.star_count -= 4

    def star_5(self, state):

        print(state)
        if state == 2:
            self.star1.setChecked(True)
            self.star2.setChecked(True)
            self.star3.setChecked(True)
            self.star4.setChecked(True)
            self.star5.setChecked(True)
            self.star_count = 5
        else:
            self.star1.setChecked(False)
            self.star2.setChecked(False)
            self.star3.setChecked(False)
            self.star4.setChecked(False)
            self.star5.setChecked(False)
            self.star_count -= 5




    def close_application(self):

        QtWidgets.QApplication.quit()

    def minimiz_application(self):

        self.showMinimized()

    def full_screen(self):

        if not self.full_screen_mod:
            self.showFullScreen()
            self.full_screen_mod = True
        else:
            self.showNormal()
            self.full_screen_mod = False


    def grab_feedback(self):

        # Add the collected input to the declared lists
        if self.count <= 5:
            self.customer_names.append(self.name.text()),
            self.customer_ratings.append(self.star_count),
            self.customer_feedback.append(self.comment.toPlainText())
            self.count += 1
        else:

            data = {
            "name":self.customer_names,
            "rating":self.customer_ratings,
            "comment":self.customer_feedback
            }

            writer = WriteData(data).write_to_csv()
            if writer:

                print("Data writen successfully")

            else:

                print(writer)

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = FeedBackApp()
    window.show()
    sys.exit(app.exec_())
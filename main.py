import sys
from PyQt6 import QtWidgets, uic
from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import QLabel, QApplication
from PyQt6.QtCore import QTimer
from datetime import datetime

from PyQt6 import QtCore, QtWidgets




class MyApp(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        try:
            # Load the UI file
            uic.loadUi('main2.ui', self)

            # Set fixed size based on loaded UI
            self.setFixedSize(self.size())

            # Initialize the emergency label
            self.emergency_label_text = "Ganapin || Emergency Calls  "
            self.emergency_label = QLabel(self.emergency_label_text, self)
            self.emergency_label.setGeometry(QtCore.QRect(10, 0, 91, 16))
            
            #if you want target the lael name it setobject then put stylesheet

            self.emergency_label.setObjectName("emergencyLabel")
            # Create a timer to update the text
            self.timer = QTimer(self)
            self.timer.timeout.connect(self.update_text)
            self.timer.start(200)  # Update every 200 milliseconds
            ##date today and time

            # Get current date and time
            # Initialize the date label
            self.date_label = QLabel(self)
            self.date_label.setGeometry(QtCore.QRect(120, 0, 150, 16))  # Adjusted width for longer text
            self.date_label.setObjectName('dateLabel')

        # Set up the timer to update the time every second
            self.timer = QtCore.QTimer(self)
            self.timer.timeout.connect(self.update_time)
            self.timer.start(1000)  # Update every 1000 milliseconds (1 second)

        # Initialize the time display
            self.update_time()

            # Apply stylesheet
            self.setStyleSheet("""
                #emergencyLabel {
                    color: white;
                }
                #dateLabel {
                    color: white;
                }
            """)

            # Attempt to find the get_started_bt button
            self.get_started_bt.clicked.connect(self.show_page2)
            self.push_button_1.clicked.connect(self.show_page3)
            self.push_button_2.clicked.connect(self.show_page4)
            self.push_button_3.clicked.connect(self.show_balmoso_page)
            self.push_button_4.clicked.connect(self.show_whity_page)
            self.homepage_bt_1.clicked.connect(self.homepage_page)
            self.homepage_bt_2.clicked.connect(self.homepage_page)
            self.homepage_bt_3.clicked.connect(self.homepage_page)
            self.homepage_bt_4.clicked.connect(self.homepage_page)
            # Create a stacked layout to manage pages

            self.stacked_layout = QtWidgets.QStackedLayout()
            self.get_started = self.findChild(QtWidgets.QWidget, 'get_started') #get started page
            self.homepage = self.findChild(QtWidgets.QWidget, 'homepage') #homepage
            self.melina_page = self.findChild(QtWidgets.QWidget, 'melina_page') #melina page
            self.rosas_page = self.findChild(QtWidgets.QWidget, 'rosas_page') #rosas page
            self.balsomo_page = self.findChild(QtWidgets.QWidget, 'balmoso_page') #balmoso page
            self.whity_page = self.findChild(QtWidgets.QWidget, 'whity_page') #balmoso page
            self.stacked_layout.addWidget(self.get_started)
            self.stacked_layout.addWidget(self.homepage)  #homepage
            self.stacked_layout.addWidget(self.melina_page)  #melina page
            self.stacked_layout.addWidget(self.rosas_page)#rosas page
            self.stacked_layout.addWidget(self.balsomo_page) #balmoso_page
            self.stacked_layout.addWidget(self.whity_page) #whity_page
            self.setLayout(self.stacked_layout)
            #whity_page
            #balmoso_page
        except FileNotFoundError:
            print("UI file 'main2.ui' not found.")

    def homepage_page(self):
        # Switch to page_2 in the stacked layout
        self.stacked_layout.setCurrentWidget(self.homepage)


    def show_page2(self):
        # Switch to page_2 in the stacked layout
        self.stacked_layout.setCurrentWidget(self.homepage)

    def show_page3(self):
        '''this page is for melina'''
        # Switch to page_2 in the stacked layout
        self.stacked_layout.setCurrentWidget(self.melina_page)

    def show_page4(self):
        '''this page is for Rosas'''
        # Switch to page_2 in the stacked layout
        self.stacked_layout.setCurrentWidget(self.rosas_page)

    def show_balmoso_page(self):
        '''this page is for Rosas'''
        # Switch to page_2 in the stacked layout
        self.stacked_layout.setCurrentWidget(self.balsomo_page)
    
    def show_whity_page(self):
        '''this page is for Rosas'''
        # Switch to page_2 in the stacked layout
        self.stacked_layout.setCurrentWidget(self.whity_page)

    def update_text(self):
        # Shift the text
        self.emergency_label_text = self.emergency_label_text[1:] + self.emergency_label_text[0]
        self.emergency_label.setText(self.emergency_label_text)


    def update_time(self):
        # Get current date and time
        now = datetime.now()
        # Format the date and time as "day | month | day_number | year hour:minute am/pm"
        dt_string = now.strftime("%A | %B | %d | %y %I:%M %p")
        # Update the label text
        self.date_label.setText(dt_string)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_app = MyApp()
    main_app.show()
    sys.exit(app.exec())

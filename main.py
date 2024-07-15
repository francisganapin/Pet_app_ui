import sys
from PyQt6 import QtWidgets, uic
from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import QLabel, QApplication

class MyApp(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        try:
            # Load the UI file
            uic.loadUi('main2.ui', self)

            # Set fixed size based on loaded UI
            self.setFixedSize(self.size())

            # Attempt to find the get_started_bt button
            self.get_started_bt = self.findChild(QtWidgets.QPushButton, 'get_started_bt')
            if self.get_started_bt:
                self.get_started_bt.clicked.connect(self.show_page2)
            else:
                print("Button 'get_started_bt' not found in UI.")

            self.push_button_1 = self.findChild(QtWidgets.QPushButton, 'push_button_1')
            if self.push_button_1:
                self.push_button_1.clicked.connect(self.show_page3)
            else:
                print("Button 'push_button_1' not found in UI.")

            self.push_button_2 = self.findChild(QtWidgets.QPushButton, 'push_button_2') 
            if self.push_button_2:
                self.push_button_2.clicked.connect(self.show_page4)
            else:
                print("Button 'push_button_1' not found in UI.")
            

            self.push_button_3 = self.findChild(QtWidgets.QPushButton,'push_button_3')
            if self.push_button_3:
                self.push_button_3.clicked.connect(self.show_balmoso_page)
            else:
                print('wala')

            self.push_button_3 = self.findChild(QtWidgets.QPushButton,'push_button_4')
            if self.push_button_3:
                self.push_button_3.clicked.connect(self.show_whity_page)
            else:
                print('wala')


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

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_app = MyApp()
    main_app.show()
    sys.exit(app.exec())

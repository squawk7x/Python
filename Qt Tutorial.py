import sys
from PySide2.QtWidgets import QApplication, QPushButton
from PySide2.QtCore import SIGNAL, Signal, QObject


def func():
	print("func has been called!")


app = QApplication(sys.argv)
button = QPushButton("Call func")
QObject.connect(button, SIGNAL('clicked()'), func)
button.show()
sys.exit(app.exec_())

import sys
from PySide2.QtWidgets import QApplication, QPushButton


def func():
	print("func has been called!")


app = QApplication(sys.argv)
button = QPushButton("Call func")
button.clicked.connect(func)
button.show()
sys.exit(app.exec_())

import sys
from PySide2.QtWidgets import QApplication, QPushButton


# define a function that will be used as a slot
def sayHello():
	print('Hello world!')


app = QApplication(sys.argv)
button = QPushButton('Say hello!')
# connect the clicked signal to the sayHello slot
button.clicked.connect(sayHello)
button.show()
sys.exit(app.exec_())

import sys
from PySide2.QtWidgets import QApplication, QPushButton
from PySide2.QtCore import QObject, Signal, Slot

app = QApplication(sys.argv)


# define a new slot that receives a string and has
# 'saySomeWords' as its name
@Slot(str)
def say_some_words(words):
	print(words)


class Communicate(QObject):
	# create a new signal on the fly and name it 'speak'
	speak = Signal(str)


someone = Communicate()
# connect signal and slot
someone.speak.connect(say_some_words)
# emit 'speak' signal
someone.speak.emit("Hello everybody!")

sys.exit(app.exec_())

import sys
from PySide2.QtWidgets import QApplication, QPushButton
from PySide2.QtCore import QObject, Signal, Slot

app = QApplication(sys.argv)


# define a new slot that receives a C 'int' or a 'str'
# and has 'say_something' as its name
@Slot(int)
@Slot(str)
def say_something(stuff):
	print(stuff)


class Communicate(QObject):
	# create two new signals on the fly: one will handle
	# int type, the other will handle strings
	speak_number = Signal(int)
	speak_word = Signal(str)


someone = Communicate()
# connect signal and slot properly
someone.speak_number.connect(say_something)
someone.speak_word.connect(say_something)
# emit each 'speak' signal
someone.speak_number.emit(10)
someone.speak_word.emit("Hello everybody!")

sys.exit(app.exec_())

import sys
from PySide2.QtWidgets import QApplication, QPushButton
from PySide2.QtCore import QObject, Signal, Slot

app = QApplication(sys.argv)


# define a new slot that receives a C 'int' or a 'str'
# and has 'saySomething' as its name
@Slot(int)
@Slot(str)
def say_something(stuff):
	print(stuff)


class Communicate(QObject):
	# create two new signals on the fly: one will handle
	# int type, the other will handle strings
	speak = Signal((int,), (str,))


someone = Communicate()
# connect signal and slot. As 'int' is the default
# we have to specify the str when connecting the
# second signal
someone.speak.connect(say_something)
someone.speak[str].connect(say_something)
# emit 'speak' signal with different arguments.
# we have to specify the str as int is the default
someone.speak.emit(10)
someone.speak[str].emit("Hello everybody!")

sys.exit(app.exec_())

import sys
from PySide2.QtCore import QObject, Signal


# Must inherit QObject for signals
class Communicate(QObject):
	speak = Signal()
	
	def __init__(self):
		super(Communicate, self).__init__()
		self.speak.connect(self.say_hello)
	
	def speaking_method(self):
		self.speak.emit()
	
	def say_hello(self):
		print("Hello")


someone = Communicate()
someone.speaking_method()

import sys
from PySide2.QtCore import QObject, Slot, Signal, QThread


# Create the Slots that will receive signals
@Slot(str)
def update_a_str_field(message):
	print(message)


@Slot(int)
def update_a_int_field(self, value):
	print(value)


# Signals must inherit QObject
class Communicate(QObject):
	signal_str = Signal(str)
	signal_int = Signal(int)


class WorkerThread(QThread):
	def __init__(self, parent=None):
		QThread.__init__(self, parent)
		self.signals = Communicate()
		# Connect the signals to the main thread slots
		self.signals.signal_str.connect(parent.update_a_str_field)
		self.signals.signal_int.connect(parent.update_a_int_field)
	
	def run(self):
		self.signals.update_a_int_field.emit(1)
		self.signals.update_a_str_field.emit("Hello World.")


from PySide2.QtCore import Qt, Signal, QEvent
from PySide2.QtWidgets import QWidget


class Button(QWidget):
	clicked = Signal(Qt.MouseButton)
	
	def mousePressEvent(self, event):
		self.clicked.emit(event.button())


"""

import sys

from PySide2.QtCore import SIGNAL, QObject
from PySide2.QtWidgets import (QLineEdit, QPushButton, QApplication,
                               QVBoxLayout, QDialog, QMessageBox, QLabel,
                               QSlider, QProgressBar, QGroupBox, QRadioButton,
                               QTextEdit, QLCDNumber)


class Form(QDialog):

	def __init__(self, parent=None):
		super(Form, self).__init__(parent)
		# Create widgets
		self.edit = QLineEdit("LineEdit")
		self.clearbutton = QPushButton("Clear")
		self.label = QLabel("Label")
		self.button = QPushButton("Pushbutton")
		self.slider = QSlider()
		self.slider.setRange(0, 100)
		self.slider.setValue(50)
		self.slider.setMinimumHeight(100)
		self.progressbar = QProgressBar()
		self.progressbar.setRange(0, 100)
		self.textedit = QTextEdit()
		self.lcdnumber = QLCDNumber()
		#self.slider.valueChanged.connect(self.updateprogressbar)

		# Create layout and add widgets
		layout = QVBoxLayout()
		layout.addWidget(self.edit)
		layout.addWidget(self.clearbutton)
		layout.addWidget(self.label)
		layout.addWidget(self.slider)
		layout.addWidget(self.button)
		layout.addWidget(self.progressbar)
		layout.addWidget(self.lcdnumber)

		# Set groupbox layout
		self.groupbox = QGroupBox("GroupBox")
		self.groupbox.setCheckable(True)

		layout.addWidget(self.groupbox)
		layout.addWidget(self.textedit)

		gboxlayout = QVBoxLayout()
		self.rb1 = QRadioButton("RadioButton 1")
		gboxlayout.addWidget(self.rb1)
		self.rb2 = QRadioButton("RadioButton 2")
		gboxlayout.addWidget(self.rb2)
		self.groupbox.setLayout(gboxlayout)

		# Set dialog layout
		self.setLayout(layout)
		# Add button signal to greetings slot
		self.clearbutton.clicked.connect(self.label.clear)
		self.button.clicked.connect(self.greetings)
		self.button.clicked.connect(self.updatelabel)
		self.slider.valueChanged.connect(self.updateprogressbar)
		#self.button.clicked.connect(self.mbox)
		#self.button.connect(self.button, self.mbox)

	# Greets the user
	def greetings(self):
		print(self.edit.text())

	def updatelabel(self):
		self.label.setText(self.edit.text())


	def updateprogressbar(self):
		self.progressbar.setValue(self.slider.value())
		self.lcdnumber.display((self.slider.value()))
		self.textedit.setText(str(self.slider.value()))

	def mbox(self):
		print("Hallo aus mbox")
		msgbox = QMessageBox()
		msgbox.setText(self.edit.text())
		msgbox.exec_()


if __name__ == '__main__':
	# Create the Qt Application
	app = QApplication(sys.argv)
	# Create and show the form
	form = Form()
	form.show()
	# Run the main Qt loop
	sys.exit(app.exec_())

"""
import sys

from PySide2.QtWidgets import QApplication, QDialog, QVBoxLayout, QLabel, QLineEdit, QPushButton, QTextEdit


class dialog(QDialog):
	
	def __init__(self):
		super().__init__()
		vblayout = QVBoxLayout(self)
		klabel = QLabel(self)
		klabel.setText('Startkapital')
		self.kedit = QLineEdit(self)
		self.kedit.setMaxLength(10)
		# self.kedit.setAlignment()
		self.kedit.setInputMask("000000000")
		
		ilabel = QLabel(self)
		ilabel.setText('Zinssatz (%)')
		self.iedit = QLineEdit(self)
		self.iedit.setMaxLength(4)
		self.iedit.setInputMask("00.00")
		nlabel = QLabel(self)
		nlabel.setText('Laufzeit (Jahre)')
		self.nedit = QLineEdit(self)
		self.nedit.setMaxLength(2)
		self.nedit.setInputMask("00")
		elabel = QLabel(self)
		elabel.setText("Ergebnis:")
		self.tedit = QTextEdit(self)
		self.tedit.setDisabled(True)
		
		pbutton = QPushButton(self)
		pbutton.setText("Calculate")
		
		vblayout.addWidget(klabel)
		vblayout.addWidget(self.kedit)
		vblayout.addWidget(ilabel)
		vblayout.addWidget(self.iedit)
		vblayout.addWidget(nlabel)
		vblayout.addWidget(self.nedit)
		vblayout.addWidget(elabel)
		vblayout.addWidget(self.tedit)
		vblayout.addWidget(pbutton)
		
		pbutton.clicked.connect(self.calculate)
	
	def calculate(self):
		
		K = int(self.kedit.text())
		i = float(self.iedit.text())
		n = int(self.nedit.text())
		
		Kn = K * ((1 + i / 100) ** n)
		self.tedit.setText('{:.2f}'.format(Kn))


app = QApplication(sys.argv)
dia = dialog()
dia.show()
sys.exit(app.exec_())

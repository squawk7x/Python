import sys
from PySide2.QtCore import QObject, Signal, Slot


class receiver(QObject):

	@Slot(str)
	def answer_str(self, message):
		print("message: " + message)
	
	@Slot(int)
	def answer_int(self, value):
		print("value: " + str(value))
		
	@Slot(str)
	@Slot(int)
	def answer_sth(self, sth):
		if isinstance(sth, str):
			print("String :", sth)
		if isinstance(sth, int):
			print("Wert: ", sth)
			
	@Slot(str, int)
	def answer(self, *sth):
		if isinstance(sth[0], str):
			print("String :", sth[0])
		if isinstance(sth[1], int):
			print("Wert: ", sth[1])


class sender(QObject):
	signal_str = Signal(str)
	signal_int = Signal(int)            # 1 type
	signal_bth = Signal(str, int)       # more than 1 value
	signal_sth = Signal((str,), (int,)) # optional types
	

r = receiver()
s = sender()
s.signal_str.connect(r.answer_str)
s.signal_int.connect(r.answer_int)

s.signal_sth[str].connect(r.answer_sth)
s.signal_sth[int].connect(r.answer_sth)

s.signal_bth.connect(r.answer)

s.signal_int.emit(10)
s.signal_str.emit("abc")
s.signal_sth[int].emit(20)
s.signal_sth.emit("def")
s.signal_bth.emit("xyz", 1001)


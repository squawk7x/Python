from PySide2.QtCore import QObject, Signal, Slot, SIGNAL, SLOT


class Empty(object):
	pass


class Father(QObject):
	signal_from_father = Signal(str)
	
	def __init__(self):
		super().__init__()
		self.setObjectName("Dad")
	
	@Slot(int)
	def answer_from_father(self):
		print("Hello Son!")
	
	@Slot(float)
	def answer_from_father(self):
		print("Hello Daughter!")


class Son(Father):
	signal_from_son = Signal(int)
	
	def __init__(self):
		super().__init__()
		self.setObjectName("Tom")
	
	@Slot(str)
	def answer_from_son(self):
		print("Hello Father from Son")
	
	@Slot(float)
	def answer_from_son(self):
		print("Hello Sister from Brother")


class Daughter(Father):
	signal_from_daughter = Signal(float)
	
	def __init__(self):
		super().__init__()
		self.setObjectName("Kim")
	
	@Slot(str)
	def answer_from_daughter(self):
		print("Hello Father from Daughter")
	
	@Slot(int)
	def answer_from_daughter(self):
		print("Hello Brother from Sister")


father = Father()
son = Son()
son.setParent(father)
daughter = Daughter()
daughter.setParent(father)

# String based form:
QObject.connect(father, SIGNAL("father.signal_from_father(str)"), son, SLOT("answer_from_son()"))
QObject.connect(father, SIGNAL("father.signal_from_father(str)"), daughter, SLOT("answer_from_daughter()"))

# Pointer based form:
father.signal_from_father.connect(son.answer_from_son)
father.signal_from_father.connect(daughter.answer_from_daughter)
son.signal_from_son.connect(father.answer_from_father)
son.signal_from_son.connect(daughter.answer_from_daughter)
daughter.signal_from_daughter.connect(father.answer_from_father)
daughter.signal_from_daughter.connect(son.answer_from_son)

father.signal_from_father.emit(str('abc'))
son.signal_from_son.emit(int(1))
daughter.signal_from_daughter.emit(float(1))

# print("__slots__(): ", father.__slots__())
print("son.signalsBlocked(): ", son.signalsBlocked())
print("children: ", father.children())
print("findChield: ", father.findChild(Son))
print("findChildren: ", father.findChildren(QObject))
print("inherits: ", son.inherits("father"))
# print("daughter isSignalConnected: ", daughter.isSignalConnected(father.metaObject().Connection))
print("isWidgetType: ", father.isWidgetType())
print("objectName: ", son.objectName())
print("parent: ", son.parent().objectName())
print("property: ", son.property("son"))
print("receivers from father signal: ", father.receivers(SIGNAL("father.signal_from_father(str)")))
print("receivers from son signal: ", son.receivers(SIGNAL("son.signal_from_son(int)")))
print("receivers from daughter signal: ", daughter.receivers(SIGNAL("daughter.signal_from_daughter(float)")))
print("thread: ", son.thread())
print("son.metaObject().className(): ", son.metaObject().className())
print("son.inherits('Father'): ", son.inherits("Father"))
print("son.inherits('Daughter'): ", son.inherits("Daughter"))
print("son.inherits('QObject'): ", son.inherits("QObject"))

father.dumpObjectInfo()
son.dumpObjectInfo()
daughter.dumpObjectInfo()

father.dumpObjectTree()
son.dumpObjectTree()
daughter.dumpObjectTree()

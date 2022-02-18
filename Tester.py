class Z:
	class_var = 1

	def __init__(self):
		self.inst_var = 2


z = Z()

print(dir(z))
print(help(z))

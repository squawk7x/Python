'''

Text Files:

- Plain Text
- XML
- JSON
- Source Code

Binary Files:

- Compiled Code
- App data
- Media files

'''

f = open(r"./test.txt")
text = f.read()
f.close()

print(text)

with open(r"./test.txt") as fobj:
	bio = fobj.read()

print(bio)

try:
	with open("./future_lottery_numbers.txt") as f:
		text = f.read()
except FileNotFoundError:
	text = None

print(text)

try:
	with open(r"./test.txt") as f:
		text = f.read()
except FileNotFoundError:
	text = None

print(text)

oceans = ["Pacific", "Atlantic", "Indian", "Southern", "Arctic"]

with open("./test.txt", "w") as f:
	for ocean in oceans:
		f.write(ocean)
		f.write("\n")

oceans = ["Pacific", "Atlantic", "Indian", "Southern", "Arctic"]

with open(r"./test.txt", "w") as f:
	for ocean in oceans:
		print(ocean, file=f)

with open(r"./test.txt", "a") as f:
	print(23 * "=", file=f)
	print("These are the 5 oceans.", file=f)

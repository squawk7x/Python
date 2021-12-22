try:
	# Runs first
	pass
except:
	# Runs if exeption occurs in try block
	pass
else:
	# Excecutes if the try block *succeeds*
	pass
finally:
	# This code *always* executes
	pass



import logging
import time

# Create logger
logging.basicConfig(filename="./test.log", level=logging.DEBUG)
logger = logging.getLogger()


def read_file_timed(path):
	"""Return the contents of the file at 'path' and measure the time required."""
	start_time = time.time()
	try:
		f = open(path, "rb")
		data = f.read()
		return data
	except FileNotFoundError as err:
		logging.error(err)
		raise
	else:
		f.close()
	finally:
		stop_time = time.time()
		dt = stop_time - start_time
		logging.info("Time required for {file} = {time}.".format(file=path, time=dt))


data = read_file_timed(r"C:\Users\lightrao\Downloads\imaginary_file.png")

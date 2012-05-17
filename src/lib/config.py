""" """

from panda3d.core import Filename
import re

class Config( dict ):
	"""Read and structure a config file for easier access. Allows for file reading code
	and such to be in a single location as well (easier for unittesting.

	>>> c = Config("config/main.cfg")
	>>> c.process()
	>>> for key, val in c.items(): BlockType( key, ** val )
	"""

	def __init__(self, fileObj):
		""" """

		from fileObjectInterface import FileObjectIF

		if not isinstance(fileObj, FileObjectIF): raise TypeError( fileObj )

		super( Config, self ).__init__()
		self.fileObj = fileObj
		return None

	def __setitem__(self, key, value):
		"""Update the file when needed."""
		return dict.__setitem__(self, key, value)

	def parse(self, value):
		"""Parse a value of the configfile and turn it into something sensible"""
		# convert empty strings to None values?
		if not value: return None
		elif value.lower() == 'true': return True
		elif value.lower() == 'false': return False
		# parse simple numbers
		elif re.match('^\d+$', value ): return int( value )
		# parse floats?
		elif re.match('^\d+\.\d+$', value): return float( value )
		elif value[:5] == 'path:': return Filename( value[5:] )
		elif value[0] == '(' and value[-1] == ')':
			return tuple( [ self.parse( s.strip() ) for s in value[1:-1].split(',') ] )
		else: return value

	def process(self):
		"""Read the file and structure all the info."""

		self.fileObj.open()
		part = None
		partDict = None

		while True:
			line = self.fileObj.readline()
			# Great, there is no way to check for EOF other then getting an empty string,
			# so strip whitespace and such (meaning empty lines '\n' become '') only after
			# we check that line is empty.
			if not line:
				# Add the last part, if necessary
				if part and partDict: self[ part ] = partDict
				break
			else: line = line.strip()

			# if the line is empty now it was just a blank line but there is more in the
			# file.
			if not line: continue

			if '#' == line[0]: pass
			elif '[' == line[0]:
				if part and partDict: self[ part ] = partDict
				part = line[1:-1].strip()
				partDict = {}
			else:
				key, value = line.split('=', 1)
				value = self.parse( value.strip() )
				partDict[ key.strip() ] = value

		self.fileObj.close()

		return None


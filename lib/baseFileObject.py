""" """

from fileObjectInterface import FileObjectIF

class BaseFileObject( FileObjectIF ):
	""" """

	def __init__(self):
		""" """
		super(BaseFileObject, self).__init__()
		self.closed = True
		return None

	def read(self, amount):
		""" """
		if self.closed: raise Exception( "File is closed", self )
		return self.fp.read( amount )

	def readlines(self):
		""" """
		if self.closed: raise Exception( "File is closed", self )
		return self.fp.readlines()

	def readline(self):
		""" """
		if self.closed: raise Exception( "File is closed", self )
		return self.fp.readline()

	def write(self, value):
		""" """
		if self.closed: raise Exception( "File is closed", self )
		return self.fp.write( value )

	def writelines(self, iterable):
		""" """
		if self.closed: raise Exception( "File is closed", self )
		return self.fp.writelines( iterable )

	def seek(self, index):
		""" """
		if self.closed: raise Exception( "File is closed", self )
		return self.fp.seek( index )

	def __iter__(self): return self.fp.__iter__()

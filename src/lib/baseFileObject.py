""" """

from fileObjectInterface import FileObjectIF

class BaseFileObject( FileObjectIF ):
	""" """

	def __init__(self):
		""" """
		super(BaseFileObject, self).__init__()
		self.closed = True
		return None

	def read(self, amount=None):
		""" """
		if self.closed: raise Exception( "File is closed", self )
		if not self.exists(): raise Exception( 'File does not exist', self )
		if amount: return self.fp.read( amount )
		else: return self.fp.read()

	def readlines(self):
		""" """
		if self.closed: raise Exception( "File is closed", self )
		if not self.exists(): raise Exception( 'File does not exist', self )
		return self.fp.readlines()

	def readline(self):
		""" """
		if self.closed: raise Exception( "File is closed", self )
		if not self.exists(): raise Exception( 'File does not exist', self )
		return self.fp.readline()

	def write(self, value):
		""" """
		if self.closed: raise Exception( "File is closed", self )
		if not self.exists(): raise Exception( 'File does not exist', self )
		return self.fp.write( value )

	def writelines(self, iterable):
		""" """
		if self.closed: raise Exception( "File is closed", self )
		if not self.exists(): raise Exception( 'File does not exist', self )
		return self.fp.writelines( iterable )

	def seek(self, index):
		""" """
		if self.closed: raise Exception( "File is closed", self )
		if not self.exists(): raise Exception( 'File does not exist', self )
		return self.fp.seek( index )

	def __iter__(self): return self.fp.__iter__()

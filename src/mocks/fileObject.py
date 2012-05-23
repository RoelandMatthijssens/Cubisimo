""" """

from StringIO import StringIO

from lib.baseFileObject import BaseFileObject


class FileObjectMock( BaseFileObject ):
	""" """

	def __init__(self, string = ''):
		""" """
		super(FileObjectMock, self).__init__()
		self.fp = StringIO( string )
		self.closed = False
		self.fileExists = True

	def exists(self): return self.fileExists

	def setExists(self, boolean): self.fileExists = False
	def open(self, mode=None): self.closed = False
	def close(self): self.closed = True

	def create(self):
		''' '''
		self.fileExists = True
		self.fp = StringIO( '' )
		# self.fp.seek( 0 )
		return None


""" """

from cStringIO import StringIO

from lib.baseFileObject import BaseFileObject

class FileObjectMock( BaseFileObject ):
	""" """

	def __init__(self, string = ''):
		""" """
		super(FileObjectMock, self).__init__()
		self.fp = StringIO( string )
		self.closed = False

	def open(self, mode=None): self.closed = False
	def close(self): self.closed = True

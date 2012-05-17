""" """

from lib.config import Config

from mocks.fileObject import FileObjectMock


class ConfigMock( Config ):
	""" """

	def __init__(self, *stringList):
		""" """
		self.fileObj = FileObjectMock( '\n'.join( stringList ) )
		super( ConfigMock, self ).__init__( self.fileObj )
		self.process()
		return None


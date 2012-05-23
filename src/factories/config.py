""" """

from mocks.fileObject import FileObjectMock
from lib.config import Config

class ConfigSetup( object ):
	''' '''

	@classmethod
	def create(cls, *stringList ):
		''' '''
		fileObj = FileObjectMock( '\n'.join( stringList ) )
		config = Config( fileObj )
		config.process()
		return config

	@classmethod
	def prepare(cls): return ()


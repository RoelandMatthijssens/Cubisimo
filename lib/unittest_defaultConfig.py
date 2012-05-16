""" """

from fileObjectMock import FileObjectMock
from panda3d.core import Filename
from defaultConfig import DefaultConfig
from unittest import TestCase, TestSuite, TextTestRunner, main

class DefaultConfigSetup( TestCase ):
	""" """

	def setUp(self):
		""" """
		self.lines = [ '# testfile'
				, '[vals]'
				, 'first=2'
				, 'second=False'
				]
		self.defaults = { 'first': 5, 'third': 'third' }
		self.fileObj = FileObjectMock( '\n'.join(self.lines) )
		return None

	def initializing(self):
		"""It should initialize without errors."""
		self.assertIsInstance( DefaultConfig( self.fileObj, ALL=self.defaults )
				, DefaultConfig
				, 'Initialization failed.'
				)
		return None

	def fileParsing(self):
		"""It should not crash when parsing a file."""
		self.c = DefaultConfig( self.fileObj, ALL=self.defaults )
		self.assertIsNone( self.c.process(), 'Parsing of the file failed.')
		return None


class BasicDefaultConfigTest( DefaultConfigSetup ):
	""" """

	def setUp(self):
		""" """
		DefaultConfigSetup.setUp(self)
		self.c = DefaultConfig( self.fileObj, ALL=self.defaults )
		self.c.process()
		return None

	def undefinedOnes(self):
		"""It should have the default values if they were not given in the config file."""
		section = self.c['vals']
		self.assertIn( 'third', section, 'DefaultConfig does not have defaults.' )
		self.assertEqual( section['third'], 'third', 'DefaultConfig has the wrong defaults.' )
		return None
	
	def definedOnes(self):
		"""It should overwrite default values with the ones in the config file."""
		section = self.c['vals']
		self.assertEqual( section['first'], 2 )
		return None


suite = TestSuite()
suite.addTest( DefaultConfigSetup( "initializing" ) )
suite.addTest( DefaultConfigSetup( "fileParsing" ) )

suite.addTest( BasicDefaultConfigTest( 'undefinedOnes' ) )
suite.addTest( BasicDefaultConfigTest( 'definedOnes' ) )

if __name__ == '__main__':
	TextTestRunner(verbosity=2).run( suite )

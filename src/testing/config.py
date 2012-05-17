""" """

from lib.config import Config
from mocks.fileObject import FileObjectMock

from panda3d.core import Filename

from unittest import TestCase, TestSuite, TextTestRunner, main

class ConfigSetup( TestCase ):
	"""Test the Config Parser."""

	def setUp(self):
		""" """
		self.lines = [ '# testfile'
				, '[balthazar]'
				, 'firstval=2'
				, 'secondval=somestring'
				, '[whatdoyouknow]'
				, 'crap='
				, 'val=4.3'
				, '[paths]'
				, 'base=path:models/eggs/'
				, '[tuples]'
				, 'tupleExample=(1, 2, 3)'
				, '[booleans]'
				, 'isSo=True'
				, 'notSo=False'
				, 'lowerSo=true'
				, 'lowerNot=false'
				]
		self.sectionCount = 5
		self.fileObj = FileObjectMock( '\n'.join(self.lines) )
		return None
	
	def it_should_initializing(self):
		"""It should initialize without errors."""
		self.assertIsInstance( Config( self.fileObj ), Config, 'Initialization failed.' )
		return None

	def it_should_parse_its_file(self):
		"""It should not crash when parsing a file."""
		self.c = Config( self.fileObj )
		self.assertIsNone( self.c.process(), 'Parsing of the file failed.')
		self.assertTrue( len( self.c ) == self.sectionCount, 'Sections count is incorrect.' )
		return None


class BasicConfigTest( ConfigSetup ):
	""" """

	def setUp(self):
		""" """
		ConfigSetup.setUp(self)
		self.c = Config( self.fileObj )
		self.c.process()
		return None

	def it_should_retrieve_sections(self):
		"""It should have the sections described by the config file."""
		# s = " : ".join( self.c.keys() )
		# self.assertEqual( s, '' )
		self.assertTrue( "balthazar" in self.c.keys(), "Sections are missing." )
		self.assertTrue( "whatdoyouknow" in self.c.keys(), "Sections are missing." )

	def it_should_have_values_in_sections(self):
		"""It should have the values described in the config file for each sections."""
		section = self.c[ 'balthazar' ]
		self.assertIn( 'firstval', section, 'Section does not have the right values.' )
		self.assertIn( 'secondval', section, 'Section does not have the right values.' )
		self.assertEqual( section[ 'secondval' ], 'somestring', 'Section has the wrong values.' )
		return None


class ConfigParsingTest( BasicConfigTest ):
	""" """

	def it_should_detect_integers(self):
		"""It should convert integers in the config file to actual integer objects.""" 
		section = self.c[ 'balthazar' ]
		self.assertEqual( section[ 'firstval' ], 2, 'Config does not parse integers.' )
		return None

	def it_should_detect_floats(self):
		"""It should convert decimal numbers in the config file to actual float objects.""" 
		section = self.c[ 'whatdoyouknow' ]
		self.assertEqual( section[ 'val' ], 4.3, 'Config does not parse floats.' )
		return None

	def it_should_detect_empty_strings(self):
		"""Empty strings as values in the config file should be converted to None."""
		section = self.c[ 'whatdoyouknow' ]
		self.assertIsNone( section[ 'crap' ], 'Config does not convert empty values.' )
		return None

	def it_should_detect_pathnames(self):
		"""It should convert pathnames in the value to path objects (val=path:model/cube.egg)."""
		section = self.c[ 'paths' ]
		path = section[ 'base' ]
		self.assertIsInstance( path, Filename, 'Config does not convert paths.')
		self.assertEqual( str(path), 'models/eggs/', 'Path is incorrect.' )
		return None

	def it_should_detect_tuples(self):
		"""It should convert tuples to python tuples."""
		section = self.c[ 'tuples' ]
		t = section[ 'tupleExample' ]
		self.assertIsInstance( t, tuple, 'Config does not convert tuples.')
		self.assertEqual( t, (1, 2, 3), 'Config does not convert tuples corectly.' )
		return None

	def it_should_detect_booleans(self):
		"""It should convert strings like 'true' and 'False' to their boolean values."""
		section = self.c[ 'booleans' ]
		self.assertTrue( section[ 'isSo' ], '')
		self.assertFalse( section[ 'notSo' ], '' )
		self.assertTrue( section[ 'lowerSo' ], '')
		self.assertFalse( section[ 'lowerNot' ], '' )
		return None


class ConfigWhitespaceTest( BasicConfigTest ):
	""" """

	def setUp(self):
		BasicConfigTest.setUp( self )
		self.lines = [ '# testfile'
				, '[uselessWhitespace]'
				, '\tstartWithTab=2'
				, 'spaceBeforeEqual =somestring'
				, 'spaceAfterEqual= AVal'
				, 'trailingSpaces=What?\t   '
				, '[whitespace in title]'
				, 'val='
				, '[  leading and trailing whitespace \t ]'
				, 'val='
				, '[whitespace in keys]'
				, 'some val=4'
				, 'other val =4'
				, '[whitespace in values]'
				, 'key=A String With Whitespace'
				, 'secondkey = A String With Whitespace'
                , 'int= 4  '
				]
		self.fileObj = FileObjectMock( '\n'.join(self.lines) )
		self.c = Config( self.fileObj )
		self.c.process()
		return None

	def it_should_strip_whitespace_from_values(self):
		"""The Config parser should strip meaningless whitespace in values."""
		section = self.c['uselessWhitespace']
		self.assertIn( 'startWithTab', section,
				'Config does not strip leading whitespace in keys.'
				)
		self.assertIn( 'spaceBeforeEqual', section,
				'Config does not strip trailing whitespace in keys.' 
				)
		return None

	def it_should_strip_whitespace_from_keys(self):
		"""The Config parser should strip meaningless whitespace in keys."""
		section = self.c['uselessWhitespace']
		self.assertEqual( section['spaceAfterEqual'], 'AVal',
				'Config does not strip leading whitespace in values.'
				)
		self.assertEqual( section['trailingSpaces'], 'What?', 
				'Config does not strip trailing whitespace in values.'
				)
		return None

	def it_should_strip_whitespace_from_section_titles(self):
		"""The Config parser should strip leading and trailing whitespaces in sectin titles."""
		self.assertIn( 'leading and trailing whitespace', self.c,
				'Config did not strip whitespace in section titles.' + str( self.c.keys())
				)
		return None

	def it_should_keep_whitespace_within_values(self):
		"""The Configparser should keep whitepsace in values when relevant."""
		section = self.c['whitespace in values']
		s = 'A String With Whitespace'
		self.assertEqual( section['key'], s, '' )
		self.assertEqual( section['secondkey'], s, '')
		self.assertEqual( section['int'], 4 )
		return None

	def it_should_keep_whitespace_within_keys(self):
		"""The Config parser should keep whitespace in keys when relevant."""
		section = self.c['whitespace in keys']
		self.assertIn( 'some val', section, '' )
		self.assertIn( 'other val', section, '' )
		return None

	def it_should_keep_whitespace_within_section_titles(self):
		"""The Config parser should keep whitespace in sectin titles when relevant."""
		self.assertIn( 'whitespace in title', self.c,
				'Config did something wierd with whitespace in the section titles.'
				)
		return None


class WriteBehaviorConfigTest( BasicConfigTest ):
	""" """

	def test_writeNewVluesToFile(self):
		"""It should update the config file if new properties are set."""
		raise NotImplementedError

	def test_doNotWriteToClosedFile(self):
		"""It should not write to the config file if it is closed."""
		raise NotImplementedError


suite = TestSuite()
suite.addTest( ConfigSetup( "it_should_initializing" ) )
suite.addTest( ConfigSetup( "it_should_parse_its_file" ) )

suite.addTest( BasicConfigTest( "it_should_retrieve_sections" ) )
suite.addTest( BasicConfigTest( "it_should_have_values_in_sections" ) )

suite.addTest( ConfigParsingTest( "it_should_detect_integers" ) )
suite.addTest( ConfigParsingTest( "it_should_detect_floats" ) )
suite.addTest( ConfigParsingTest( "it_should_detect_empty_strings" ) )
suite.addTest( ConfigParsingTest( "it_should_detect_pathnames" ) )
suite.addTest( ConfigParsingTest( "it_should_detect_tuples" ) )
suite.addTest( ConfigParsingTest( "it_should_detect_booleans" ) )

suite.addTest( ConfigWhitespaceTest( "it_should_strip_whitespace_from_values" ) )
suite.addTest( ConfigWhitespaceTest( "it_should_strip_whitespace_from_keys" ) )
suite.addTest( ConfigWhitespaceTest( "it_should_strip_whitespace_from_section_titles" ) )
suite.addTest( ConfigWhitespaceTest( "it_should_keep_whitespace_within_values" ) )
suite.addTest( ConfigWhitespaceTest( "it_should_keep_whitespace_within_keys" ) )
suite.addTest( ConfigWhitespaceTest( "it_should_keep_whitespace_within_section_titles" ) )

if __name__ == '__main__':
	TextTestRunner(verbosity=2).run( suite )

""" """

import os
from fileObject import FileObject
from panda3d.core import Filename
from unittest import TestCase, TestSuite, TextTestRunner, main

class FileObjectSetup( TestCase ):
	""" """

	def setUp(self):
		""" """
		self.filename = Filename( 'testFile.txt' )
		return None

	def initializing(self):
		""" """
		self.assertIsInstance( FileObject( self.filename ), FileObject )
		return None


class BasicFileObjectTest( FileObjectSetup ):
	""" """

	def setUp(self):
		""" """
		super( BasicFileObjectTest, self ).setUp()
		self.fileObj = FileObject( self.filename )
		return None

	def tearDown(self):
		""" """
		try: os.remove( self.filename.toOsSpecific() )
		except OSError, e: pass
		return None

	def exists(self):
		""" """
		self.assertFalse( self.fileObj.exists() )
		fp = open( self.fileObj.filename.toOsSpecific(), 'w+' )
		fp.close()
		self.assertTrue( self.fileObj.exists() )
		return None

	def creation(self):
		""" """
		self.fileObj.create()
		self.assertTrue( self.fileObj.exists() )
		return None


suite = TestSuite()
suite.addTest( FileObjectSetup( "initializing" ) )

suite.addTest( BasicFileObjectTest( 'exists' ) )
suite.addTest( BasicFileObjectTest( 'creation' ) )

if __name__ == '__main__':
	TextTestRunner(verbosity=2).run( suite )

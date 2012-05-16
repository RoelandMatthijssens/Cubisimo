""" """

from panda3d.core import Filename
from pandac.PandaModules import Point3

from cStringIO import StringIO

from unittest import TestCase, TestSuite, TextTestRunner

from world import World
from config import Config

class WorldSetup( TestCase ):
	""" """

	def setUp(self):
		""" """

		self.settingsLines = [ '# some comment'
				, '[general]'
				, 'chunkSize = 64'
				, 'viewDistance = 128'
				]

		self.savePath = Filename('../saveData/')
		self.settings = Config( StringIO('\n'.join(self.settingsLines)) )
		self.blockTypes = Config( StringIO( '' ) )
		self.blockTypeIds = Config( StringIO( '' ) )
		self.players = Config( StringIO( '' ) )
		self.playerIds = Config( StringIO( '' ) )

		for obj in [ self.settings, self.blockTypes, self.blockTypeIds
				, self.players, self.playerIds ]:
			obj.process()

		return None

	def initializing(self):
		""" """
		self.assertIsInstance(
			World( self.savePath, self.settings, self.blockTypes, self.blockTypeIds
				, self.players, self.playerIds
				)
			, World
			, ''
			)
		return None


class BasicWorldTest( WorldSetup ):
	""" """

	def setUp(self):
		""" """

		WorldSetup.setUp( self )
		self.world = World( self.savePath, self.settings, self.blockTypes
				, self.blockTypeIds, self.players, self.playerIds
				)

		return None

	def toChunkPos(self):
		""" """

		p = Point3( 17, 20, 9 )
		newP = self.world.toChunkPos( p )
		self.assertEqual( newP, Point3(0, 0, 0), '' )

		p = Point3( 66, 30, 201 )
		newP = self.world.toChunkPos( p )
		self.assertEqual( newP, Point3(1, 0, 3  ) )

		p = Point3( -17, -20, -9 )
		newP = self.world.toChunkPos( p )
		self.assertEqual( newP, Point3(0, 0, 0), '' )

		p = Point3( -66, -30, -201 )
		newP = self.world.toChunkPos( p )
		self.assertEqual( newP, Point3(-1, 0, -3) )

		return None

suite = TestSuite()
suite.addTest( WorldSetup( 'initializing' ) )
suite.addTest( BasicWorldTest( 'toChunkPos' ) )

if __name__ == '__main__':
	TextTestRunner(verbosity=2).run( suite )

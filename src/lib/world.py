""" """

from panda3d.core import Filename
from fileObject import FileObject
from pandac.PandaModules import Vec3
from math import ceil
from chunk import Chunk
from playerFactory import PlayerFactory
from blockTypeFactory import BlockTypeFactory
from chunkGenerator import ChunkGenerator
from encoder import Encoder

class World( object ):
	""" """

	def __init__(self, settings, playerFactory, blockTypeFactory):
		""" """
		super( World, self ).__init__()

		self.settings = settings
		self.playerFactory = playerFactory
		self.blockTypeFactory = blockTypeFactory

		return None

	def setup(self):
		""" """
		self.encoder = Encoder( self.playerFactory, self.blockTypeFactory )
		self.generator = ChunkGenerator( self.encoder, self.playerFactory
				, self.blockTypeFactory, self.settings['general']['chunkSize']
				)
		return None

	def findChunkPos(self, position ):
		"""Given the absolute coordinates of a block, get the coordinates of the chunk the
		block belongs to."""
		# shift by half the chunkSize. and devide the remainder by the chunkSize rounded
		# up.
		chunkSize = self.settings['general']['chunkSize']
		
		x, y, z = position.getX(), position.getY(), position.getZ()
		newX = round( x / chunkSize )
		newY = round( y / chunkSize )
		newZ = round( z / chunkSize )

		return Vec3( newX, newY, newZ )

	def getChunkFile( self, position ):
		"""Return the File that contains the data for the chunk at the given position."""
		var = position.getX(), position.getY(), position.getZ()
		base = self.settings['general']['save']
		filename = Filename( base + "x?%i_y?%i_z?%i.dat" % var )
		return FileObject( filename )

	def getChunks( self, position ):
		"""Return an iterater with all chunks that can be viewed from the position"""

		chunkSize = self.settings['general']['chunkSize']
		viewDist = self.settings['general']['viewDistance']
		# get all chunks that have a block within viewDist from the position. Just use a
		# max metric (maybe just for now?).
		boundary = int( ceil( viewDist / chunkSize ) )
		chunkPos = self.findChunkPos( position )

		chunkList = []
		pos = Vec3( 0, 0, 0 )
		chunk = self.getChunk( pos, chunkCoords = True )
		chunkList.append( chunk )
		return chunkList

		x = Vec3(1, 0, 0)
		y = Vec3(0, 1, 0)
		z = Vec3(0, 0, 1)

		# Oh great, there has got to be a better way.
		for i in range( 0 - boundary,  boundary+1 ):
			for j in range( 0 - boundary,  boundary+1 ):
				for k in range( 0 - boundary,  boundary+1 ):
					# shift position with i on the x axis, and so on.
					pos = chunkPos + x*i + y*j + z*k
					chunk = self.getChunk( pos, chunkCoords = True )
					chunkList.append( chunk )

		return chunkList

	def getChunk( self, position, chunkCoords = False ):
		"""Get the chunk that containse the position at coordinates posX, posY, posZ."""

		position = position if chunkCoords else self.findChunkPos( position )
		fileObj = self.getChunkFile( position )
		chunkSize = self.settings['general']['chunkSize']

		chunk = Chunk( self.encoder, self.generator, fileObj, chunkSize, position )

		return chunk


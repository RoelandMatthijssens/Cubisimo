""" """

from pandac.PandaModules import Vec3
from pandac.PandaModules import NodePath
from block import Block
from fileObjectInterface import FileObjectIF
import struct

class Chunk( object ):
	""" """

	def __init__(self, encoder, generator, fileObj, chunkSize, position):
		""" """

		from chunkGenerator import ChunkGenerator
		from encoder import Encoder
		from panda3d.core import Filename

		if not isinstance( generator, ChunkGenerator ): raise TypeError( generator )
		if not isinstance( encoder, Encoder ): raise TypeError( encoder )
		if not isinstance( fileObj, FileObjectIF ): raise TypeError( fileObj )
		if not isinstance( position, Vec3 ): raise TypeError( position )
		if not isinstance( chunkSize, int ): raise TypeError( chunkSize )

		super( Chunk, self ).__init__()
		self.encoder = encoder
		self.generator = generator
		self.position = position
		self.chunkSize = chunkSize
		self.fileObj = fileObj
		self.chunkModel = None
		self.blocks = []

		return None

	def toRelativePosition( self, position ):
		"""Given the absolute coordinates of a block, get the coordinates of the block
		relative to the chunk it belongs to."""
		chunkSize = self.settings['general']['chunkSize']
		x = position.getX() % chunkSize
		y = position.getY() % chunkSize
		z = position.getZ() % chunkSize
		return Vec3(x, y, z)

	def toAbsolutePosition(self, position):
		"""Given the position of a block in it's chunk, calculate it's position in
		absolute coordinates."""
		x = position.getX() + self.chunkSize * self.position.getX()
		y = position.getY() + self.chunkSize * self.position.getY()
		z = position.getZ() + self.chunkSize * self.position.getZ()
		return Vec3(x, y, z)

	def getFilePosition(self, position):
		"""given the coordinates within the chunk, get the index where the data of the
		block begins in the file."""
		x, y, z = position.getX(), position.getY(), position.getZ()
		index = x * self.chunkSize ** 2 + y * self.chunkSize + z
		return index

	def saveBlock(self, block):
		""" """

		position = self.toRelativePosition( block.position )
		index = self.getFilePosition( position )
		representation = self.encoder.encodeBlock( block )

		self.fileObj.open( 'w+b' )
		self.fileObj.seek( index )
		self.fileObj.write( representation )
		self.fileObj.close()

		return None

	def load(self, environment):
		"""Construct all the blocks in this chunk, and add it to the environment."""

		self.chunkModel = NodePath("chunk")
		pos = Vec3(0, 0, 0)

		if not self.fileObj.exists(): self.generator.generate(self.fileObj, self.position)

		self.fileObj.open()
		self.fileObj.seek( 0 )

		while True:
			part = self.fileObj.read( self.encoder.size() )
			block = self.encoder.decodeBlock( part, pos )

			block.create( self.chunkModel )
			self.blocks.append( block )

			if pos.getX() >= self.chunkSize - 1: pos = Vec3( 0, pos.getY() + 1, pos.getZ() )
			else: pos = pos + (1, 0, 0)
			if pos.getY() >= self.chunkSize - 1: pos = Vec3( pos.getX(), 0, pos.getZ() + 1 )
			if pos.getZ() >= self.chunkSize - 1: break

		self.fileObj.close()
		self.chunkModel.reparentTo( environment )
		return None

	def unload(self):
		""" """
		self.chunkModel.detachNode()
		return None

	def purge(self):
		"""allow the garbage collector to clean all the block data?"""
		self.chunkModel.removeNode()
		self.chunkModel = None
		return None

	def place(self, block, position):
		string = self.encoder.encodeBlock( block )
		blockIdx = self.getIdx( position )
		self.fileObj.open()
		self.fileObj.seek( blockIdx )
		self.fileObj.write( string )
		self.fileObj.close()
		return None

	def getIdx(self, position):
		''' '''
		i = position.getZ()
		i += position.getY() * self.chunkSize
		i += position.getX() * self.chunkSize ** 2
		i = i * self.encoder.size()
		if i > 0: i -= 1
		return int( i )

	def __iter__(self): return self.blocks


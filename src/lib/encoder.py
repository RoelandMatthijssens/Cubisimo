""" """

import struct

class Encoder( object ):
	""" """

	def __init__(self, playerFactory, blockTypeFactory):
		""" """

		from playerFactory import PlayerFactory
		from blockTypeFactory import BlockTypeFactory

		if not isinstance( playerFactory, PlayerFactory ): raise TypeError( playerFactory )
		if not isinstance( blockTypeFactory, BlockTypeFactory ): raise TypeError( blockTypeFactory )

		super( Encoder, self ).__init__()
		self.playerFactory = playerFactory
		self.blockTypeFactory = blockTypeFactory
		return None

	def size(self):
		""" """

		b = self.blockTypeFactory.idSize()
		p = self.playerFactory.idSize()
		d = 1 # nubmer of bytes for damage
		s = 1 # number of bytes for seed

		return p + b + d + s

	def encodeBlock(self, block):
		""" """
		encodeString = 'B' * self.size()
		encodeBytes = []
		for integer in [ block.identifier, block.owner.identifier, block.damage, block.seed ]:
			encodeBytes.extend( self.intToByteList( integer ) )

		return struct.pack( encodeString, * encodeBytes )

	def decodeBlock(self, data, position):
		""" """

		if not len( data ) == self.size(): raise Exception( data, self.size() )
		decodeString = 'B' * self.size()
		byteList = struct.unpack( decodeString, data )

		btIndex = self.blockTypeFactory.idSize()
		playerIndex = btIndex + self.playerFactory.idSize()
		damageIndex = playerIndex + 1
		seedIndex = damageIndex + 1

		blockTypeId = self.byteListToInt( byteList[ : btIndex] )
		playerId = self.byteListToInt( byteList[ btIndex : playerIndex ] )
		damage = self.byteListToInt( byteList[ playerIndex : damageIndex ] )
		seed = self.byteListToInt( byteList[ damageIndex : seedIndex ] )

		blockType = self.blockTypeFactory.fromId( blockTypeId )
		player = self.playerFactory.fromId( playerId )

		# return Block( blockType, position, player, damage, seed, blockType.baseColor )
		return blockType.newBlock( owner=player, position=position, damage=damage, seed=seed  )

	def intToByteList(self, integer ):
		""" """
		
		r =  []
		while integer > 255:
			i = integer & 255 # bitwas and the two
			integer = integer >> 8 # bitshift the number to the right
			r.append( i )
		
		r.append( integer ) # don't forget the last part
		r.reverse()
		return r

	def byteListToInt(self, byteList ):
		""" """
		r = 0
		for i in byteList: r = (r << 8) + i
		return r


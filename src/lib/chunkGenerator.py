""" """

class ChunkGenerator( object ):
	""" """

	def __init__(self, encoder, playerFactory, blockTypeFactory, chunkSize):
		""" """

		from playerFactory import PlayerFactory
		from blockTypeFactory import BlockTypeFactory
		from encoder import Encoder

		if not isinstance( playerFactory, PlayerFactory ): raise TypeError( playerFactory )
		if not isinstance( blockTypeFactory, BlockTypeFactory ): raise TypeError( blockTypeFactory )
		if not isinstance( encoder, Encoder ): raise TypeError( encoder )
		if not isinstance( chunkSize, int ): raise TypeError( chunkSize )

		super( ChunkGenerator, self ).__init__()

		self.encoder = encoder
		self.blockTypeFactory = blockTypeFactory
		self.playerFactory = playerFactory
		self.chunkSize = chunkSize

		return None

	def generate(self, fileObj, position):
		""" """
		
		# for now just fill it with air.
		air = self.blockTypeFactory.fromName( 'air' )
		owner = self.playerFactory.fromName('__WORLD__')
		airBlock = air.newBlock( owner )
		representation = self.encoder.encodeBlock( airBlock )

		if not fileObj.exists(): fileObj.create()
		fileObj.open()

		count = 0
		while count < self.chunkSize ** 3:
			fileObj.write( representation )
			count += 1

		fileObj.close()

		return None


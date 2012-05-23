""" """

from lib.playerFactory import PlayerFactory
from factories.setup import Setup
from factories.config import ConfigSetup

class PlayerFactorySetup( Setup ):
	''' '''

	objectsText = [ '#comment'
			, '[__WORLD__]'
			, 'hp = 100'
			, '[Jhon]'
			, 'hp = 100'
			, '[Smith]'
			, 'hp = 100'
			]
	idsText = [ '# the id\'s of the blocks above.'
			, '[ids]'
			, '__WORLD__=0'
			, 'Jhon=1'
			, 'Smith=1'
			]

	@classmethod
	def create(cls, objectsConfig=None, idsConfig=None):
		''' '''
		objectsConfig = objectsConfig or cls.createObjectsConfig()
		idsConfig = idsConfig or cls.createIdsConfig()
		playerFactory = PlayerFactory( objectsConfig, idsConfig )
		playerFactory.process()
		return playerFactory

	@classmethod
	def prepare(cls): return cls.createObjectsConfig(), cls.createIdsConfig()

	@classmethod
	def createObjectsConfig(cls): return ConfigSetup.create( * cls.objectsText )

	@classmethod
	def createIdsConfig(cls): return ConfigSetup.create( * cls.idsText )


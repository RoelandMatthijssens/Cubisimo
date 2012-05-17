""" """

from lib.playerFactory import PlayerFactory
from mocks.config import ConfigMock

class PlayerFactoryMock( PlayerFactory ):
	''' '''

	def __init__(self, objectConfig=None, idsConfig=None ):
		''' '''
		objectsConfig = objectConfig or self.createObjectConf()
		idsConfig = idsConfig or self.createIdsConf()
		super( PlayerFactoryMock, self ).__init__(objectsConfig, idsConfig)
		return None

	def createObjectConf(self):
		return ConfigMock( '#comment'
				, '[__WORLD__]'
				, 'hp = 100'
				, '[Jhon]'
				, 'hp = 100'
				, '[Smith]'
				, 'hp = 100'
				)

	def createIdsConf(self):
		idsConfig = ConfigMock( '# the id\'s of the blocks above.'
				, '[ids]'
				, '__WORLD__=0'
				, 'Jhon=1'
				, 'Smith=1'
				)


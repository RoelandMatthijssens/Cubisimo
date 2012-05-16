""" """

from math import ceil

class Factory( object ):
	""" """

	def __init__(self, objectConfig, idConfig):
		"""  """

		super( Factory, self ).__init__()
		self.objectConfig = objectConfig
		self.idConfig = idConfig
		self.objects = {}
		self.ids = {}

		return None

	def __bool__(self): return bool( self.objects )

	def fromName(self, name): return self.objects[name]
	def fromId(self, identifier): return self.fromName( self.ids[identifier] )
	def idSize(self): return int( ceil( len( self.ids ) / float(2 << 7) ) )

	def createInstance(self, identifier, name, values): raise NotImplementedError

	def process(self):
		""" """

		for name, values in self.objectConfig.items():
			if not name in self.idConfig['ids']:
				raise Exception('Object could not be found in idConfig.', name, self.idConfig['ids'])
			identifier = self.idConfig['ids'][name]
			obj = self.createInstance( identifier, name, values )
			self.objects[ name ] = obj

		for name, identifier in self.idConfig['ids'].items():
			if not name in self.objects:
				raise Exception('Object\'s name could not be found.')
			self.ids[ identifier ] = name

		return None



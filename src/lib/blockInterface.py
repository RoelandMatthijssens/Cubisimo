''' '''

class BlockIF( object ):
	''' '''

	def __init__(self): return super(BlockIF, self).__init__()

	def damage(self, amount, item): raise NotImplementedError
	def create(self, environment): raise NotImplementedError
	def load( self, environment): raise NotImplementedError
	def unload(self): raise NotImplementedError
	def destroy(self): raise NotImplementedError

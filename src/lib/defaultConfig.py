""" """

from config import Config

class DefaultConfig( Config ):
	""" """

	def __init__(self, fileObj, **defaultValues):
		""" """
		
		super( DefaultConfig, self ).__init__( fileObj )
		self.defaults = defaultValues
		self.update( defaultValues )
		return None

	def __setitem__(self, key, value):
		""" """
		if 'ALL' in self.defaults or key in self.defaults:
			# even if we are resetting the key to a new dictionary we should still put in
			# the default values; put in the defaults first so they are overwriten by what
			# is in value.
			d = dict()
			# either one of the following should happen, maybe even both, but we don't
			# know which ones.
			if 'ALL' in self.defaults: d.update( self.defaults['ALL'] )
			if key in self.defaults: d.update( self.defaults[ key ] )
			d.update( value )
			super(DefaultConfig, self).__setitem__(key, d )
		else: super(DefaultConfig, self).__setitem__(key,value)
		return None


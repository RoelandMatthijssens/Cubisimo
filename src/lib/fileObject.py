""" """

from panda3d.core import Filename
from baseFileObject import BaseFileObject
from os import path

class FileObject( BaseFileObject ):
	""" """

	def __init__(self, filename):
		""" """

		if not type( filename ) == Filename: raise TypeError( filename )

		super(FileObject, self).__init__()

		self.filename = filename
		self.fp = None

		return None

	def open(self, mode='rw+b'):
		""" """
		if not self.closed: return None

		try: self.fp = open( self.filename.toOsSpecific(), mode )
		# if there is an error figure out what to do later.
		except IOError, e: raise e
		else: self.closed = False

		return None

	def close(self):
		""" """
		if self.closed: return None

		self.fp.close()
		self.closed = True
		return None

	def exists(self): return path.isfile( self.filename.toOsSpecific() )
	def create(self):
		""" """
		if self.exists(): return None
		self.open( 'w+b' )
		self.close()
		return None

	def __iter__(self): return self.fp.__iter__()

	def __del__(self):
		self.close()
		# object does not have a __del__ method?
		# super( FileObject, self ).__del__()
		return None


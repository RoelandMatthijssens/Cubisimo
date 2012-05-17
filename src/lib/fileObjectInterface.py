""" """

class FileObjectIF( object ):
	""" """

	def open(self, mode=None): raise NotImplementedError
	def read(self, amount): raise NotImplementedError
	def readlines(self): raise NotImplementedError
	def readline(self): raise NotImplementedError
	def write(self, value): raise NotImplementedError
	def writelines(self, value): raise NotImplementedError
	def close(self): raise NotImplementedError
	def seek(self, index): raise NotImplementedError
	def insert(self, index): raise NotImplementedError

	def exists(self): raise NotImplementedError
	def create(self): raise NotImplementedError

	def __iter__(self): raise NotImplementedError


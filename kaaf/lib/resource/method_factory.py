from lib.http_methods.get import Get
from lib.http_methods.post import Post
from lib.http_methods.put import Put
from lib.http_methods.delete import Delete

class MethodFactory(object):

	def __init__(self):
		self.method = None
		self.ret_method = None

	@classmethod
	def get_method(self, method):

		self.method = method
		
		if self.method == 'get':
			self.ret_method = Get()

		if self.method == 'post':
			self.ret_method = Post()

		if self.method == 'put':
			self.ret_method = Put()

		if self.method == 'delete':
			self.ret_method = Delete()

		return self.ret_method				


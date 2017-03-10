

import sys
sys.path.append("/Users/ankitsahu/Documents/kaaf/")

import subprocess
from config.config import Config
from lib.resource.method_factory import MethodFactory

try:
	import requests
except:
	subprocess.call(["pip3", "install" , "requests"])
	import requests	

class Resource(object):

	def __init__(self):
		self.req = None
		self.resp = None
		self.method = None

	@classmethod
	def send_request(self, method_type, url=None, realtive_url=None, param=None, data=None, headers=None):

		self.method = MethodFactory.get_method(method_type)
		self.resp = self.method.make_request(url,realtive_url, param=param, headers=headers, data=data)
		return self.resp



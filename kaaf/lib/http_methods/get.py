import requests
from config.config import Config


class Get(object):

	def __init__(self):
		pass

	@classmethod
	def make_request(self, url, realtive_url=None, param=None, headers=None):
		
		if realtive_url == None:
			final_url = url
		else:
			final_url = Config.url + relative_url
		return requests.get(final_url, params=param, headers=headers)
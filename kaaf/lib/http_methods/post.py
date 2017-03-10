import requests

class Post(object):

	@classmethod
	def make_request(self, url, realtive_url=None, param=None, data=None, headers=None):
		
		if realtive_url == None:
			final_url = url
		else:
			final_url = Config.url + relative_url
		return requests.post(final_url, params=param, data=data, headers=headers)
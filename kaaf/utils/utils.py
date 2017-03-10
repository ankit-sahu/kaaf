

class Utils(object):
	

	@classmethod
	def sort_json(self,json_obj):

		if isinstance(json_obj, dict):
			return sorted((key , self.sort_json(value)) for key, value in json_obj.items())
		if isinstance(json_obj, list):
			return sorted(self.sort_json(x) for x in json_obj)
		else:
			return json_obj			
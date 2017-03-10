
import sys
sys.path.append("/Users/ankitsahu/Documents/kaaf/")

from ddt import ddt,unpack,data
import unittest

from lib.base_test import BaseTest
from lib.resource.resource import Resource
from config.config import Config
from utils.utils import Utils
from utils.data_ref import DataRef
from lib.logger import LogObject

# @ddt
class Login(BaseTest):

	# @data(*DataRef.read('login'))
	# @unpack
	# def test_login(self, *value):
	# 	key = DataRef.read_keys('login')
	# 	payload = {key[0] : value[0], key[1] : value[1]}
	# 	response = Resource.send_request('post', Config.url, data=payload)
	# 	res_body = response.json()
	# 	print(res_body['data']['id'])
	# 	self.assertEquals(response.status_code, value[2])
	# 	self.assertEquals(res_body['data']['id'], str(int(value[3])))
	# 	self.assertEquals(res_body['data']['type'], value[4])
	# 	self.assertEquals(res_body['data']['attributes']['email'], value[5])
	# 	self.assertEquals(res_body['data']['attributes']['first_name'], value[6])
	# 	self.assertEquals(res_body['data']['attributes']['last_name'], value[7])
	# 	self.assertEquals(res_body['data']['attributes']['job_title'], value[8])
	# 	self.assertEquals(res_body['data']['attributes']['based_city'], value[9])


	

	# @data((1,1),(1,2),(1,3))
	# @unpack
	# def test_sample1(self,a,b):
	# 	log.info("what's up")
	# 	self.assertEquals(a,b)

	def __init__(self, *args, **kwargs):
		BaseTest.__init__(self, *args, **kwargs)
		self.logger = LogObject.get_logger('Login')

	def test_sample2(self):

		
		self.logger.info('try hard')
		self.assertEquals(1,1)

	# def test_sample3(self):
	# 	self.assertEquals('a', 3)		

import logging

class Logger(object):

	def __init__(self):
		self.logger = None
		self.file_handler = None
		self.console_handler = None
		self.formatter = None

	def set_logger(self,logname):
		self.logger = logging.getLogger(logname)


	def set_file_handler(self, file_name):
		self.file_handler = 	logging.FileHandler(file_name)
		self.file_handler.setLevel(logging.INFO)
		self.formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
		self.file_handler.setFormatter(self.formatter)

	def set_console_logging(self):
		self.console_handler = logging.StreamHandler()
		self.console_handler.setLevel(logging.INFO)
		self.formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
		self.console_handler.setFormatter(self.formatter)
		

	def init_logger(self):	
		self.logger.addHandler(self.file_handler)
		self.logger.addHandler(self.console_handler)
		return self.logger
		

class LogObject(object):

	@classmethod
	def get_logger(self, class_name):
		log = Logger()
		log.set_logger(class_name)
		log.set_file_handler("/Users/ankitsahu/Documents/kaaf/sample.txt" )
		log.set_console_logging()
		print(log.init_logger())
		return log.init_logger()
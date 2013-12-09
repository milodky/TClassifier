from classifier import Classifier

class RawClassifier(object):
	def __init__(self):
		self.classifier = Classifier()
	def ClassifyHandler(self, args):
		self.classifier.validate(args)
		result = self.classifier.execute()
		if result > 0.5:
			return args[3]
		else:
			return args[4]
	def SFHandler(self, data):
		args = ['bayes.py', 'classify', data, 'sports', 'finance']
		result = self.ClassifyHandler(args)
		return result
	def FinalHandler(self, data):
		cate = self.SFHandler(data)
		args = ['bayes.py', 'classify', data, 'personal', cate]
		result = self.ClassifyHandler(args)
		return result

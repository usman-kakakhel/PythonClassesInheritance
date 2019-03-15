from Question import Question

class TrueFalseQuestion(Question):
	def __init__(self, question, answer, score, incorrectPoints):
		super().__init__(question, answer, score)
		self.__incorrectPoints = incorrectPoints


	def scoreQueston(self):
		return super.scoreQuestion() - incorrectPoints

	def displayQuestion(self):
		print ("True or False: ")
		super().displayQuestion()



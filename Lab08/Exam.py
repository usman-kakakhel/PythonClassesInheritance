from Question import Question
from TrueFalseQuestion import TrueFalseQuestion

def initializeQuestions(myFile, myList):
	for x in myFile:
		next = x.find(";")
		type = x[ : next]
		pre = next + 1
		next = x.find(";", pre)
		question = x[pre : next]
		pre = next + 1
		next = x.find(";", pre)
		answer = x[pre : next]
		pre = next + 1
		next = x.find(";", pre)
		score = x[pre : next]
		if (type == "T"):
			pre = next + 1
			next = x.find(";", pre)
			incorrectPoints = x[pre : next]
			myList.append(TrueFalseQuestion(question, answer, score, incorrectPoints))
		elif (type == "R"):
			myList.append(Question(question, answer, score))
	return myList

def gradeExam(myList):
	print("********Grading Exam*********")
	score = 0
	fScore = 0
	for x in myList:
		fScore = fScore + x.getScore()
		score = score + x.scoreQuestion()		
		if (x.scoreQuestion() <= 0):
			print("Incorrect Answer!")
			print(x)
			print()


	print("********End Of Grading*********")
	print("Your Score Is: {}/{}".format(score,fScore))


myFile = open("questions.txt", "r")
myList = []

myList = initializeQuestions(myFile, myList)

myFile.close()
for x in myList:
	x.displayQuestion()
	x.answerQuestion(input("Enter Choice: "))

gradeExam(myList)

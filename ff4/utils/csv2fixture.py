#!/usr/bin/env python
import csv, json, sys

if len(sys.argv) > 1:
    csvFile = sys.argv[1]
else:
    print "Error: Please specify a csv file"
    exit()

class QuizQuestion:
    """FF4 Quiz Item"""
    pk = 0
    question = "question"
    model = "things.QuizQuestion"
    fixture = ''
    answers = list()
    def __init__(self, pk, question):
        self.pk = pk
        self.question = question
    def addQuestion(self, question):
        self.answers.append(question)
    def getFixture(self):
        self.fixture = ''
        self.fixture += "- fields: { question_en: \"" + self.question + "\" }\n"
        self.fixture += "  model: " + self.model + "\n"
        self.fixture += "  pk: " + str(self.pk) + "\n"
        return self.fixture

class QuizAnswer:
    pk = 0
    question = 0
    answer = "answer"
    model = "things.QuizAnswer"
    images = list()
    def __init__(self, pk, answer, question):
        self.pk = pk
        self.answer = answer
        self.question = question
    def addImage(self, image):
        self.images.append(image)
    def getFixture(self):
        self.fixture = ''
        self.fixture += "- fields: { answer_en: \"" + self.answer + "\", quiz_question: " + str(self.question) + ", slug: \"" + str(self.pk) + "\" }\n"
        self.fixture += "  model: " + self.model + "\n"
        self.fixture += "  pk: " + str(self.pk) + "\n"
        return self.fixture

class QuizAnswerByImage:
    """FF4 QuizAnswerByImage"""
    pk = 0
    answer = 0
    image = 0
    slug = "name"
    tooltip = "tooltip"
    model = "things.QuizAnswerByImage"
    def __init__(self, pk, image, answer, tooltip):
        self.image = image
        self.answer = answer
        self.pk = pk
        self.tooltip = tooltip
    def getFixture(self):
        self.fixture = ''
        self.fixture += "- fields: { image: " + str(self.image) + ", answer: " + str(self.answer) + ", tooltip_en: \"" + self.tooltip + "\" }\n"
        self.fixture += "  model: " + self.model + "\n"
        self.fixture += "  pk: " + str(self.pk) + "\n"
        return self.fixture
        
class Image:
    pk = 0
    file_name = "file.jpg"
    name = "image name"
    model = "things.Image"
    images = list()
    def __init__(self, pk, filename, name):
        self.pk = pk
        self.file_name = filename
        self.name = name
    def getFixture(self):
        self.fixture = ''
        self.fixture += "- fields: { file_name: \"" + self.file_name + "\", name_en: \"" + self.name + "\", slug: \"" + str(self.file_name) + "\" }\n"
        self.fixture += "  model: " + self.model + "\n"
        self.fixture += "  pk: " + str(self.pk) + "\n"
        return self.fixture

myCSV = csv.reader(open(csvFile, 'rb'), delimiter=',')

questionList = list()
answerList = list()
answerByImageList = list()
imagesList = {}

# why would i do this this way?
questionCounter = 1
answerCounter = 1
imageCounter = 1

# first, we need to get and ID all our images
for i in myCSV:
    if i[2] != '':
        if i[4].rstrip().lower() not in imagesList:
            imagesList[i[4].rstrip().lower()] = Image(len(imagesList)+1, i[4].rstrip().lower(), i[2].rstrip())

# next we need to loop through and build queries for all our stuff
myCSV = csv.reader(open(csvFile, 'rb'), delimiter=',')

question = None
answer = None

for i in myCSV:
    if i[0].rstrip() != '':
        question = QuizQuestion(questionCounter, i[0])
        questionList.append(question)
        questionCounter += 1
    elif i[1].rstrip() != '':
        answer = QuizAnswer(answerCounter, i[1], question.pk)
        answerList.append(answer)
        question.addQuestion(answer)
        answerCounter += 1
    elif i[2].rstrip() != '':
        if i[4].rstrip().lower() in imagesList:
            image = imagesList[i[4].rstrip().lower()]
            answerByImageList.append(QuizAnswerByImage(imageCounter, image.pk, answer.pk, i[3]))
            imageCounter += 1

# output our quiz_questions fixtures
f = open('./quiz_questions.yaml', 'w')
for q in questionList:
    f.write(q.getFixture())
    
# output our quiz_answers fixtures
f = open('./quiz_answers.yaml', 'w')
for a in answerList:
    f.write(a.getFixture())
    
# output our quizanswer_by_image file
f = open('./quizanswer_by_image.yaml', 'w')
for abi in answerByImageList:
    f.write(abi.getFixture())
    
# output our images file
f = open('./images.yaml', 'w')
for k,i in imagesList.items():
    f.write(i.getFixture())
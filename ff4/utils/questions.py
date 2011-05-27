from django.core import serializers
import json
from things.models import QuizQuestion, QuizAnswer


# get the question and answers in json formatin JSON format
def get_question_JSON(qid):
    q = QuizQuestion.objects.filter(id=qid)
    a = QuizAnswer.objects.filter(quiz_question=q[0].pk)
    qa = list(a) + list(q)
    data = serializers.serialize('json', qa)
    return data


def serialize_image_list(images):
    imageObj = {}
    c = 0
    for image in images:
        imageObj[c] = {'img': image.file_name, 'width': 0, 'height': 0, 'name': image.slug, 'description': 'blah blah blah'}
    return imageObj

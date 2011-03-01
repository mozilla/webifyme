from dbgettext.registry import registry, Options
from dbgettext.lexicons import html

from ff4.things.models import QuizQuestion, QuizAnswer, Image, QuizAnswerByImage

class QuizQuestionOptions(Options):
    attributes = ('question',)
    parsed_attributes = {'question': html.lexicon}

registry.register(QuizQuestion, QuizQuestionOptions)

class QuizAnswerOptions(Options):
    attributes = ('answer',)
    parsed_attributes = {'answer': html.lexicon}

registry.register(QuizAnswer, QuizAnswerOptions)

class ImageOptions(Options):
    attributes = ('name',)
    parsed_attributes = {'name': html.lexicon}

registry.register(Image, ImageOptions)

class QuizAnswerByImageOptions(Options):
    attributes = ('tooltip',)
    parsed_attributes = {'tooltip': html.lexicon}

registry.register(QuizAnswerByImage, QuizAnswerByImageOptions)


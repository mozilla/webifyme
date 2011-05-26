# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Renaming field QuizAnswerByImage.tooltip_en to QuizAnswerByImage.tooltip
        db.rename_column('things_quizanswerbyimage', 'tooltip_en', 'tooltip')

        # Deleting field 'QuizAnswerByImage.tooltip_sr'
        db.delete_column('things_quizanswerbyimage', 'tooltip_sr')

        # Deleting field 'QuizAnswerByImage.tooltip_zh-cn'
        db.delete_column('things_quizanswerbyimage', 'tooltip_zh-cn')

        # Deleting field 'QuizAnswerByImage.tooltip_bg'
        db.delete_column('things_quizanswerbyimage', 'tooltip_bg')

        # Deleting field 'QuizAnswerByImage.tooltip_bn'
        db.delete_column('things_quizanswerbyimage', 'tooltip_bn')

        # Deleting field 'QuizAnswerByImage.tooltip_hu'
        db.delete_column('things_quizanswerbyimage', 'tooltip_hu')

        # Deleting field 'QuizAnswerByImage.tooltip_sr-latn'
        db.delete_column('things_quizanswerbyimage', 'tooltip_sr-latn')

        # Deleting field 'QuizAnswerByImage.tooltip_bs'
        db.delete_column('things_quizanswerbyimage', 'tooltip_bs')

        # Deleting field 'QuizAnswerByImage.tooltip_zh-tw'
        db.delete_column('things_quizanswerbyimage', 'tooltip_zh-tw')

        # Deleting field 'QuizAnswerByImage.tooltip_sq'
        db.delete_column('things_quizanswerbyimage', 'tooltip_sq')

        # Deleting field 'QuizAnswerByImage.tooltip_nl'
        db.delete_column('things_quizanswerbyimage', 'tooltip_nl')

        # Deleting field 'QuizAnswerByImage.tooltip_sv'
        db.delete_column('things_quizanswerbyimage', 'tooltip_sv')

        # Deleting field 'QuizAnswerByImage.tooltip_nn'
        db.delete_column('things_quizanswerbyimage', 'tooltip_nn')

        # Deleting field 'QuizAnswerByImage.tooltip_he'
        db.delete_column('things_quizanswerbyimage', 'tooltip_he')

        # Deleting field 'QuizAnswerByImage.tooltip_es-ar'
        db.delete_column('things_quizanswerbyimage', 'tooltip_es-ar')

        # Deleting field 'QuizAnswerByImage.tooltip_fr'
        db.delete_column('things_quizanswerbyimage', 'tooltip_fr')

        # Deleting field 'QuizAnswerByImage.tooltip_kn'
        db.delete_column('things_quizanswerbyimage', 'tooltip_kn')

        # Deleting field 'QuizAnswerByImage.tooltip_uk'
        db.delete_column('things_quizanswerbyimage', 'tooltip_uk')

        # Deleting field 'QuizAnswerByImage.tooltip_pl'
        db.delete_column('things_quizanswerbyimage', 'tooltip_pl')

        # Deleting field 'QuizAnswerByImage.tooltip_nb'
        db.delete_column('things_quizanswerbyimage', 'tooltip_nb')

        # Deleting field 'QuizAnswerByImage.tooltip_hi'
        db.delete_column('things_quizanswerbyimage', 'tooltip_hi')

        # Deleting field 'QuizAnswerByImage.tooltip_pt-br'
        db.delete_column('things_quizanswerbyimage', 'tooltip_pt-br')

        # Deleting field 'QuizAnswerByImage.tooltip_da'
        db.delete_column('things_quizanswerbyimage', 'tooltip_da')

        # Deleting field 'QuizAnswerByImage.tooltip_hr'
        db.delete_column('things_quizanswerbyimage', 'tooltip_hr')

        # Deleting field 'QuizAnswerByImage.tooltip_fa'
        db.delete_column('things_quizanswerbyimage', 'tooltip_fa')

        # Deleting field 'QuizAnswerByImage.tooltip_de'
        db.delete_column('things_quizanswerbyimage', 'tooltip_de')

        # Deleting field 'QuizAnswerByImage.tooltip_ja'
        db.delete_column('things_quizanswerbyimage', 'tooltip_ja')

        # Deleting field 'QuizAnswerByImage.tooltip_sl'
        db.delete_column('things_quizanswerbyimage', 'tooltip_sl')

        # Deleting field 'QuizAnswerByImage.tooltip_lv'
        db.delete_column('things_quizanswerbyimage', 'tooltip_lv')

        # Deleting field 'QuizAnswerByImage.tooltip_fi'
        db.delete_column('things_quizanswerbyimage', 'tooltip_fi')

        # Deleting field 'QuizAnswerByImage.tooltip_lt'
        db.delete_column('things_quizanswerbyimage', 'tooltip_lt')

        # Deleting field 'QuizAnswerByImage.tooltip_te'
        db.delete_column('things_quizanswerbyimage', 'tooltip_te')

        # Deleting field 'QuizAnswerByImage.tooltip_ca'
        db.delete_column('things_quizanswerbyimage', 'tooltip_ca')

        # Deleting field 'QuizAnswerByImage.tooltip_gl'
        db.delete_column('things_quizanswerbyimage', 'tooltip_gl')

        # Deleting field 'QuizAnswerByImage.tooltip_ga'
        db.delete_column('things_quizanswerbyimage', 'tooltip_ga')

        # Deleting field 'QuizAnswerByImage.tooltip_ru'
        db.delete_column('things_quizanswerbyimage', 'tooltip_ru')

        # Deleting field 'QuizAnswerByImage.tooltip_mk'
        db.delete_column('things_quizanswerbyimage', 'tooltip_mk')

        # Deleting field 'QuizAnswerByImage.tooltip_tr'
        db.delete_column('things_quizanswerbyimage', 'tooltip_tr')

        # Deleting field 'QuizAnswerByImage.tooltip_no'
        db.delete_column('things_quizanswerbyimage', 'tooltip_no')

        # Deleting field 'QuizAnswerByImage.tooltip_cs'
        db.delete_column('things_quizanswerbyimage', 'tooltip_cs')

        # Deleting field 'QuizAnswerByImage.tooltip_cy'
        db.delete_column('things_quizanswerbyimage', 'tooltip_cy')

        # Deleting field 'QuizAnswerByImage.tooltip_ar'
        db.delete_column('things_quizanswerbyimage', 'tooltip_ar')

        # Deleting field 'QuizAnswerByImage.tooltip_id'
        db.delete_column('things_quizanswerbyimage', 'tooltip_id')

        # Deleting field 'QuizAnswerByImage.tooltip_es'
        db.delete_column('things_quizanswerbyimage', 'tooltip_es')

        # Deleting field 'QuizAnswerByImage.tooltip_ta'
        db.delete_column('things_quizanswerbyimage', 'tooltip_ta')

        # Deleting field 'QuizAnswerByImage.tooltip_eu'
        db.delete_column('things_quizanswerbyimage', 'tooltip_eu')

        # Deleting field 'QuizAnswerByImage.tooltip_et'
        db.delete_column('things_quizanswerbyimage', 'tooltip_et')

        # Deleting field 'QuizAnswerByImage.tooltip_ml'
        db.delete_column('things_quizanswerbyimage', 'tooltip_ml')

        # Deleting field 'QuizAnswerByImage.tooltip_sk'
        db.delete_column('things_quizanswerbyimage', 'tooltip_sk')

        # Deleting field 'QuizAnswerByImage.tooltip_pt'
        db.delete_column('things_quizanswerbyimage', 'tooltip_pt')

        # Deleting field 'QuizAnswerByImage.tooltip_mn'
        db.delete_column('things_quizanswerbyimage', 'tooltip_mn')

        # Deleting field 'QuizAnswerByImage.tooltip_vi'
        db.delete_column('things_quizanswerbyimage', 'tooltip_vi')

        # Deleting field 'QuizAnswerByImage.tooltip_ko'
        db.delete_column('things_quizanswerbyimage', 'tooltip_ko')

        # Deleting field 'QuizAnswerByImage.tooltip_it'
        db.delete_column('things_quizanswerbyimage', 'tooltip_it')

        # Deleting field 'QuizAnswerByImage.tooltip_km'
        db.delete_column('things_quizanswerbyimage', 'tooltip_km')

        # Deleting field 'QuizAnswerByImage.tooltip_fy-nl'
        db.delete_column('things_quizanswerbyimage', 'tooltip_fy-nl')

        # Deleting field 'QuizAnswerByImage.tooltip_is'
        db.delete_column('things_quizanswerbyimage', 'tooltip_is')

        # Deleting field 'QuizAnswerByImage.tooltip_th'
        db.delete_column('things_quizanswerbyimage', 'tooltip_th')

        # Deleting field 'QuizAnswerByImage.tooltip_ro'
        db.delete_column('things_quizanswerbyimage', 'tooltip_ro')

        # Deleting field 'QuizAnswerByImage.tooltip_en-gb'
        db.delete_column('things_quizanswerbyimage', 'tooltip_en-gb')

        # Deleting field 'QuizAnswerByImage.tooltip_el'
        db.delete_column('things_quizanswerbyimage', 'tooltip_el')

        # Deleting field 'QuizAnswerByImage.tooltip_ka'
        db.delete_column('things_quizanswerbyimage', 'tooltip_ka')

        # Deleting field 'QuizAnswerByImage.tooltip_en'
        #db.delete_column('things_quizanswerbyimage', 'tooltip_en')

        # Adding field 'QuizAnswerByImage.tooltip'
        #db.add_column('things_quizanswerbyimage', 'tooltip', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True), keep_default=False)

        # Renaming QuizAnswer.answer_en to QuizAnswer.answer
        db.rename_column('things_quizanswer', 'answer_en', 'answer')

        # Deleting field 'QuizAnswer.answer_bn'
        db.delete_column('things_quizanswer', 'answer_bn')

        # Deleting field 'QuizAnswer.answer_ru'
        db.delete_column('things_quizanswer', 'answer_ru')

        # Deleting field 'QuizAnswer.answer_pt-br'
        db.delete_column('things_quizanswer', 'answer_pt-br')

        # Deleting field 'QuizAnswer.answer_uk'
        db.delete_column('things_quizanswer', 'answer_uk')

        # Deleting field 'QuizAnswer.answer_bg'
        db.delete_column('things_quizanswer', 'answer_bg')

        # Deleting field 'QuizAnswer.answer_de'
        db.delete_column('things_quizanswer', 'answer_de')

        # Deleting field 'QuizAnswer.answer_zh-cn'
        db.delete_column('things_quizanswer', 'answer_zh-cn')

        # Deleting field 'QuizAnswer.answer_te'
        db.delete_column('things_quizanswer', 'answer_te')

        # Deleting field 'QuizAnswer.answer_bs'
        db.delete_column('things_quizanswer', 'answer_bs')

        # Deleting field 'QuizAnswer.answer_en-gb'
        db.delete_column('things_quizanswer', 'answer_en-gb')

        # Deleting field 'QuizAnswer.answer_fr'
        db.delete_column('things_quizanswer', 'answer_fr')

        # Deleting field 'QuizAnswer.answer_th'
        db.delete_column('things_quizanswer', 'answer_th')

        # Deleting field 'QuizAnswer.answer_ta'
        db.delete_column('things_quizanswer', 'answer_ta')

        # Deleting field 'QuizAnswer.answer_nn'
        db.delete_column('things_quizanswer', 'answer_nn')

        # Deleting field 'QuizAnswer.answer_no'
        db.delete_column('things_quizanswer', 'answer_no')

        # Deleting field 'QuizAnswer.answer_nl'
        db.delete_column('things_quizanswer', 'answer_nl')

        # Deleting field 'QuizAnswer.answer_ja'
        db.delete_column('things_quizanswer', 'answer_ja')

        # Deleting field 'QuizAnswer.answer_nb'
        db.delete_column('things_quizanswer', 'answer_nb')

        # Deleting field 'QuizAnswer.answer_hu'
        db.delete_column('things_quizanswer', 'answer_hu')

        # Deleting field 'QuizAnswer.answer_sv'
        db.delete_column('things_quizanswer', 'answer_sv')

        # Deleting field 'QuizAnswer.answer_sq'
        db.delete_column('things_quizanswer', 'answer_sq')

        # Deleting field 'QuizAnswer.answer_hr'
        db.delete_column('things_quizanswer', 'answer_hr')

        # Deleting field 'QuizAnswer.answer_sr'
        db.delete_column('things_quizanswer', 'answer_sr')

        # Deleting field 'QuizAnswer.answer_sl'
        db.delete_column('things_quizanswer', 'answer_sl')

        # Deleting field 'QuizAnswer.answer_fa'
        db.delete_column('things_quizanswer', 'answer_fa')

        # Deleting field 'QuizAnswer.answer_lt'
        db.delete_column('things_quizanswer', 'answer_lt')

        # Deleting field 'QuizAnswer.answer_hi'
        db.delete_column('things_quizanswer', 'answer_hi')

        # Deleting field 'QuizAnswer.answer_lv'
        db.delete_column('things_quizanswer', 'answer_lv')

        # Deleting field 'QuizAnswer.answer_da'
        db.delete_column('things_quizanswer', 'answer_da')

        # Deleting field 'QuizAnswer.answer_he'
        db.delete_column('things_quizanswer', 'answer_he')

        # Deleting field 'QuizAnswer.answer_fi'
        db.delete_column('things_quizanswer', 'answer_fi')

        # Deleting field 'QuizAnswer.answer_tr'
        db.delete_column('things_quizanswer', 'answer_tr')

        # Deleting field 'QuizAnswer.answer_sk'
        db.delete_column('things_quizanswer', 'answer_sk')

        # Deleting field 'QuizAnswer.answer_sr-latn'
        db.delete_column('things_quizanswer', 'answer_sr-latn')

        # Deleting field 'QuizAnswer.answer_ml'
        db.delete_column('things_quizanswer', 'answer_ml')

        # Deleting field 'QuizAnswer.answer_ca'
        db.delete_column('things_quizanswer', 'answer_ca')

        # Deleting field 'QuizAnswer.answer_fy-nl'
        db.delete_column('things_quizanswer', 'answer_fy-nl')

        # Deleting field 'QuizAnswer.answer_ar'
        db.delete_column('things_quizanswer', 'answer_ar')

        # Deleting field 'QuizAnswer.answer_et'
        db.delete_column('things_quizanswer', 'answer_et')

        # Deleting field 'QuizAnswer.answer_cy'
        db.delete_column('things_quizanswer', 'answer_cy')

        # Deleting field 'QuizAnswer.answer_ro'
        db.delete_column('things_quizanswer', 'answer_ro')

        # Deleting field 'QuizAnswer.answer_ka'
        db.delete_column('things_quizanswer', 'answer_ka')

        # Deleting field 'QuizAnswer.answer_vi'
        db.delete_column('things_quizanswer', 'answer_vi')

        # Deleting field 'QuizAnswer.answer_cs'
        db.delete_column('things_quizanswer', 'answer_cs')

        # Deleting field 'QuizAnswer.answer_zh-tw'
        db.delete_column('things_quizanswer', 'answer_zh-tw')

        # Deleting field 'QuizAnswer.answer_pt'
        db.delete_column('things_quizanswer', 'answer_pt')

        # Deleting field 'QuizAnswer.answer_mn'
        db.delete_column('things_quizanswer', 'answer_mn')

        # Deleting field 'QuizAnswer.answer_eu'
        db.delete_column('things_quizanswer', 'answer_eu')

        # Deleting field 'QuizAnswer.answer_es-ar'
        db.delete_column('things_quizanswer', 'answer_es-ar')

        # Deleting field 'QuizAnswer.answer_es'
        db.delete_column('things_quizanswer', 'answer_es')

        # Deleting field 'QuizAnswer.answer_is'
        db.delete_column('things_quizanswer', 'answer_is')

        # Deleting field 'QuizAnswer.answer_mk'
        db.delete_column('things_quizanswer', 'answer_mk')

        # Deleting field 'QuizAnswer.answer_ko'
        db.delete_column('things_quizanswer', 'answer_ko')

        # Deleting field 'QuizAnswer.answer_kn'
        db.delete_column('things_quizanswer', 'answer_kn')

        # Deleting field 'QuizAnswer.answer_it'
        db.delete_column('things_quizanswer', 'answer_it')

        # Deleting field 'QuizAnswer.answer_ga'
        db.delete_column('things_quizanswer', 'answer_ga')

        # Deleting field 'QuizAnswer.answer_km'
        db.delete_column('things_quizanswer', 'answer_km')

        # Deleting field 'QuizAnswer.answer_pl'
        db.delete_column('things_quizanswer', 'answer_pl')

        # Deleting field 'QuizAnswer.answer_en'
        #db.delete_column('things_quizanswer', 'answer_en')

        # Deleting field 'QuizAnswer.answer_el'
        db.delete_column('things_quizanswer', 'answer_el')

        # Deleting field 'QuizAnswer.answer_gl'
        db.delete_column('things_quizanswer', 'answer_gl')

        # Deleting field 'QuizAnswer.answer_id'
        db.delete_column('things_quizanswer', 'answer_id')

        # Adding field 'QuizAnswer.answer'
        #db.add_column('things_quizanswer', 'answer', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True), keep_default=False)

        # Renaming field 'Image.name_en' to 'Image.name'
        db.rename_column('things_image', 'name_en', 'name')

        # Deleting field 'Image.name_zh-cn'
        db.delete_column('things_image', 'name_zh-cn')

        # Deleting field 'Image.name_fr'
        db.delete_column('things_image', 'name_fr')

        # Deleting field 'Image.name_zh-tw'
        db.delete_column('things_image', 'name_zh-tw')

        # Deleting field 'Image.name_fa'
        db.delete_column('things_image', 'name_fa')

        # Deleting field 'Image.name_de'
        db.delete_column('things_image', 'name_de')

        # Deleting field 'Image.name_no'
        db.delete_column('things_image', 'name_no')

        # Deleting field 'Image.name_da'
        db.delete_column('things_image', 'name_da')

        # Deleting field 'Image.name_fi'
        db.delete_column('things_image', 'name_fi')

        # Deleting field 'Image.name_ml'
        db.delete_column('things_image', 'name_ml')

        # Deleting field 'Image.name_pl'
        db.delete_column('things_image', 'name_pl')

        # Deleting field 'Image.name_mn'
        db.delete_column('things_image', 'name_mn')

        # Deleting field 'Image.name_ca'
        db.delete_column('things_image', 'name_ca')

        # Deleting field 'Image.name_it'
        db.delete_column('things_image', 'name_it')

        # Deleting field 'Image.name_ta'
        db.delete_column('things_image', 'name_ta')

        # Deleting field 'Image.name_mk'
        db.delete_column('things_image', 'name_mk')

        # Deleting field 'Image.name_vi'
        db.delete_column('things_image', 'name_vi')

        # Deleting field 'Image.name_nb'
        db.delete_column('things_image', 'name_nb')

        # Deleting field 'Image.name_th'
        db.delete_column('things_image', 'name_th')

        # Deleting field 'Image.name_cs'
        db.delete_column('things_image', 'name_cs')

        # Deleting field 'Image.name_en-gb'
        db.delete_column('things_image', 'name_en-gb')

        # Deleting field 'Image.name_id'
        db.delete_column('things_image', 'name_id')

        # Deleting field 'Image.name_ko'
        db.delete_column('things_image', 'name_ko')

        # Deleting field 'Image.name_km'
        db.delete_column('things_image', 'name_km')

        # Deleting field 'Image.name_kn'
        db.delete_column('things_image', 'name_kn')

        # Deleting field 'Image.name_ro'
        db.delete_column('things_image', 'name_ro')

        # Deleting field 'Image.name_cy'
        db.delete_column('things_image', 'name_cy')

        # Deleting field 'Image.name_es-ar'
        db.delete_column('things_image', 'name_es-ar')

        # Deleting field 'Image.name_pt'
        db.delete_column('things_image', 'name_pt')

        # Deleting field 'Image.name_et'
        db.delete_column('things_image', 'name_et')

        # Deleting field 'Image.name_eu'
        db.delete_column('things_image', 'name_eu')

        # Deleting field 'Image.name_he'
        db.delete_column('things_image', 'name_he')

        # Deleting field 'Image.name_es'
        db.delete_column('things_image', 'name_es')

        # Deleting field 'Image.name_ar'
        db.delete_column('things_image', 'name_ar')

        # Deleting field 'Image.name_te'
        db.delete_column('things_image', 'name_te')

        # Deleting field 'Image.name_gl'
        db.delete_column('things_image', 'name_gl')

        # Deleting field 'Image.name_is'
        db.delete_column('things_image', 'name_is')

        # Deleting field 'Image.name_pt-br'
        db.delete_column('things_image', 'name_pt-br')

        # Deleting field 'Image.name_sk'
        db.delete_column('things_image', 'name_sk')

        # Deleting field 'Image.name_el'
        db.delete_column('things_image', 'name_el')

        # Deleting field 'Image.name_en'
        #db.delete_column('things_image', 'name_en')

        # Deleting field 'Image.name_sr-latn'
        db.delete_column('things_image', 'name_sr-latn')

        # Deleting field 'Image.name_ga'
        db.delete_column('things_image', 'name_ga')

        # Deleting field 'Image.name_sr'
        db.delete_column('things_image', 'name_sr')

        # Deleting field 'Image.name_hr'
        db.delete_column('things_image', 'name_hr')

        # Deleting field 'Image.name_bg'
        db.delete_column('things_image', 'name_bg')

        # Deleting field 'Image.name_ka'
        db.delete_column('things_image', 'name_ka')

        # Deleting field 'Image.name_sv'
        db.delete_column('things_image', 'name_sv')

        # Deleting field 'Image.name_nl'
        db.delete_column('things_image', 'name_nl')

        # Deleting field 'Image.name_hu'
        db.delete_column('things_image', 'name_hu')

        # Deleting field 'Image.name_nn'
        db.delete_column('things_image', 'name_nn')

        # Deleting field 'Image.name_bn'
        db.delete_column('things_image', 'name_bn')

        # Deleting field 'Image.name_fy-nl'
        db.delete_column('things_image', 'name_fy-nl')

        # Deleting field 'Image.name_ru'
        db.delete_column('things_image', 'name_ru')

        # Deleting field 'Image.name_sq'
        db.delete_column('things_image', 'name_sq')

        # Deleting field 'Image.name_uk'
        db.delete_column('things_image', 'name_uk')

        # Deleting field 'Image.name_bs'
        db.delete_column('things_image', 'name_bs')

        # Deleting field 'Image.name_lv'
        db.delete_column('things_image', 'name_lv')

        # Deleting field 'Image.name_hi'
        db.delete_column('things_image', 'name_hi')

        # Deleting field 'Image.name_lt'
        db.delete_column('things_image', 'name_lt')

        # Deleting field 'Image.name_ja'
        db.delete_column('things_image', 'name_ja')

        # Deleting field 'Image.name_tr'
        db.delete_column('things_image', 'name_tr')

        # Deleting field 'Image.name_sl'
        db.delete_column('things_image', 'name_sl')

        # Adding field 'Image.name'
        #db.add_column('things_image', 'name', self.gf('django.db.models.fields.CharField')(default='', max_length=100), keep_default=False)

        # Renaming field 'QuizQuestion.question_en' to 'QuizQuestion.question'
        db.rename_column('things_quizquestion', 'question_en', 'question')

        # Deleting field 'QuizQuestion.question_nn'
        db.delete_column('things_quizquestion', 'question_nn')

        # Deleting field 'QuizQuestion.question_no'
        db.delete_column('things_quizquestion', 'question_no')

        # Deleting field 'QuizQuestion.question_nl'
        db.delete_column('things_quizquestion', 'question_nl')

        # Deleting field 'QuizQuestion.question_kn'
        db.delete_column('things_quizquestion', 'question_kn')

        # Deleting field 'QuizQuestion.question_fr'
        db.delete_column('things_quizquestion', 'question_fr')

        # Deleting field 'QuizQuestion.question_en-gb'
        db.delete_column('things_quizquestion', 'question_en-gb')

        # Deleting field 'QuizQuestion.question_sr'
        db.delete_column('things_quizquestion', 'question_sr')

        # Deleting field 'QuizQuestion.question_bs'
        db.delete_column('things_quizquestion', 'question_bs')

        # Deleting field 'QuizQuestion.question_nb'
        db.delete_column('things_quizquestion', 'question_nb')

        # Deleting field 'QuizQuestion.question_ta'
        db.delete_column('things_quizquestion', 'question_ta')

        # Deleting field 'QuizQuestion.question_sv'
        db.delete_column('things_quizquestion', 'question_sv')

        # Deleting field 'QuizQuestion.question_bn'
        db.delete_column('things_quizquestion', 'question_bn')

        # Deleting field 'QuizQuestion.question_sr-latn'
        db.delete_column('things_quizquestion', 'question_sr-latn')

        # Deleting field 'QuizQuestion.question_fa'
        db.delete_column('things_quizquestion', 'question_fa')

        # Deleting field 'QuizQuestion.question_de'
        db.delete_column('things_quizquestion', 'question_de')

        # Deleting field 'QuizQuestion.question_vi'
        db.delete_column('things_quizquestion', 'question_vi')

        # Deleting field 'QuizQuestion.question_sk'
        db.delete_column('things_quizquestion', 'question_sk')

        # Deleting field 'QuizQuestion.question_fi'
        db.delete_column('things_quizquestion', 'question_fi')

        # Deleting field 'QuizQuestion.question_lt'
        db.delete_column('things_quizquestion', 'question_lt')

        # Deleting field 'QuizQuestion.question_lv'
        db.delete_column('things_quizquestion', 'question_lv')

        # Deleting field 'QuizQuestion.question_zh-cn'
        db.delete_column('things_quizquestion', 'question_zh-cn')

        # Deleting field 'QuizQuestion.question_th'
        db.delete_column('things_quizquestion', 'question_th')

        # Deleting field 'QuizQuestion.question_ro'
        db.delete_column('things_quizquestion', 'question_ro')

        # Deleting field 'QuizQuestion.question_pl'
        db.delete_column('things_quizquestion', 'question_pl')

        # Deleting field 'QuizQuestion.question_hr'
        db.delete_column('things_quizquestion', 'question_hr')

        # Deleting field 'QuizQuestion.question_zh-tw'
        db.delete_column('things_quizquestion', 'question_zh-tw')

        # Deleting field 'QuizQuestion.question_hu'
        db.delete_column('things_quizquestion', 'question_hu')

        # Deleting field 'QuizQuestion.question_bg'
        db.delete_column('things_quizquestion', 'question_bg')

        # Deleting field 'QuizQuestion.question_da'
        db.delete_column('things_quizquestion', 'question_da')

        # Deleting field 'QuizQuestion.question_hi'
        db.delete_column('things_quizquestion', 'question_hi')

        # Deleting field 'QuizQuestion.question_ja'
        db.delete_column('things_quizquestion', 'question_ja')

        # Deleting field 'QuizQuestion.question_he'
        db.delete_column('things_quizquestion', 'question_he')

        # Deleting field 'QuizQuestion.question_tr'
        db.delete_column('things_quizquestion', 'question_tr')

        # Deleting field 'QuizQuestion.question_ru'
        db.delete_column('things_quizquestion', 'question_ru')

        # Deleting field 'QuizQuestion.question_ca'
        db.delete_column('things_quizquestion', 'question_ca')

        # Deleting field 'QuizQuestion.question_fy-nl'
        db.delete_column('things_quizquestion', 'question_fy-nl')

        # Deleting field 'QuizQuestion.question_eu'
        db.delete_column('things_quizquestion', 'question_eu')

        # Deleting field 'QuizQuestion.question_et'
        db.delete_column('things_quizquestion', 'question_et')

        # Deleting field 'QuizQuestion.question_es'
        db.delete_column('things_quizquestion', 'question_es')

        # Deleting field 'QuizQuestion.question_ga'
        db.delete_column('things_quizquestion', 'question_ga')

        # Deleting field 'QuizQuestion.question_ar'
        db.delete_column('things_quizquestion', 'question_ar')

        # Deleting field 'QuizQuestion.question_el'
        db.delete_column('things_quizquestion', 'question_el')

        # Deleting field 'QuizQuestion.question_cs'
        db.delete_column('things_quizquestion', 'question_cs')

        # Deleting field 'QuizQuestion.question_pt-br'
        db.delete_column('things_quizquestion', 'question_pt-br')

        # Deleting field 'QuizQuestion.question_cy'
        db.delete_column('things_quizquestion', 'question_cy')

        # Deleting field 'QuizQuestion.question_gl'
        db.delete_column('things_quizquestion', 'question_gl')

        # Deleting field 'QuizQuestion.question_sl'
        db.delete_column('things_quizquestion', 'question_sl')

        # Deleting field 'QuizQuestion.question_uk'
        db.delete_column('things_quizquestion', 'question_uk')

        # Deleting field 'QuizQuestion.question_en'
        #db.delete_column('things_quizquestion', 'question_en')

        # Deleting field 'QuizQuestion.question_is'
        db.delete_column('things_quizquestion', 'question_is')

        # Deleting field 'QuizQuestion.question_mk'
        db.delete_column('things_quizquestion', 'question_mk')

        # Deleting field 'QuizQuestion.question_sq'
        db.delete_column('things_quizquestion', 'question_sq')

        # Deleting field 'QuizQuestion.question_es-ar'
        db.delete_column('things_quizquestion', 'question_es-ar')

        # Deleting field 'QuizQuestion.question_it'
        db.delete_column('things_quizquestion', 'question_it')

        # Deleting field 'QuizQuestion.question_km'
        db.delete_column('things_quizquestion', 'question_km')

        # Deleting field 'QuizQuestion.question_pt'
        db.delete_column('things_quizquestion', 'question_pt')

        # Deleting field 'QuizQuestion.question_ko'
        db.delete_column('things_quizquestion', 'question_ko')

        # Deleting field 'QuizQuestion.question_te'
        db.delete_column('things_quizquestion', 'question_te')

        # Deleting field 'QuizQuestion.question_mn'
        db.delete_column('things_quizquestion', 'question_mn')

        # Deleting field 'QuizQuestion.question_ml'
        db.delete_column('things_quizquestion', 'question_ml')

        # Deleting field 'QuizQuestion.question_ka'
        db.delete_column('things_quizquestion', 'question_ka')

        # Deleting field 'QuizQuestion.question_id'
        db.delete_column('things_quizquestion', 'question_id')

        # Adding field 'QuizQuestion.question'
        #db.add_column('things_quizquestion', 'question', self.gf('django.db.models.fields.CharField')(default='', max_length=200), keep_default=False)

    def backwards(self, orm):

        # Adding field 'QuizAnswerByImage.tooltip_sr'
        db.add_column('things_quizanswerbyimage', 'tooltip_sr', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True), keep_default=False)

        # Adding field 'QuizAnswerByImage.tooltip_zh-cn'
        db.add_column('things_quizanswerbyimage', 'tooltip_zh-cn', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True), keep_default=False)

        # Adding field 'QuizAnswerByImage.tooltip_bg'
        db.add_column('things_quizanswerbyimage', 'tooltip_bg', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True), keep_default=False)

        # Adding field 'QuizAnswerByImage.tooltip_bn'
        db.add_column('things_quizanswerbyimage', 'tooltip_bn', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True), keep_default=False)

        # Adding field 'QuizAnswerByImage.tooltip_hu'
        db.add_column('things_quizanswerbyimage', 'tooltip_hu', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True), keep_default=False)

        # Adding field 'QuizAnswerByImage.tooltip_sr-latn'
        db.add_column('things_quizanswerbyimage', 'tooltip_sr-latn', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True), keep_default=False)

        # Adding field 'QuizAnswerByImage.tooltip_bs'
        db.add_column('things_quizanswerbyimage', 'tooltip_bs', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True), keep_default=False)

        # Adding field 'QuizAnswerByImage.tooltip_zh-tw'
        db.add_column('things_quizanswerbyimage', 'tooltip_zh-tw', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True), keep_default=False)

        # Adding field 'QuizAnswerByImage.tooltip_sq'
        db.add_column('things_quizanswerbyimage', 'tooltip_sq', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True), keep_default=False)

        # Adding field 'QuizAnswerByImage.tooltip_nl'
        db.add_column('things_quizanswerbyimage', 'tooltip_nl', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True), keep_default=False)

        # Adding field 'QuizAnswerByImage.tooltip_sv'
        db.add_column('things_quizanswerbyimage', 'tooltip_sv', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True), keep_default=False)

        # Adding field 'QuizAnswerByImage.tooltip_nn'
        db.add_column('things_quizanswerbyimage', 'tooltip_nn', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True), keep_default=False)

        # Adding field 'QuizAnswerByImage.tooltip_he'
        db.add_column('things_quizanswerbyimage', 'tooltip_he', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True), keep_default=False)

        # Adding field 'QuizAnswerByImage.tooltip_es-ar'
        db.add_column('things_quizanswerbyimage', 'tooltip_es-ar', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True), keep_default=False)

        # Adding field 'QuizAnswerByImage.tooltip_fr'
        db.add_column('things_quizanswerbyimage', 'tooltip_fr', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True), keep_default=False)

        # Adding field 'QuizAnswerByImage.tooltip_kn'
        db.add_column('things_quizanswerbyimage', 'tooltip_kn', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True), keep_default=False)

        # Adding field 'QuizAnswerByImage.tooltip_uk'
        db.add_column('things_quizanswerbyimage', 'tooltip_uk', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True), keep_default=False)

        # Adding field 'QuizAnswerByImage.tooltip_pl'
        db.add_column('things_quizanswerbyimage', 'tooltip_pl', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True), keep_default=False)

        # Adding field 'QuizAnswerByImage.tooltip_nb'
        db.add_column('things_quizanswerbyimage', 'tooltip_nb', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True), keep_default=False)

        # Adding field 'QuizAnswerByImage.tooltip_hi'
        db.add_column('things_quizanswerbyimage', 'tooltip_hi', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True), keep_default=False)

        # Adding field 'QuizAnswerByImage.tooltip_pt-br'
        db.add_column('things_quizanswerbyimage', 'tooltip_pt-br', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True), keep_default=False)

        # Adding field 'QuizAnswerByImage.tooltip_da'
        db.add_column('things_quizanswerbyimage', 'tooltip_da', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True), keep_default=False)

        # Adding field 'QuizAnswerByImage.tooltip_hr'
        db.add_column('things_quizanswerbyimage', 'tooltip_hr', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True), keep_default=False)

        # Adding field 'QuizAnswerByImage.tooltip_fa'
        db.add_column('things_quizanswerbyimage', 'tooltip_fa', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True), keep_default=False)

        # Adding field 'QuizAnswerByImage.tooltip_de'
        db.add_column('things_quizanswerbyimage', 'tooltip_de', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True), keep_default=False)

        # Adding field 'QuizAnswerByImage.tooltip_ja'
        db.add_column('things_quizanswerbyimage', 'tooltip_ja', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True), keep_default=False)

        # Adding field 'QuizAnswerByImage.tooltip_sl'
        db.add_column('things_quizanswerbyimage', 'tooltip_sl', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True), keep_default=False)

        # Adding field 'QuizAnswerByImage.tooltip_lv'
        db.add_column('things_quizanswerbyimage', 'tooltip_lv', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True), keep_default=False)

        # Adding field 'QuizAnswerByImage.tooltip_fi'
        db.add_column('things_quizanswerbyimage', 'tooltip_fi', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True), keep_default=False)

        # Adding field 'QuizAnswerByImage.tooltip_lt'
        db.add_column('things_quizanswerbyimage', 'tooltip_lt', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True), keep_default=False)

        # Adding field 'QuizAnswerByImage.tooltip_te'
        db.add_column('things_quizanswerbyimage', 'tooltip_te', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True), keep_default=False)

        # Adding field 'QuizAnswerByImage.tooltip_ca'
        db.add_column('things_quizanswerbyimage', 'tooltip_ca', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True), keep_default=False)

        # Adding field 'QuizAnswerByImage.tooltip_gl'
        db.add_column('things_quizanswerbyimage', 'tooltip_gl', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True), keep_default=False)

        # Adding field 'QuizAnswerByImage.tooltip_ga'
        db.add_column('things_quizanswerbyimage', 'tooltip_ga', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True), keep_default=False)

        # Adding field 'QuizAnswerByImage.tooltip_ru'
        db.add_column('things_quizanswerbyimage', 'tooltip_ru', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True), keep_default=False)

        # Adding field 'QuizAnswerByImage.tooltip_mk'
        db.add_column('things_quizanswerbyimage', 'tooltip_mk', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True), keep_default=False)

        # Adding field 'QuizAnswerByImage.tooltip_tr'
        db.add_column('things_quizanswerbyimage', 'tooltip_tr', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True), keep_default=False)

        # Adding field 'QuizAnswerByImage.tooltip_no'
        db.add_column('things_quizanswerbyimage', 'tooltip_no', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True), keep_default=False)

        # Adding field 'QuizAnswerByImage.tooltip_cs'
        db.add_column('things_quizanswerbyimage', 'tooltip_cs', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True), keep_default=False)

        # Adding field 'QuizAnswerByImage.tooltip_cy'
        db.add_column('things_quizanswerbyimage', 'tooltip_cy', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True), keep_default=False)

        # Adding field 'QuizAnswerByImage.tooltip_ar'
        db.add_column('things_quizanswerbyimage', 'tooltip_ar', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True), keep_default=False)

        # Adding field 'QuizAnswerByImage.tooltip_id'
        db.add_column('things_quizanswerbyimage', 'tooltip_id', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True), keep_default=False)

        # Adding field 'QuizAnswerByImage.tooltip_es'
        db.add_column('things_quizanswerbyimage', 'tooltip_es', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True), keep_default=False)

        # Adding field 'QuizAnswerByImage.tooltip_ta'
        db.add_column('things_quizanswerbyimage', 'tooltip_ta', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True), keep_default=False)

        # Adding field 'QuizAnswerByImage.tooltip_eu'
        db.add_column('things_quizanswerbyimage', 'tooltip_eu', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True), keep_default=False)

        # Adding field 'QuizAnswerByImage.tooltip_et'
        db.add_column('things_quizanswerbyimage', 'tooltip_et', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True), keep_default=False)

        # Adding field 'QuizAnswerByImage.tooltip_ml'
        db.add_column('things_quizanswerbyimage', 'tooltip_ml', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True), keep_default=False)

        # Adding field 'QuizAnswerByImage.tooltip_sk'
        db.add_column('things_quizanswerbyimage', 'tooltip_sk', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True), keep_default=False)

        # Adding field 'QuizAnswerByImage.tooltip_pt'
        db.add_column('things_quizanswerbyimage', 'tooltip_pt', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True), keep_default=False)

        # Adding field 'QuizAnswerByImage.tooltip_mn'
        db.add_column('things_quizanswerbyimage', 'tooltip_mn', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True), keep_default=False)

        # Adding field 'QuizAnswerByImage.tooltip_vi'
        db.add_column('things_quizanswerbyimage', 'tooltip_vi', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True), keep_default=False)

        # Adding field 'QuizAnswerByImage.tooltip_ko'
        db.add_column('things_quizanswerbyimage', 'tooltip_ko', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True), keep_default=False)

        # Adding field 'QuizAnswerByImage.tooltip_it'
        db.add_column('things_quizanswerbyimage', 'tooltip_it', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True), keep_default=False)

        # Adding field 'QuizAnswerByImage.tooltip_km'
        db.add_column('things_quizanswerbyimage', 'tooltip_km', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True), keep_default=False)

        # Adding field 'QuizAnswerByImage.tooltip_fy-nl'
        db.add_column('things_quizanswerbyimage', 'tooltip_fy-nl', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True), keep_default=False)

        # Adding field 'QuizAnswerByImage.tooltip_is'
        db.add_column('things_quizanswerbyimage', 'tooltip_is', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True), keep_default=False)

        # Adding field 'QuizAnswerByImage.tooltip_th'
        db.add_column('things_quizanswerbyimage', 'tooltip_th', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True), keep_default=False)

        # Adding field 'QuizAnswerByImage.tooltip_ro'
        db.add_column('things_quizanswerbyimage', 'tooltip_ro', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True), keep_default=False)

        # Adding field 'QuizAnswerByImage.tooltip_en-gb'
        db.add_column('things_quizanswerbyimage', 'tooltip_en-gb', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True), keep_default=False)

        # Adding field 'QuizAnswerByImage.tooltip_el'
        db.add_column('things_quizanswerbyimage', 'tooltip_el', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True), keep_default=False)

        # Adding field 'QuizAnswerByImage.tooltip_ka'
        db.add_column('things_quizanswerbyimage', 'tooltip_ka', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True), keep_default=False)

        # renaming...
        db.rename_column('things_quizanswerbyimage', 'tooltip', 'tooltip_en')
        # Adding field 'QuizAnswerByImage.tooltip_en'
        #db.add_column('things_quizanswerbyimage', 'tooltip_en', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True), keep_default=False)

        # Deleting field 'QuizAnswerByImage.tooltip'
        #db.delete_column('things_quizanswerbyimage', 'tooltip')

        # Adding field 'QuizAnswer.answer_bn'
        db.add_column('things_quizanswer', 'answer_bn', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True), keep_default=False)

        # Adding field 'QuizAnswer.answer_ru'
        db.add_column('things_quizanswer', 'answer_ru', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True), keep_default=False)

        # Adding field 'QuizAnswer.answer_pt-br'
        db.add_column('things_quizanswer', 'answer_pt-br', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True), keep_default=False)

        # Adding field 'QuizAnswer.answer_uk'
        db.add_column('things_quizanswer', 'answer_uk', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True), keep_default=False)

        # Adding field 'QuizAnswer.answer_bg'
        db.add_column('things_quizanswer', 'answer_bg', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True), keep_default=False)

        # Adding field 'QuizAnswer.answer_de'
        db.add_column('things_quizanswer', 'answer_de', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True), keep_default=False)

        # Adding field 'QuizAnswer.answer_zh-cn'
        db.add_column('things_quizanswer', 'answer_zh-cn', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True), keep_default=False)

        # Adding field 'QuizAnswer.answer_te'
        db.add_column('things_quizanswer', 'answer_te', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True), keep_default=False)

        # Adding field 'QuizAnswer.answer_bs'
        db.add_column('things_quizanswer', 'answer_bs', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True), keep_default=False)

        # Adding field 'QuizAnswer.answer_en-gb'
        db.add_column('things_quizanswer', 'answer_en-gb', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True), keep_default=False)

        # Adding field 'QuizAnswer.answer_fr'
        db.add_column('things_quizanswer', 'answer_fr', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True), keep_default=False)

        # Adding field 'QuizAnswer.answer_th'
        db.add_column('things_quizanswer', 'answer_th', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True), keep_default=False)

        # Adding field 'QuizAnswer.answer_ta'
        db.add_column('things_quizanswer', 'answer_ta', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True), keep_default=False)

        # Adding field 'QuizAnswer.answer_nn'
        db.add_column('things_quizanswer', 'answer_nn', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True), keep_default=False)

        # Adding field 'QuizAnswer.answer_no'
        db.add_column('things_quizanswer', 'answer_no', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True), keep_default=False)

        # Adding field 'QuizAnswer.answer_nl'
        db.add_column('things_quizanswer', 'answer_nl', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True), keep_default=False)

        # Adding field 'QuizAnswer.answer_ja'
        db.add_column('things_quizanswer', 'answer_ja', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True), keep_default=False)

        # Adding field 'QuizAnswer.answer_nb'
        db.add_column('things_quizanswer', 'answer_nb', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True), keep_default=False)

        # Adding field 'QuizAnswer.answer_hu'
        db.add_column('things_quizanswer', 'answer_hu', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True), keep_default=False)

        # Adding field 'QuizAnswer.answer_sv'
        db.add_column('things_quizanswer', 'answer_sv', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True), keep_default=False)

        # Adding field 'QuizAnswer.answer_sq'
        db.add_column('things_quizanswer', 'answer_sq', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True), keep_default=False)

        # Adding field 'QuizAnswer.answer_hr'
        db.add_column('things_quizanswer', 'answer_hr', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True), keep_default=False)

        # Adding field 'QuizAnswer.answer_sr'
        db.add_column('things_quizanswer', 'answer_sr', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True), keep_default=False)

        # Adding field 'QuizAnswer.answer_sl'
        db.add_column('things_quizanswer', 'answer_sl', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True), keep_default=False)

        # Adding field 'QuizAnswer.answer_fa'
        db.add_column('things_quizanswer', 'answer_fa', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True), keep_default=False)

        # Adding field 'QuizAnswer.answer_lt'
        db.add_column('things_quizanswer', 'answer_lt', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True), keep_default=False)

        # Adding field 'QuizAnswer.answer_hi'
        db.add_column('things_quizanswer', 'answer_hi', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True), keep_default=False)

        # Adding field 'QuizAnswer.answer_lv'
        db.add_column('things_quizanswer', 'answer_lv', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True), keep_default=False)

        # Adding field 'QuizAnswer.answer_da'
        db.add_column('things_quizanswer', 'answer_da', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True), keep_default=False)

        # Adding field 'QuizAnswer.answer_he'
        db.add_column('things_quizanswer', 'answer_he', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True), keep_default=False)

        # Adding field 'QuizAnswer.answer_fi'
        db.add_column('things_quizanswer', 'answer_fi', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True), keep_default=False)

        # Adding field 'QuizAnswer.answer_tr'
        db.add_column('things_quizanswer', 'answer_tr', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True), keep_default=False)

        # Adding field 'QuizAnswer.answer_sk'
        db.add_column('things_quizanswer', 'answer_sk', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True), keep_default=False)

        # Adding field 'QuizAnswer.answer_sr-latn'
        db.add_column('things_quizanswer', 'answer_sr-latn', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True), keep_default=False)

        # Adding field 'QuizAnswer.answer_ml'
        db.add_column('things_quizanswer', 'answer_ml', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True), keep_default=False)

        # Adding field 'QuizAnswer.answer_ca'
        db.add_column('things_quizanswer', 'answer_ca', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True), keep_default=False)

        # Adding field 'QuizAnswer.answer_fy-nl'
        db.add_column('things_quizanswer', 'answer_fy-nl', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True), keep_default=False)

        # Adding field 'QuizAnswer.answer_ar'
        db.add_column('things_quizanswer', 'answer_ar', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True), keep_default=False)

        # Adding field 'QuizAnswer.answer_et'
        db.add_column('things_quizanswer', 'answer_et', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True), keep_default=False)

        # Adding field 'QuizAnswer.answer_cy'
        db.add_column('things_quizanswer', 'answer_cy', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True), keep_default=False)

        # Adding field 'QuizAnswer.answer_ro'
        db.add_column('things_quizanswer', 'answer_ro', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True), keep_default=False)

        # Adding field 'QuizAnswer.answer_ka'
        db.add_column('things_quizanswer', 'answer_ka', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True), keep_default=False)

        # Adding field 'QuizAnswer.answer_vi'
        db.add_column('things_quizanswer', 'answer_vi', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True), keep_default=False)

        # Adding field 'QuizAnswer.answer_cs'
        db.add_column('things_quizanswer', 'answer_cs', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True), keep_default=False)

        # Adding field 'QuizAnswer.answer_zh-tw'
        db.add_column('things_quizanswer', 'answer_zh-tw', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True), keep_default=False)

        # Adding field 'QuizAnswer.answer_pt'
        db.add_column('things_quizanswer', 'answer_pt', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True), keep_default=False)

        # Adding field 'QuizAnswer.answer_mn'
        db.add_column('things_quizanswer', 'answer_mn', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True), keep_default=False)

        # Adding field 'QuizAnswer.answer_eu'
        db.add_column('things_quizanswer', 'answer_eu', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True), keep_default=False)

        # Adding field 'QuizAnswer.answer_es-ar'
        db.add_column('things_quizanswer', 'answer_es-ar', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True), keep_default=False)

        # Adding field 'QuizAnswer.answer_es'
        db.add_column('things_quizanswer', 'answer_es', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True), keep_default=False)

        # Adding field 'QuizAnswer.answer_is'
        db.add_column('things_quizanswer', 'answer_is', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True), keep_default=False)

        # Adding field 'QuizAnswer.answer_mk'
        db.add_column('things_quizanswer', 'answer_mk', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True), keep_default=False)

        # Adding field 'QuizAnswer.answer_ko'
        db.add_column('things_quizanswer', 'answer_ko', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True), keep_default=False)

        # Adding field 'QuizAnswer.answer_kn'
        db.add_column('things_quizanswer', 'answer_kn', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True), keep_default=False)

        # Adding field 'QuizAnswer.answer_it'
        db.add_column('things_quizanswer', 'answer_it', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True), keep_default=False)

        # Adding field 'QuizAnswer.answer_ga'
        db.add_column('things_quizanswer', 'answer_ga', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True), keep_default=False)

        # Adding field 'QuizAnswer.answer_km'
        db.add_column('things_quizanswer', 'answer_km', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True), keep_default=False)

        # Adding field 'QuizAnswer.answer_pl'
        db.add_column('things_quizanswer', 'answer_pl', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True), keep_default=False)

        # renaming...
        db.rename_column('things_quizanswer', 'answer', 'answer_en')
        # Adding field 'QuizAnswer.answer_en'
        #db.add_column('things_quizanswer', 'answer_en', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True), keep_default=False)

        # Adding field 'QuizAnswer.answer_el'
        db.add_column('things_quizanswer', 'answer_el', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True), keep_default=False)

        # Adding field 'QuizAnswer.answer_gl'
        db.add_column('things_quizanswer', 'answer_gl', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True), keep_default=False)

        # Adding field 'QuizAnswer.answer_id'
        db.add_column('things_quizanswer', 'answer_id', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True), keep_default=False)

        # Deleting field 'QuizAnswer.answer'
        #db.delete_column('things_quizanswer', 'answer')

        # Adding field 'Image.name_zh-cn'
        db.add_column('things_image', 'name_zh-cn', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True), keep_default=False)

        # Adding field 'Image.name_fr'
        db.add_column('things_image', 'name_fr', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True), keep_default=False)

        # Adding field 'Image.name_zh-tw'
        db.add_column('things_image', 'name_zh-tw', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True), keep_default=False)

        # Adding field 'Image.name_fa'
        db.add_column('things_image', 'name_fa', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True), keep_default=False)

        # Adding field 'Image.name_de'
        db.add_column('things_image', 'name_de', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True), keep_default=False)

        # Adding field 'Image.name_no'
        db.add_column('things_image', 'name_no', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True), keep_default=False)

        # Adding field 'Image.name_da'
        db.add_column('things_image', 'name_da', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True), keep_default=False)

        # Adding field 'Image.name_fi'
        db.add_column('things_image', 'name_fi', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True), keep_default=False)

        # Adding field 'Image.name_ml'
        db.add_column('things_image', 'name_ml', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True), keep_default=False)

        # Adding field 'Image.name_pl'
        db.add_column('things_image', 'name_pl', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True), keep_default=False)

        # Adding field 'Image.name_mn'
        db.add_column('things_image', 'name_mn', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True), keep_default=False)

        # Adding field 'Image.name_ca'
        db.add_column('things_image', 'name_ca', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True), keep_default=False)

        # Adding field 'Image.name_it'
        db.add_column('things_image', 'name_it', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True), keep_default=False)

        # Adding field 'Image.name_ta'
        db.add_column('things_image', 'name_ta', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True), keep_default=False)

        # Adding field 'Image.name_mk'
        db.add_column('things_image', 'name_mk', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True), keep_default=False)

        # Adding field 'Image.name_vi'
        db.add_column('things_image', 'name_vi', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True), keep_default=False)

        # Adding field 'Image.name_nb'
        db.add_column('things_image', 'name_nb', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True), keep_default=False)

        # Adding field 'Image.name_th'
        db.add_column('things_image', 'name_th', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True), keep_default=False)

        # Adding field 'Image.name_cs'
        db.add_column('things_image', 'name_cs', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True), keep_default=False)

        # Adding field 'Image.name_en-gb'
        db.add_column('things_image', 'name_en-gb', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True), keep_default=False)

        # Adding field 'Image.name_id'
        db.add_column('things_image', 'name_id', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True), keep_default=False)

        # Adding field 'Image.name_ko'
        db.add_column('things_image', 'name_ko', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True), keep_default=False)

        # Adding field 'Image.name_km'
        db.add_column('things_image', 'name_km', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True), keep_default=False)

        # Adding field 'Image.name_kn'
        db.add_column('things_image', 'name_kn', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True), keep_default=False)

        # Adding field 'Image.name_ro'
        db.add_column('things_image', 'name_ro', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True), keep_default=False)

        # Adding field 'Image.name_cy'
        db.add_column('things_image', 'name_cy', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True), keep_default=False)

        # Adding field 'Image.name_es-ar'
        db.add_column('things_image', 'name_es-ar', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True), keep_default=False)

        # Adding field 'Image.name_pt'
        db.add_column('things_image', 'name_pt', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True), keep_default=False)

        # Adding field 'Image.name_et'
        db.add_column('things_image', 'name_et', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True), keep_default=False)

        # Adding field 'Image.name_eu'
        db.add_column('things_image', 'name_eu', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True), keep_default=False)

        # Adding field 'Image.name_he'
        db.add_column('things_image', 'name_he', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True), keep_default=False)

        # Adding field 'Image.name_es'
        db.add_column('things_image', 'name_es', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True), keep_default=False)

        # Adding field 'Image.name_ar'
        db.add_column('things_image', 'name_ar', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True), keep_default=False)

        # Adding field 'Image.name_te'
        db.add_column('things_image', 'name_te', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True), keep_default=False)

        # Adding field 'Image.name_gl'
        db.add_column('things_image', 'name_gl', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True), keep_default=False)

        # Adding field 'Image.name_is'
        db.add_column('things_image', 'name_is', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True), keep_default=False)

        # Adding field 'Image.name_pt-br'
        db.add_column('things_image', 'name_pt-br', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True), keep_default=False)

        # Adding field 'Image.name_sk'
        db.add_column('things_image', 'name_sk', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True), keep_default=False)

        # Adding field 'Image.name_el'
        db.add_column('things_image', 'name_el', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True), keep_default=False)

        #rename...
        db.rename_column('things_image', 'name', 'name_en')
        # Adding field 'Image.name_en'
        #db.add_column('things_image', 'name_en', self.gf('django.db.models.fields.CharField')(max_length=100, null=True), keep_default=False)

        # Adding field 'Image.name_sr-latn'
        db.add_column('things_image', 'name_sr-latn', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True), keep_default=False)

        # Adding field 'Image.name_ga'
        db.add_column('things_image', 'name_ga', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True), keep_default=False)

        # Adding field 'Image.name_sr'
        db.add_column('things_image', 'name_sr', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True), keep_default=False)

        # Adding field 'Image.name_hr'
        db.add_column('things_image', 'name_hr', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True), keep_default=False)

        # Adding field 'Image.name_bg'
        db.add_column('things_image', 'name_bg', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True), keep_default=False)

        # Adding field 'Image.name_ka'
        db.add_column('things_image', 'name_ka', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True), keep_default=False)

        # Adding field 'Image.name_sv'
        db.add_column('things_image', 'name_sv', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True), keep_default=False)

        # Adding field 'Image.name_nl'
        db.add_column('things_image', 'name_nl', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True), keep_default=False)

        # Adding field 'Image.name_hu'
        db.add_column('things_image', 'name_hu', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True), keep_default=False)

        # Adding field 'Image.name_nn'
        db.add_column('things_image', 'name_nn', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True), keep_default=False)

        # Adding field 'Image.name_bn'
        db.add_column('things_image', 'name_bn', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True), keep_default=False)

        # Adding field 'Image.name_fy-nl'
        db.add_column('things_image', 'name_fy-nl', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True), keep_default=False)

        # Adding field 'Image.name_ru'
        db.add_column('things_image', 'name_ru', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True), keep_default=False)

        # Adding field 'Image.name_sq'
        db.add_column('things_image', 'name_sq', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True), keep_default=False)

        # Adding field 'Image.name_uk'
        db.add_column('things_image', 'name_uk', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True), keep_default=False)

        # Adding field 'Image.name_bs'
        db.add_column('things_image', 'name_bs', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True), keep_default=False)

        # Adding field 'Image.name_lv'
        db.add_column('things_image', 'name_lv', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True), keep_default=False)

        # Adding field 'Image.name_hi'
        db.add_column('things_image', 'name_hi', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True), keep_default=False)

        # Adding field 'Image.name_lt'
        db.add_column('things_image', 'name_lt', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True), keep_default=False)

        # Adding field 'Image.name_ja'
        db.add_column('things_image', 'name_ja', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True), keep_default=False)

        # Adding field 'Image.name_tr'
        db.add_column('things_image', 'name_tr', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True), keep_default=False)

        # Adding field 'Image.name_sl'
        db.add_column('things_image', 'name_sl', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True), keep_default=False)

        # Deleting field 'Image.name'
        #db.delete_column('things_image', 'name')

        # Adding field 'QuizQuestion.question_nn'
        db.add_column('things_quizquestion', 'question_nn', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True), keep_default=False)

        # Adding field 'QuizQuestion.question_no'
        db.add_column('things_quizquestion', 'question_no', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True), keep_default=False)

        # Adding field 'QuizQuestion.question_nl'
        db.add_column('things_quizquestion', 'question_nl', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True), keep_default=False)

        # Adding field 'QuizQuestion.question_kn'
        db.add_column('things_quizquestion', 'question_kn', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True), keep_default=False)

        # Adding field 'QuizQuestion.question_fr'
        db.add_column('things_quizquestion', 'question_fr', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True), keep_default=False)

        # Adding field 'QuizQuestion.question_en-gb'
        db.add_column('things_quizquestion', 'question_en-gb', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True), keep_default=False)

        # Adding field 'QuizQuestion.question_sr'
        db.add_column('things_quizquestion', 'question_sr', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True), keep_default=False)

        # Adding field 'QuizQuestion.question_bs'
        db.add_column('things_quizquestion', 'question_bs', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True), keep_default=False)

        # Adding field 'QuizQuestion.question_nb'
        db.add_column('things_quizquestion', 'question_nb', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True), keep_default=False)

        # Adding field 'QuizQuestion.question_ta'
        db.add_column('things_quizquestion', 'question_ta', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True), keep_default=False)

        # Adding field 'QuizQuestion.question_sv'
        db.add_column('things_quizquestion', 'question_sv', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True), keep_default=False)

        # Adding field 'QuizQuestion.question_bn'
        db.add_column('things_quizquestion', 'question_bn', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True), keep_default=False)

        # Adding field 'QuizQuestion.question_sr-latn'
        db.add_column('things_quizquestion', 'question_sr-latn', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True), keep_default=False)

        # Adding field 'QuizQuestion.question_fa'
        db.add_column('things_quizquestion', 'question_fa', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True), keep_default=False)

        # Adding field 'QuizQuestion.question_de'
        db.add_column('things_quizquestion', 'question_de', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True), keep_default=False)

        # Adding field 'QuizQuestion.question_vi'
        db.add_column('things_quizquestion', 'question_vi', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True), keep_default=False)

        # Adding field 'QuizQuestion.question_sk'
        db.add_column('things_quizquestion', 'question_sk', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True), keep_default=False)

        # Adding field 'QuizQuestion.question_fi'
        db.add_column('things_quizquestion', 'question_fi', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True), keep_default=False)

        # Adding field 'QuizQuestion.question_lt'
        db.add_column('things_quizquestion', 'question_lt', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True), keep_default=False)

        # Adding field 'QuizQuestion.question_lv'
        db.add_column('things_quizquestion', 'question_lv', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True), keep_default=False)

        # Adding field 'QuizQuestion.question_zh-cn'
        db.add_column('things_quizquestion', 'question_zh-cn', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True), keep_default=False)

        # Adding field 'QuizQuestion.question_th'
        db.add_column('things_quizquestion', 'question_th', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True), keep_default=False)

        # Adding field 'QuizQuestion.question_ro'
        db.add_column('things_quizquestion', 'question_ro', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True), keep_default=False)

        # Adding field 'QuizQuestion.question_pl'
        db.add_column('things_quizquestion', 'question_pl', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True), keep_default=False)

        # Adding field 'QuizQuestion.question_hr'
        db.add_column('things_quizquestion', 'question_hr', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True), keep_default=False)

        # Adding field 'QuizQuestion.question_zh-tw'
        db.add_column('things_quizquestion', 'question_zh-tw', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True), keep_default=False)

        # Adding field 'QuizQuestion.question_hu'
        db.add_column('things_quizquestion', 'question_hu', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True), keep_default=False)

        # Adding field 'QuizQuestion.question_bg'
        db.add_column('things_quizquestion', 'question_bg', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True), keep_default=False)

        # Adding field 'QuizQuestion.question_da'
        db.add_column('things_quizquestion', 'question_da', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True), keep_default=False)

        # Adding field 'QuizQuestion.question_hi'
        db.add_column('things_quizquestion', 'question_hi', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True), keep_default=False)

        # Adding field 'QuizQuestion.question_ja'
        db.add_column('things_quizquestion', 'question_ja', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True), keep_default=False)

        # Adding field 'QuizQuestion.question_he'
        db.add_column('things_quizquestion', 'question_he', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True), keep_default=False)

        # Adding field 'QuizQuestion.question_tr'
        db.add_column('things_quizquestion', 'question_tr', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True), keep_default=False)

        # Adding field 'QuizQuestion.question_ru'
        db.add_column('things_quizquestion', 'question_ru', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True), keep_default=False)

        # Adding field 'QuizQuestion.question_ca'
        db.add_column('things_quizquestion', 'question_ca', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True), keep_default=False)

        # Adding field 'QuizQuestion.question_fy-nl'
        db.add_column('things_quizquestion', 'question_fy-nl', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True), keep_default=False)

        # Adding field 'QuizQuestion.question_eu'
        db.add_column('things_quizquestion', 'question_eu', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True), keep_default=False)

        # Adding field 'QuizQuestion.question_et'
        db.add_column('things_quizquestion', 'question_et', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True), keep_default=False)

        # Adding field 'QuizQuestion.question_es'
        db.add_column('things_quizquestion', 'question_es', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True), keep_default=False)

        # Adding field 'QuizQuestion.question_ga'
        db.add_column('things_quizquestion', 'question_ga', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True), keep_default=False)

        # Adding field 'QuizQuestion.question_ar'
        db.add_column('things_quizquestion', 'question_ar', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True), keep_default=False)

        # Adding field 'QuizQuestion.question_el'
        db.add_column('things_quizquestion', 'question_el', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True), keep_default=False)

        # Adding field 'QuizQuestion.question_cs'
        db.add_column('things_quizquestion', 'question_cs', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True), keep_default=False)

        # Adding field 'QuizQuestion.question_pt-br'
        db.add_column('things_quizquestion', 'question_pt-br', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True), keep_default=False)

        # Adding field 'QuizQuestion.question_cy'
        db.add_column('things_quizquestion', 'question_cy', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True), keep_default=False)

        # Adding field 'QuizQuestion.question_gl'
        db.add_column('things_quizquestion', 'question_gl', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True), keep_default=False)

        # Adding field 'QuizQuestion.question_sl'
        db.add_column('things_quizquestion', 'question_sl', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True), keep_default=False)

        # Adding field 'QuizQuestion.question_uk'
        db.add_column('things_quizquestion', 'question_uk', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True), keep_default=False)

        #rename
        db.rename_column('things_quizquestion', 'question', 'question_en')
        # Adding field 'QuizQuestion.question_en'
        #db.add_column('things_quizquestion', 'question_en', self.gf('django.db.models.fields.CharField')(max_length=200, null=True), keep_default=False)

        # Adding field 'QuizQuestion.question_is'
        db.add_column('things_quizquestion', 'question_is', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True), keep_default=False)

        # Adding field 'QuizQuestion.question_mk'
        db.add_column('things_quizquestion', 'question_mk', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True), keep_default=False)

        # Adding field 'QuizQuestion.question_sq'
        db.add_column('things_quizquestion', 'question_sq', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True), keep_default=False)

        # Adding field 'QuizQuestion.question_es-ar'
        db.add_column('things_quizquestion', 'question_es-ar', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True), keep_default=False)

        # Adding field 'QuizQuestion.question_it'
        db.add_column('things_quizquestion', 'question_it', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True), keep_default=False)

        # Adding field 'QuizQuestion.question_km'
        db.add_column('things_quizquestion', 'question_km', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True), keep_default=False)

        # Adding field 'QuizQuestion.question_pt'
        db.add_column('things_quizquestion', 'question_pt', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True), keep_default=False)

        # Adding field 'QuizQuestion.question_ko'
        db.add_column('things_quizquestion', 'question_ko', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True), keep_default=False)

        # Adding field 'QuizQuestion.question_te'
        db.add_column('things_quizquestion', 'question_te', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True), keep_default=False)

        # Adding field 'QuizQuestion.question_mn'
        db.add_column('things_quizquestion', 'question_mn', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True), keep_default=False)

        # Adding field 'QuizQuestion.question_ml'
        db.add_column('things_quizquestion', 'question_ml', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True), keep_default=False)

        # Adding field 'QuizQuestion.question_ka'
        db.add_column('things_quizquestion', 'question_ka', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True), keep_default=False)

        # Adding field 'QuizQuestion.question_id'
        db.add_column('things_quizquestion', 'question_id', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True), keep_default=False)

        # Deleting field 'QuizQuestion.question'
        #db.delete_column('things_quizquestion', 'question')

    models = {
        'things.collage': {
            'Meta': {'object_name': 'Collage'},
            'background_img': ('django.db.models.fields.CharField', [], {'default': "'wood.jpg'", 'max_length': '50'}),
            'featured': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'filename': ('django.db.models.fields.CharField', [], {'max_length': '75'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'images_coords': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'in_gallery': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'packed': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50', 'db_index': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'things.image': {
            'Meta': {'object_name': 'Image'},
            'file_name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'}),
            'height': ('django.db.models.fields.IntegerField', [], {'default': '50'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'locale': ('django.db.models.fields.CharField', [], {'max_length': '2', 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50', 'db_index': 'True'}),
            'width': ('django.db.models.fields.IntegerField', [], {'default': '50'})
        },
        'things.quizanswer': {
            'Meta': {'object_name': 'QuizAnswer'},
            'answer': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'quiz_question': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['things.QuizQuestion']"}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50', 'db_index': 'True'})
        },
        'things.quizanswerbyimage': {
            'Meta': {'object_name': 'QuizAnswerByImage'},
            'answer': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['things.QuizAnswer']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['things.Image']"}),
            'tooltip': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'})
        },
        'things.quizquestion': {
            'Meta': {'object_name': 'QuizQuestion'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'question': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'slug': ('django.db.models.fields.SlugField', [], {'db_index': 'True', 'max_length': '50', 'blank': 'True'})
        }
    }

    complete_apps = ['things']

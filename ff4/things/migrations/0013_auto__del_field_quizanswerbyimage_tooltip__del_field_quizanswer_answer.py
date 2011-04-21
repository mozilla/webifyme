# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):
    
    def forwards(self, orm):
        
        # Deleting field 'QuizAnswerByImage.tooltip'
        db.delete_column('things_quizanswerbyimage', 'tooltip')

        # Deleting field 'QuizAnswer.answer'
        db.delete_column('things_quizanswer', 'answer')

        # Deleting field 'QuizQuestion.question'
        db.delete_column('things_quizquestion', 'question')
    
    
    def backwards(self, orm):
        
        # Adding field 'QuizAnswerByImage.tooltip'
        db.add_column('things_quizanswerbyimage', 'tooltip', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True), keep_default=False)

        # Adding field 'QuizAnswer.answer'
        db.add_column('things_quizanswer', 'answer', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True), keep_default=False)

        # Adding field 'QuizQuestion.question'
        db.add_column('things_quizquestion', 'question', self.gf('django.db.models.fields.CharField')(default=None, max_length=200), keep_default=False)
    
    
    models = {
        'things.collage': {
            'Meta': {'object_name': 'Collage'},
            'background_img': ('django.db.models.fields.CharField', [], {'default': "'wood.jpg'", 'max_length': '50'}),
            'bitly_url': ('django.db.models.fields.CharField', [], {'max_length': '75', 'null': 'True', 'blank': 'True'}),
            'featured': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'filename': ('django.db.models.fields.CharField', [], {'max_length': '75'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'images_coords': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'in_gallery': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'packed': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
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
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'quiz_question': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['things.QuizQuestion']"}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50', 'db_index': 'True'})
        },
        'things.quizanswerbyimage': {
            'Meta': {'object_name': 'QuizAnswerByImage'},
            'answer': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['things.QuizAnswer']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['things.Image']"})
        },
        'things.quizquestion': {
            'Meta': {'object_name': 'QuizQuestion'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'db_index': 'True', 'max_length': '50', 'blank': 'True'})
        }
    }
    
    complete_apps = ['things']

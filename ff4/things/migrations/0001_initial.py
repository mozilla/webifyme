# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Adding model 'QuizQuestion'
        db.create_table('things_quizquestion', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('slug', self.gf('django.db.models.fields.CharField')(unique=True, max_length=30)),
            ('question', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal('things', ['QuizQuestion'])

        # Adding model 'QuizAnswer'
        db.create_table('things_quizanswer', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('slug', self.gf('django.db.models.fields.CharField')(unique=True, max_length=30)),
            ('answer', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('weight', self.gf('django.db.models.fields.IntegerField')()),
            ('quiz_question', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['things.QuizQuestion'])),
        ))
        db.send_create_signal('things', ['QuizAnswer'])

        # Adding model 'Image'
        db.create_table('things_image', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('slug', self.gf('django.db.models.fields.CharField')(unique=True, max_length=30)),
            ('file_name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=100)),
            ('area_small', self.gf('django.db.models.fields.IntegerField')()),
            ('area_medium', self.gf('django.db.models.fields.IntegerField')()),
            ('area_large', self.gf('django.db.models.fields.IntegerField')()),
            ('locale', self.gf('django.db.models.fields.CharField')(max_length=2)),
        ))
        db.send_create_signal('things', ['Image'])

        # Adding model 'QuizAnswerByImage'
        db.create_table('things_quizanswerbyimage', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('image', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['things.Image'])),
            ('answer', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['things.QuizAnswer'])),
            ('tooltip', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal('things', ['QuizAnswerByImage'])

        # Adding model 'Collage'
        db.create_table('things_collage', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('slug', self.gf('django.db.models.fields.CharField')(unique=True, max_length=100)),
            ('username', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('featured', self.gf('django.db.models.fields.IntegerField')()),
            ('filename', self.gf('django.db.models.fields.CharField')(max_length=75)),
        ))
        db.send_create_signal('things', ['Collage'])

    def backwards(self, orm):

        # Deleting model 'QuizQuestion'
        db.delete_table('things_quizquestion')

        # Deleting model 'QuizAnswer'
        db.delete_table('things_quizanswer')

        # Deleting model 'Image'
        db.delete_table('things_image')

        # Deleting model 'QuizAnswerByImage'
        db.delete_table('things_quizanswerbyimage')

        # Deleting model 'Collage'
        db.delete_table('things_collage')

    models = {
        'things.collage': {
            'Meta': {'object_name': 'Collage'},
            'featured': ('django.db.models.fields.IntegerField', [], {}),
            'filename': ('django.db.models.fields.CharField', [], {'max_length': '75'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'slug': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'}),
            'username': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'things.image': {
            'Meta': {'object_name': 'Image'},
            'area_large': ('django.db.models.fields.IntegerField', [], {}),
            'area_medium': ('django.db.models.fields.IntegerField', [], {}),
            'area_small': ('django.db.models.fields.IntegerField', [], {}),
            'file_name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'locale': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'slug': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'things.quizanswer': {
            'Meta': {'object_name': 'QuizAnswer'},
            'answer': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'quiz_question': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['things.QuizQuestion']"}),
            'slug': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'}),
            'weight': ('django.db.models.fields.IntegerField', [], {})
        },
        'things.quizanswerbyimage': {
            'Meta': {'object_name': 'QuizAnswerByImage'},
            'answer': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['things.QuizAnswer']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['things.Image']"}),
            'tooltip': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'things.quizquestion': {
            'Meta': {'object_name': 'QuizQuestion'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'question': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'slug': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        }
    }

    complete_apps = ['things']

# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'YouTube'
        db.create_table('cmsplugin_youtube', (
            ('cmsplugin_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['cms.CMSPlugin'], unique=True, primary_key=True)),
            ('video_id', self.gf('django.db.models.fields.CharField')(max_length=60)),
            ('autoplay', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('width', self.gf('django.db.models.fields.IntegerField')(default=425)),
            ('height', self.gf('django.db.models.fields.IntegerField')(default=344)),
            ('border', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('allow_fullscreen', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('loop', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('display_related_videos', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('cmsplugin_youtube', ['YouTube'])


    def backwards(self, orm):
        
        # Deleting model 'YouTube'
        db.delete_table('cmsplugin_youtube')


    models = {
        'cms.cmsplugin': {
            'Meta': {'object_name': 'CMSPlugin'},
            'creation_date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language': ('django.db.models.fields.CharField', [], {'max_length': '15', 'db_index': 'True'}),
            'level': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'lft': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['cms.CMSPlugin']", 'null': 'True', 'blank': 'True'}),
            'placeholder': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['cms.Placeholder']", 'null': 'True'}),
            'plugin_type': ('django.db.models.fields.CharField', [], {'max_length': '50', 'db_index': 'True'}),
            'position': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'rght': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'tree_id': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'})
        },
        'cms.placeholder': {
            'Meta': {'object_name': 'Placeholder'},
            'default_width': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'slot': ('django.db.models.fields.CharField', [], {'max_length': '50', 'db_index': 'True'})
        },
        'cmsplugin_youtube.youtube': {
            'Meta': {'object_name': 'YouTube', 'db_table': "'cmsplugin_youtube'", '_ormbases': ['cms.CMSPlugin']},
            'allow_fullscreen': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'autoplay': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'border': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'cmsplugin_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['cms.CMSPlugin']", 'unique': 'True', 'primary_key': 'True'}),
            'display_related_videos': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'height': ('django.db.models.fields.IntegerField', [], {'default': '344'}),
            'loop': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'video_id': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'width': ('django.db.models.fields.IntegerField', [], {'default': '425'})
        }
    }

    complete_apps = ['cmsplugin_youtube']

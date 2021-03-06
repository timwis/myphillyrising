# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Changing field 'ContentTag_item.contenttag_id'
        db.alter_column(u'alexander_contentitem_tags', 'contenttag_id', self.gf('django.db.models.fields.CharField')(max_length=100))

    def backwards(self, orm):
        # User chose to not deal with backwards NULL issues for 'ContentItem.tags.through.contenttag_id'
        raise RuntimeError("Cannot reverse this migration. 'ContentItem_tags.contenttag_id' and its values cannot be restored.")

    models = {
        u'alexander.contentitem': {
            'Meta': {'object_name': 'ContentItem'},
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'feed': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'items'", 'to': u"orm['alexander.Feed']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'source_content': ('django.db.models.fields.TextField', [], {}),
            'source_id': ('django.db.models.fields.CharField', [], {'max_length': '1000'}),
            'source_posted_at': ('django.db.models.fields.DateTimeField', [], {}),
            'source_url': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'tags': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['alexander.ContentTag']", 'symmetrical': 'False'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '160', 'null': 'True'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        u'alexander.contenttag': {
            'Meta': {'object_name': 'ContentTag'},
            'label': ('django.db.models.fields.CharField', [], {'max_length': '100', 'primary_key': 'True'})
        },
        u'alexander.feed': {
            'Meta': {'object_name': 'Feed'},
            'default_category': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_read_at': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'source_type': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'source_url': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['alexander']
from django.contrib import admin

from jonnsonaguirre.works.models import Work, MediaFile, YoutubeVideo



class MediaFileInline(admin.TabularInline):
    model = MediaFile
    exclude = ('name',)
    order_field = 'order'
    
class YoutubeVideoInline(admin.TabularInline):
    model = YoutubeVideo
    exclude = ()
    order_field = 'order'

class WorkAdmin(admin.ModelAdmin):
    list_display = ('name','date',)
    ordering = ('name',)
    inlines = (MediaFileInline,YoutubeVideoInline,)
    prepopulated_fields = {
        'slug': ('name',)
    }

admin.site.register(Work, WorkAdmin)

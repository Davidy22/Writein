from django.contrib import admin
from .models import poll, entry

# Register your models here.
class pollAdmin(admin.ModelAdmin):
	list_display = ('question', 'id')
	pass
admin.site.register(poll,pollAdmin)

class entryAdmin(admin.ModelAdmin):
	list_filter = ('pollID','IP', 'text')
	list_display = ('text', 'IP', 'pollID')
admin.site.register(entry,entryAdmin)

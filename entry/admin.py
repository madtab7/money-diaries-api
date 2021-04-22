from django.contrib import admin
from .models import Entry

class EntryAdmin(admin.ModelAdmin):
  list_display=('id', 'source', 'text', 'occupation', 'location', 'industry', 'age', 'salary')
  list_filter = ('location', 'industry')
  search_fields= ('location', 'text', 'industry', 'other_data')


admin.site.register(Entry, EntryAdmin)

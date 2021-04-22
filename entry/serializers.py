from rest_framework import serializers
from .models import Entry

class GeneralEntriesSerializer(serializers.ModelSerializer):
  class Meta:
    model = Entry
    fields = '__all__'
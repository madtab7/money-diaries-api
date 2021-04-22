from django.shortcuts import render
from django.db import IntegrityError, Error, DatabaseError, InternalError, transaction
from django.http import HttpResponse
from rest_framework import viewsets, parsers, renderers, status
from rest_framework.response import Response
from drf_spectacular.utils import extend_schema, inline_serializer, OpenApiParameter

from .models import Entry
from .serializers import GeneralEntriesSerializer

def index(request):
  return HttpResponse("hello")

# def _get_data_value_or_default(data_obj, key, type):
    # default_string = "N/A"
    # default_num = 0
#     string_fields = ['source']
#     default_value = 

#     value = data_obj.key if key in data_obj else default_value
#     return value


class EntryView(viewsets.ViewSet):
  permission_classes = ()

  @extend_schema(
    parameters=[],
    responses={200: GeneralEntriesSerializer, 404: None}
  )
  def list(self, request):
    """
    Returns all entries.
    """
    try:
      entries = Entry.objects.all()
      serialized_entries = GeneralEntriesSerializer(entries, many=True)
      return Response(serialized_entries.data, status=200)
    except Exception as e:
      return Response(status=404)

  @extend_schema(
    responses={200: GeneralEntriesSerializer, 404: None}
  )
  def retrieve(self, request, pk=None):
    """
    Returns information about specified entry.
    """
    try:
        entry = Entry.objects.get(pk=pk)
    except Entry.DoesNotExist:
        return Response({'error': f'Unable to find entry with id {pk}'})

    serialized_data = GeneralEntriesSerializer(entry)
    return Response(serialized_data.data)

  @extend_schema(
    request=GeneralEntriesSerializer(many=True)
    
  )
  def create(self, request):
    """
    Creates new money diary entry.
    """
    serializer = GeneralEntriesSerializer(data=request.data, many=True)

    if serializer.is_valid(raise_exception=True):
      default_string = "N/A"
      default_num = 0

      created_entries = 0
      errors = []

      for entry in request.data:
        try:
          with transaction.atomic():
            # CREATE HELPER FUNCTION TO NORMALIZE DEFAULT DATA
            source=entry['url'] if 'url' in entry else default_string
            text=entry['title'] if 'title' in entry else default_string
            occupation=entry['occupation'] if 'occupation' in entry else default_string
            industry=entry['industry'] if 'industry' in entry else default_string
            age=entry['age'] if 'age' in entry else default_num
            location=entry['location'] if 'location' in entry else default_string
            salary=entry['salary'] if 'salary' in entry else default_num
            paycheck=entry['paycheck'] if 'paycheck' in entry else default_num
            debt=entry['debt'] if 'debt' in entry else default_num
            net_worth=entry['net_worth'] if 'net_worth' in entry else default_num
            rent=entry['rent'] if 'rent' in entry else default_num
            pronouns=entry['pronouns'] if 'pronouns' in entry else default_string
            gender=entry['gender'] if 'gender' in entry else default_string
            other_data=entry['meta']

            created_entry = Entry.objects.create(
              source=source,
              text=text,
              occupation=occupation,
              industry=industry,
              age=age,
              location=location,
              salary=salary,
              paycheck=paycheck,
              debt=debt,
              net_worth=net_worth,
              rent=rent,
              pronouns=pronouns,
              gender=gender,
              other_data=other_data
            )

            created_entries += 1
        except (IntegrityError, Error, DatabaseError, InternalError) as e:
          errors.append(e)
      return Response({"success": f"created {created_entries} new entries.", "errors": errors}, status=201)
    else: 
      return Response({"error": "something went wrong. please try again."}, status=400)
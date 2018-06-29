from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import course
from .serializers import courseSerializer


class courseList(APIView):
    

    def get(self, request, Chapter,Class,Subject):
        course1 =course.objects.filter(Chapter = Chapter, Class=Class, Subject=Subject)
        serializer=courseSerializer(course1, many=True)
        return Response(serializer.data)

    def post(self):
        pass

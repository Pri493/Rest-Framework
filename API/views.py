from django.shortcuts import render
from rest_framework import viewsets

from .models import Question

from .serializers import QuestionSerializer, ChoiceSerializer


class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

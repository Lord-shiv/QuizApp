from rest_framework import generics
from .serializers import QuizSerializer, RandomQuestionSerializer, QuestionSerializer
from .models import Quiz, Question
from rest_framework.response import Response
from rest_framework.views import APIView


class Quiz(generics.ListAPIView):

    serializer_class = QuizSerializer
    queryset = Quiz.objects.all()


class RandomQuestion(APIView):

    def get(self, request, format=None, **kwargs):
        question = Question.objects.filter(
            quiz__title__iexact=kwargs['topic']).order_by('?')[:1]
        serializer = RandomQuestionSerializer(question, many=True)
        return Response(serializer.data)


class QuizQuestion(APIView):

    def get(self, request, format=None, **kwargs):
        quiz = Question.objects.filter(quiz__title__iexact=kwargs['topic'])
        serializer = QuestionSerializer(quiz, many=True)
        return Response(serializer.data)

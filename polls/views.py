from unittest import loader
from urllib import response
from django import template
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404


from .models import Question



def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    template = loader.get_template("polls/index.html")
    context = {"latest_question_list": latest_question_list,}
    return render(template.render(context, request))


def results(request, question_id):
    response = "you'r looking at the results of question %s."
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("you'r voting on %s." % question_id)


def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "polls/detail.html", {"question": question})
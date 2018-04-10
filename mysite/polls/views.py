#Views: "Type" of webpage in your django application
#In our POLL Applicaation- Question "index" page > dislplays latest few ques ; Question "detail" page > ques text no result but with a form of vote; Vote action; Question "result" page
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, get_object_or_404
from django.template import loader
# Create your views here.
from django.http import HttpResponse, Http404
from .models import Question

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    #output = ', '.join([q.question_text for q in latest_question_list])
    #return HttpResponse(output)
#long way-1    template = loader.get_template('polls/index.html')
    context={'latest_question_list': latest_question_list}
#long way-1    return HttpResponse(template.render(context,request))
    return render(request, 'polls/index.html', context)

def detail(request, question_id):
    #return HttpResponse("you're looking at question %s. " % question_id)
    ''' #long way
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404('Question does not exist')
    return render(request, 'polls/detail.html', {'question':question})
    '''
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html',{'question':question})

def results(request, question_id):
    response = "you're looking at the results of question %s. "
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("you're voting the question %s." % question_id)

#Views: "Type" of webpage in your django application
#In our POLL Applicaation- Question "index" page > dislplays latest few ques ; Question "detail" page > ques text no result but with a form of vote; Vote action; Question "result" page

from __future__ import unicode_literals
from django.shortcuts import render, get_object_or_404
from django.template import loader
from django.http import HttpResponse, Http404, HttpResponseRedirect
from .models import Question, Choice
from django.urls import reverse
from django.views import generic
from django.utils import timezone

#Create Views here
'''
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
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html',{'question':question})

def results(request, question_id):
    #return HttpResponse("you're looking at results of question %s." % question_id)
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/result.html', {'question':question})
'''
class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        #return Question.objects.order_by('-pub_date')[:5]
        return Question.objects.filter(
            pub_date__lte= timezone.now()
        ).order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name= 'polls/detail.html'
    def get_queryset(self):
        #Excludes any questions that aren't published yet.
        return Question.objects.filter(pub_date__lte=timezone.now())

class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'

def vote(request, question_id):
    '''return HttpResponse("you're voting the question %s." % question_id)'''
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, choice.DoesNotExist):
        return render(request, 'polls/detail.html',{
            'question': question,
            'error_message': "You didn't selected",
        })
    else:
        selected_choice.votes +=1
        selected_choice.save()
        #Always return as HttpResponseRedirect after successfully dealing with POST data.
        #This prevents data from being posted twice if a user hits the back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))

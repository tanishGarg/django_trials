from django.conf.urls import url

from . import views

app_name= 'polls'
urlpatterns = [
    url(r'^$',views.IndexView.as_view(), name='index'),
    url(r'^(?P<pk>[0-9]+)/$',views.DetailView.as_view(), name='detail'), #<int:question_id>
    url(r'^(?P<pk>[0-9]+)/results/$',views.ResultsView.as_view(), name='results'), #<int:question_id>/results/
    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'), #<int:question_id>/vote/
]
'''urlpatterns = [
    url(r'^$',views.index, name='index'),
    url(r'^(?P<question_id>[0-9]+)/$',views.detail, name='detail'), #<int:question_id>
    url(r'^(?P<question_id>[0-9]+)/results/$',views.results, name='results'), #<int:question_id>/results/
    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'), #<int:question_id>/vote/
]
'''

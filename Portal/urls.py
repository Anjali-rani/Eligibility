from django.conf.urls import url
from Portal import views
from django.contrib.auth import views as auth_views
app_name = 'Portal'

urlpatterns = [
    url(r'^create/$', views.AddQuestion.as_view(), name='create'),
    url(r'^$', views.QuestionList.as_view(), name='list'),
    # url(r'^home/$', views.home, name = 'home'),
    url(r'^result', views.result, name = 'result'),

    url(r'^(?P<choice>[\w]+)', views.questions, name = 'questions'),

]










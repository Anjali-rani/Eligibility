from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from . models import Questions,Scores,Student
from django.views.generic import TemplateView,CreateView,UpdateView,DeleteView,ListView,DetailView

# Create your views here.


def home(request, user_id=None):

    # choices = Questions. CAT_CHOICES
    # for ch in choices:
    #     if ch[0] == 'technical':
    #         return render(request, 'Portal/questions.html',)
    pass



def questions(request,choice):
    print(choice)
    # print(choice)
    # ques = Questions.objects.filter(category__exact = choice)
    # return render(request,'Portal/questions.html', {'ques':ques})

    tech_questions = Questions.objects.filter(category='technical').order_by('?')[0:25]
    apt_questions = Questions.objects.filter(category='aptitude').order_by('?')[0:25]
    questions_obj = tech_questions | apt_questions
    id_list = []
    for question_obj in questions_obj:
        id_list.append(question_obj.id)
    return render(request, 'Portal/questions.html', {'questions_obj': questions_obj})

def result(request,user_id=None):
    try:
        user = Student.objects.get(pk=user_id)
    except:
        print("result page")

    if request.method == 'POST':
        data = request.POST
        datas = dict(data)
        qid = []
        qans = []
        ans = []
        score = 0
        for key in datas:
            try:
                qid.append(int(key))
                qans.append(datas[key][0])
            except:
                print("Csrf")
        for q in qid:
            ans.append((Questions.objects.get(id = q)).answer)
        total = len(ans)
        for i in range(total):
            if ans[i] == qans[i]:
                score += 2

        print(score)
        qu = Scores(TotalMarks=score,)
        qu.save()
        return render(request,'Portal/result.html',{'score':score,})

class AddQuestion(CreateView):
    fields = ('category','question', 'optiona', 'optionb', 'optionc', 'optiond', 'answer', )
    model = Questions
    # success_url = reverse_lazy("TT:list")


class QuestionList(ListView):
    context_object_name = 'ques'
    model = Questions
    template_name = 'Portal/list.html'



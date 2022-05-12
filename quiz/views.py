from django.shortcuts import  render, redirect

from .models import *
from .forms import NewUserForm
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from .forms import *

# Create your views here.
def homepage(request):
	return render(request, "quiz/homepage.html")

def questionario(request):
	if request.method == 'POST':
		questions=Questionario.objects.all()
		print(request.POST)
		score=0
		wrong=0
		correct=0
		total=0
		for q in questions:
			total+=1
			print(q.id)
			print(request.POST.get(q.pergunta))
			print(q.resposta)
			print()
			if q.resposta == request.POST.get(q.pergunta):
				score+=10
				correct+=1
			else:
				wrong+=1
				score-=2
		print(score)
		print(total)
		percent = round(score / (total*10) * 100, 2)
		if percent < 0:
			percent = 0
		print(percent)
		context = {
			'score':score,
			'time':request.POST.get('timer'),
			'correct':correct,
			'wrong':wrong,
			'percent': percent,
			'total':total
		}
		return render(request, 'quiz/result.html', context)
	else:
		questions=Questionario.objects.all()
		#request.session['questions'] = questions
		context = {
            'questions':questions
        }
		return render(request,'quiz/questionario.html',context)

def ranking(request):
	ranking=Ranking.objects.all().order_by('-score')
	ranking=ranking[:10]
	return render(request, "quiz/ranking.html", {
		"ranking": ranking
	})

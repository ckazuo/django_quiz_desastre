from django.shortcuts import  render, redirect
from scipy import rand

from .models import *
from .forms import NewUserForm
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from .forms import *
import random

# Create your views here.
def homepage(request):
	return render(request, "quiz/homepage.html")

def questionario(request):
	if request.method == 'POST':
		questions=Questionario.objects.all()
		score=0
		wrong=int(request.POST.get('errado'))
		correct=int(request.POST.get('correto'))
		total=0
		point_right=15
		point_wrong=-1
		for q in questions:
			total+=1
		score = (wrong*point_wrong)+(correct*point_right) 
		print(score)
		print(total)
		percent = round(correct / total * 100, 2)
		if percent < 0:
			percent = 0
		print(percent)
		context = {
			'score':score,
			'time':request.POST.get('timer'),
			'correct':correct,
			'wrong':wrong,
			'percent': percent,
			'total':total,
			'form': uploadRanking(request.POST),
		}
		return render(request, 'quiz/result.html', context)
	else:
		questions=Questionario.objects.all()
		my_list = list(questions)
		random.shuffle(my_list)
		print(my_list)
		number = 1
		context = {
            'questions':my_list,
			'number'   :number
        }
		return render(request,'quiz/questionario.html',context)

def ranking(request):
	if request.POST:
		print(request)
		form = uploadRanking(request.POST)
		score = request.POST.get('score')
		print(f"User {request.POST.get('username')}")
		print(f"Scored {request.POST.get('score')}")
		if form.is_valid():
			name=request.POST.get('username')
			reg = Ranking(username = name, score = score)
			reg.save()
	ranking=Ranking.objects.all().order_by('-score')
	ranking=ranking[:10]
	return render(request, "quiz/ranking.html", {
		"ranking": ranking
	})

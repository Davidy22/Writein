from django.shortcuts import render, redirect
from .models import poll, entry
from .form import submitEntryForm, newPollForm
from .group import groupEntries
# Create your views here.

def index(request):
	form = newPollForm()
	return render(request, 'index.html', context={'form':form})

def polling(request,ID):
	pollIDFound = poll.objects.filter(id=ID).count()
	if pollIDFound == 0:
		return render(request, 'error.html')
		
	x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
	if x_forwarded_for:
		ip = x_forwarded_for.split(',')[0]
	else:
		ip = request.META.get('REMOTE_ADDR')
	
	if (entry.objects.filter(IP=ip,pollID=ID).count() > 0):
		entries = groupEntries(ID)
		question = poll.objects.filter(id=ID)[0].question
		return render(request, 'view.html', context={'entries':entries,'question':question})

	if request.method == 'POST':
		form = submitEntryForm(request.POST)
		
		if form.is_valid():
			entryField = form.cleaned_data['entryField']
			
			entry.objects.create(IP=ip,text=entryField,pollID=poll.objects.filter(id=ID)[0])
			entries = groupEntries(ID)
			if (len(entries) > 20):
				entries = entries[:19]
			return render(request, 'view.html', context={'entries':entries})
	else:
		form = submitEntryForm()


	question = poll.objects.filter(id=ID)[0].question
	return render(request, 'poll.html', context={'form':form,'question':question})

def create(request):
	form = newPollForm(request.POST)
	
	if form.is_valid():
		questionField = form.cleaned_data['questionField']
		temp = poll.objects.create(question=questionField)
		return redirect('/{0}'.format(temp.id))
	else:
		temp = poll.objects.create(question='')
		return redirect('/{0}'.format(temp.id))
	# add case for invalid question

from django.shortcuts import render, redirect
from .models import poll, entry
from .form import submitEntryForm
from .group import groupEntries
# Create your views here.

def index(request):
	return render(request, 'index.html')

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
		return render(request, 'view.html', context={'entries':entries})

	if request.method == 'POST':
		form = submitEntryForm(request.POST)
		
		if form.is_valid():
			entryField = form.cleaned_data['entryField']
			
			entry.objects.create(IP=ip,text=entryField,pollID=poll.objects.filter(id=ID)[0])
			entries = groupEntries(ID)
			return render(request, 'view.html', context={'entries':entries})
	else:
		form = submitEntryForm()

	entries = groupEntries(ID)
	if (len(entries) > 20):
		entries = entries[:19]
	return render(request, 'poll.html', context={'entries':entries, 'form':form})

def create(request):
	temp = poll.objects.create()
	return redirect('/{0}'.format(temp.id))

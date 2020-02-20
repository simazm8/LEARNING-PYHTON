from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import get_object_or_404, render
from .models import Note



def index(request):
    note_list = Note.objects.order_by('-pub_date')[:5]
    template = loader.get_template('polls/index.html')
    context = { 'note_list': note_list,}
    return render(request,'polls/index.html',context)

def details(request, note_id):
    try:
        note = Note.objects.get(id=note_id)
    except Note.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'polls/detail.html', {'note':note})

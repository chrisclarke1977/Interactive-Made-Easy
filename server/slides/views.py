from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext

from pymongo import Connection

from media_library.views import AddMediaForm, media_db
from slides.forms import SlideForm

connection = Connection()
slides_db = connection.ime.slides

def add_slide(request):
    if request.method == 'POST':
        form = SlideForm(request.POST)
        if form.is_valid():
            
            return HttpResponseRedirect(reverse('slide'))
    else:
        form = SlideForm()

    context = {
        'media_form': AddMediaForm(),
        'form': form,
        'files': media_db.find(),
    }
    return render_to_response('add_slide.html', context_instance=RequestContext(request, context))

def slide(request, id):
    slides_db.insert({'we': 2})

    context = {
        'text': '3333',
    }
    return render_to_response('slide.html')

def main_page(request):
    return render_to_response('main.html')

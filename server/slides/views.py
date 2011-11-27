from django.conf import settings
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext

from pymongo import Connection

from media_library.views import AddMediaForm, media_db
from slides.forms import SlideForm

connection = Connection()
slides_db = connection.ime.slides
slides_db.create_index('name', unique=True)

def add_slide(request, id):
    html = ''

    if request.method == 'POST':
        form = SlideForm(request.POST)
        if form.is_valid():

            data = {
                'name': form.cleaned_data['name'],
                'html': form.cleaned_data['html'],
            }
            slides_db.insert(data)
            return HttpResponseRedirect(reverse('slide', args=[data['name']]))
    else:
        form = SlideForm({'id': id})

    files = list(media_db.find())
    for fl in files:
        if fl['url'].startswith(settings.MEDIA_URL):
            fl['name_short'] = fl['name']
        else:
            fl['name_short'] = fl['name'].split('/')[-1]

    if id != '':
        html = slides_db.find_one({'name': id})['html']

    context = {
        'media_form': AddMediaForm(),
        'form': form,
        'files': files,
        'html': html,
    }
    return render_to_response('add_slide.html', context_instance=RequestContext(request, context))

def slide(request, id):
    html = slides_db.find_one({'name': id})['html']

    context = {
        'name': id,
        'html': html,
    }
    return render_to_response('slide.html', context_instance=RequestContext(request, context))

def main_page(request):
    return render_to_response('main.html', context_instance=RequestContext(request, {}))

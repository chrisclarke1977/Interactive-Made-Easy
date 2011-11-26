import os.path

from django.conf import settings
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext

from media_library.forms import AddMediaForm

from pymongo import Connection

connection = Connection()
media_db = connection.ime.media

# TODO: user folders for files
# TODO: uniqueness of file names
def add_media(request):
    if request.method == 'POST':
        form = AddMediaForm(request.POST, request.FILES)
        if form.is_valid():
            if form.cleaned_data['source'] == 'file':
                # TODO: check request.FILES['file'].content_type
                filename = request.FILES['file']._name
                f = open(os.path.join(settings.MEDIA_ROOT, 'files', filename), 'w')
                f.write(request.FILES['file'].read())

                media_db.insert({
                    'name': filename,
                    'media_type': form.cleaned_data['media_type'],
                    'url': settings.MEDIA_URL + 'files/' + filename,
                })
            else:
                media_db.insert({
                    'name': form.cleaned_data['url'],
                    'media_type': form.cleaned_data['media_type'],
                    'url': form.cleaned_data['url'],
                })

            #print media_db.find_one({'name': form.cleaned_data['name']})['url']

            return HttpResponseRedirect(reverse('media'))
    else:
        form = AddMediaForm()

    context = {
        'form': form,
        'files': media_db.find(),
    }
    return render_to_response('add_media.html', context_instance=RequestContext(request, context))

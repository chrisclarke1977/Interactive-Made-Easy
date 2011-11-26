import json

from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext

from pymongo import Connection

connection = Connection()
workflow_db = connection.ime.workflow
workflow_db.create_index('name', unique=True)

def add_workflow(request):
    workflows = list(workflow_db.find())
    for workflow in workflows:
        del workflow['_id']
    context = {
        'workflows': json.dumps(workflows),
    }
    print workflows
    return render_to_response('workflow.html', context_instance=RequestContext(request, context))

def ajax(request):
    print request.GET
    

    if request.GET.get('action', '') == 'create_workflow':
        workflow_db.insert({'name': request.GET['name'], 'slides': []})
        return HttpResponse('ok')

    elif request.GET.get('action', '') == 'rearrange':
        request.GET['positions']
        
        
        return HttpResponse('ok')
    elif request.GET.get('action', '') == 'delete':
        # TODO: delete slide
        return HttpResponse('ok')
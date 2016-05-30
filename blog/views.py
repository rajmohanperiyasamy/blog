from django.shortcuts import render_to_response
from django.template import RequestContext
from blog.models import *

def gale_task(request):
    data={}
    data['user']= request.user
    try:
        articles = Articles.objects.all().order_by('-publication_date')
        random_article=Articles.objects.all().order_by('?')[0]
        data['articles']= articles
        data['random_article']= random_article
    except:
        data={}
        pass
    
    return render_to_response('index3.html',data,context_instance=RequestContext(request))


def detail(request,pk=0):
    data={}
    try:
        article=Articles.objects.get(id=pk)
        data['article']= article
        articles = Articles.objects.all()
        data['articles']= articles
    except:
        data={}
        pass
 
    return render_to_response('detail.html',data,context_instance=RequestContext(request))
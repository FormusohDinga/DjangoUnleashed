from django.template import Context, loader
from django.http.response import (HttpResponse, Http404)
from django.shortcuts import (get_object_or_404, render_to_response)

from .models import Tag

def homepage(request):
    # tag_list = Tag.objects.all()
    # template = loader.get_template('organizer/tag_list.html')
    # context = Context({'tag_list': tag_list})
    # output = template.render(context)
    return render_to_response('organizer/tag_list.html', {'tag_list':Tag.objects.all()})

def tag_detail(request, slug):
    # template = loader.get_template('organizer/tag_detail.html')
    # context = Context({'tag':tag})
    # return HttpResponse(template.render(context))
    tag = get_object_or_404(Tag, slug__iexact = slug)
    return render_to_response('organizer/tag_detail', {'tag': tag})

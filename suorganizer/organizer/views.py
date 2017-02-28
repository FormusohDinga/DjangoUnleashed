from django.http.response import HttpResponse
from django.shortcuts import (get_object_or_404 ,redirect,render)
from django.template import RequestContext, loader
from django.views.generic import View

from .models import Tag, Startup
from .forms import TagForm

def tag_list(request):
    return render(request, 'organizer/tag_list.html',{'tag_list': Tag.objects.all()})

def tag_detail(request, slug):
    tag = get_object_or_404(Tag, slug__iexact = slug)
    return render(request, 'organizer/tag_detail.html', {'tag': tag})

def startup_list(request):
    return render(request, 'organizer/startup_list.html', {'startup_list': Startup.objects.all()})

def startup_detail(request,slug):
    startup = get_object_or_404(Startup, slug__iexact=slug)
    return render(request, 'organizer/startup_detail.html', {'startup':startup})

class TagCreate(View):
    form_class = TagForm
    template_name = 'organizer/tag_form.html'

    def get(self,request):
        return render(request,
                self.template_name,
                {'form': self.form_class()})

    def post(slef,request):
        bound_form = self.form_class(request.POST)
        if bound_form.is_valid():
            new_tag = bound_form.save()
            return redirect(new_tag)
        else:
            return render(request,
                            self.template_name,
                            {'form':bound_form})

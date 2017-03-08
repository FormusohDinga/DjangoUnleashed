from django.shortcuts import (
    get_object_or_404, render, redirect)
from django.core.urlresolvers import reverse_lazy, reverse
from django.views.generic import (DetailView, View, CreateView, DeleteView, ListView)
from core.utils import UpdateView
from django.core.paginator import (EmptyPage, PageNotAnInteger, Paginator)
from django.contrib.auth import PermissionDenied
from django.contrib.auth.decorators import (login_required, permission_required)
from django.utils.decorators import method_decorator

from user.decorators import (
    class_login_required,
    require_authenticated_permission)

from .forms import (
    NewsLinkForm, StartupForm, TagForm)
from .models import Startup, Tag, NewsLink

from .utils import PageLinksMixin


def in_contrib_group(user):
    print(user.groups)
    if user.groups.filter(name='contributors').exists():
        return True
    else:
        raise  PermissionDenied


class NewsLinkCreate( CreateView):
    form_class = NewsLinkForm
    template_name = 'organizer/newslink_form.html'
    model = NewsLink

class NewsLinkDelete(DeleteView):
    model = NewsLink

    def get_success_url(self):
        return (self.object.startup.get_absolute_url())

class NewsLinkUpdate(UpdateView):
    form_class = NewsLinkForm
    model = NewsLink


class StartupCreate( CreateView):
    form_class = StartupForm
    template_name = 'organizer/startup_form.html'
    model = Startup

@require_authenticated_permission('organizer.change_startup')
class StartupUpdate(UpdateView):
    form_class = StartupForm
    model = Startup

class StartupDelete(DeleteView):

    model = Startup
    success_url = reverse_lazy(
        'organizer_startup_list')


class StartupDetail(DetailView):
    model = Startup


class StartupList(PageLinksMixin, ListView):
    model = Startup
    paginate_by = 5

class TagList(PageLinksMixin, ListView):
    model = Tag
    paginate_by = 5


@require_authenticated_permission('organizer.add_tag')
class TagCreate(CreateView):
    form_class = TagForm
    template_name = 'organizer/tag_form.html'
    model = Tag

@require_authenticated_permission('organizer.change_tag')
class TagUpdate(UpdateView):
    form_class = TagForm
    model = Tag


class TagDelete(DeleteView):
    model = Tag
    success_url = reverse_lazy(
        'organizer_tag_list')

class TagDetail(DetailView):
    model = Tag


from django.shortcuts import render,redirect
from django.urls import reverse_lazy

# generic 함수를 import 하여 ListView: 디비list, Detail: 해당디비에서 아이디값으로 하나에 객체 을 가져옴.
from django.views.generic import ListView,DetailView,UpdateView,CreateView,DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from mysite.views import OwnerOnlyMixin
from photo.models import Album,Photo
from photo.forms import PhotoInlineFormSet


class AlbumLV(ListView):
    model = Album
class AlbumDV(DetailView):
    model = Album
class PhotoDV(DetailView):
    model = Photo

class PhotoChangeView(LoginRequiredMixin,ListView):
    model = Photo
    template_name = 'photo/photo_change_list.html'

    def get_queryset(self):
        return Photo.objects.filter(owner=self.request.user)

class PhotoCreateView(LoginRequiredMixin,CreateView):
    model = Photo
    fields = ['album','title','image','description']

    def form_valid(self,form):

        form.instance.owner = self.request.user
        return super().form_valid(form)
class PhotoUpdateView(OwnerOnlyMixin,UpdateView):
    model =Photo
    fields = ['album','title','image','description']
    success_url = reverse_lazy('photo:index')

class PhotoDeleteView(OwnerOnlyMixin,DeleteView):
    model=Photo
    success_url = reverse_lazy('photo:index')

class AlbumChangeView(LoginRequiredMixin,ListView):
    template_name = 'photo/album_change_list.html'
    def get_queryset(self):
        return Album.objects.filter(owner =self.request.user)

class AlbumDeleteView(LoginRequiredMixin,DeleteView):
    model=Album
    success_url=reverse_lazy('photo:index')

class AlbumCreateView(LoginRequiredMixin,CreateView):
    model= Album
    fields=['name','description']
    success_url = reverse_lazy('photo:index')

    def get_context_data(self, **kwargs):
        context =super().get_context_data(**kwargs) 
        if self.request.POST:
            context['formset'] = PhotoInlineFormSet(self.request.POST,self.request.FILES)            
        else:
            context['formset'] = PhotoInlineFormSet()            
        return context

    def form_valid(self,form):
        form.instance.owner =self.request.user
        context = self.get_context_data()
        formset = context['formset']
        for photoform in formset:
            photoform.instance.owner = self.request.user
        if formset.is_valid():
            self.object = form.save()
            formset.instance = self.object
            formset.save()
            return redirect(self.get_success_url())
        else:            
            return self.render_to_response(self.get_context_data(form=form))

class AlbumUpdateView(LoginRequiredMixin,UpdateView):
    model = Album
    fields=['name','description']
    success_url = reverse_lazy('photo:index')

    def get_context_data(self, **kwargs):
        context =super().get_context_data(**kwargs)
        if self.request.POST:
            context['formset'] = PhotoInlineFormSet(self.request.POST,self.request.FILES,instance=self.object)
        else:
            context['formset'] = PhotoInlineFormSet(instance=self.object)
        return context
    def form_valid(self,form):
        context = self.get_context_data()
        formset = context['formset']
        if formset.is_valid():
            self.object = form.save()#
            formset.instance = self.object #
            formset.save()
            return redirect(self.get_success_url())
        else:
            return self.render_to_response(self.get_context_data(form=form))

         
    




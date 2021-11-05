from django.shortcuts import render
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from bookmark.models import Bookmark
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from mysite.views import OwnerOnlyMixin

class BookmarkLV(ListView):
    model = Bookmark

class BookmarkDV(DetailView):
    model = Bookmark

class BookmarkCreateView(LoginRequiredMixin,CreateView):
    model = Bookmark #데이터을 넣을 테이블 설정
    fields = ['title','url'] #데이터 넣을 필드설정
    success_url = reverse_lazy('bookmark:index') # 성공했을떄 가는 url 설정
    def form_valid(self,form): # form 데이터 검증
        form.instance.owner = self.request.user # owner필드에 유저정보 insert
        return super().form_valid(form) # 상위에 데이터검증을 요청하고 완료되여 form.save() 호출

class BookmarkChangeView(LoginRequiredMixin,ListView):
    model = Bookmark
    template_name = 'bookmark/bookmark_change_list.html'
    def get_queryset(self):
        return Bookmark.objects.filter(owner=self.request.user)
class BookmarkUpdateView(OwnerOnlyMixin,UpdateView):
    model = Bookmark
    fields = ['title','url']        
    success_url=reverse_lazy('bookmark:index')

class BookmarkDeleteView(OwnerOnlyMixin,DeleteView):
    model =Bookmark
    success_url=reverse_lazy('bookmark:index')




# Create your views here.

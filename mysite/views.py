from django.views.generic import TemplateView

from django.views.generic import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.contrib.auth.mixins import AccessMixin

class HomeView(TemplateView):
    template_name ='home.html'

class UserCreateView(CreateView):
    template_name = 'registration/register.html'
    form_class=UserCreationForm
    success_url = reverse_lazy('register_done')

class UserCreateDoneTV(TemplateView):
    template_name = 'registration/register_done.html'

class OwnerOnlyMixin(AccessMixin):
    raise_exception =True
    permission_denied_message ="Owner only update/delete the object"
    
    def dispatch(self,request,*args,**kwargs): #해당 메소드을 호출할떄 dispatch메소드을 제일 처음으로 호출한다 dispatch는 get,post을 구분한다.ex)  (get,post)
        obj = self.get_object()
        if request.user != obj.owner: #해당객체에 owner와 로그인한유저에 정보가다르면 해당 구문을 탄다
            return self.handle_no_permission() #사용자에게 404,403 에러을 노출 시킴
        return super().dispatch(request,*args,**kwargs)
        

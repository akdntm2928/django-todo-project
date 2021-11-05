from django.urls import path
# from bookmark.views import BookmarkLV,BookmarkDV

from bookmark import views


app_name ='bookmark'
urlpatterns = [
    path('',views.BookmarkLV.as_view(),name='index'),#리스트
    path('<int:pk>/',views.BookmarkDV.as_view(),name='detail'), # 상세 
    path('add/',views.BookmarkCreateView.as_view(),name="add"),
    path('change/',views.BookmarkChangeView.as_view(),name="change"),
    path('<int:pk>/create/',views.BookmarkUpdateView.as_view(),name="update"),
    path('<int:pk>/delete/',views.BookmarkDeleteView.as_view(),name='delete')
]



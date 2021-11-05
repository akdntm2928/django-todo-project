from django.urls import path
from photo import views

app_name = 'photo'

urlpatterns=[
    path('',views.AlbumLV.as_view(),name='index'),
    path('album',views.AlbumLV.as_view(),name="album_list"),
    path('album/<int:pk>/',views.AlbumDV.as_view(),name="album_detail"),
    
    path('album/add/',views.AlbumCreateView.as_view(),name ='album_create'),
    path('album/change/',views.AlbumChangeView.as_view(),name="album_change"),
    path('album/<int:pk>/update/',views.AlbumUpdateView.as_view(),name="album_update"),
    path('album/<int:pk>/delete/',views.AlbumDeleteView.as_view(),name="album_delete"),

    path('photo/<int:pk>/',views.PhotoDV.as_view(),name="photo_detail"),
    path('photo/create/',views.PhotoCreateView.as_view(),name="photo_create"),
    path('photo/change/',views.PhotoChangeView.as_view(),name="photo_change"),
    path('photo/<int:pk>/update/',views.PhotoUpdateView.as_view(),name="photo_update"),
    path('photo/<int:pk>/delete/',views.PhotoDeleteView.as_view(),name="photo_delete"),
]
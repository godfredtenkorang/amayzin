from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path('sponsorship', views.sponsorship, name='sponsorship'),
    path('contact', views.contact, name='contact'),
    path('getinvolve', views.getinvolve, name='getinvolve'),
    path('watch', views.watch, name='watch'),
    path('news', views.news, name='news'),
    path('news_detail/<slug:news_slug>/', views.detail, name='detail'),
    path('photos', views.photos, name='photos'),
    path('galleryDetail/', views.galleryDetail, name='galleryDetail'),
    path('ghprojectPhotos/', views.ghprojectPhotos, name='ghprojectPhotos'),
    path('usaprojectPhotos/', views.usaprojectPhotos, name='usaprojectPhotos'),
    path('usaproject/', views.usaProject, name='usaproject'),
    path('ghanaproject/', views.ghProject, name='ghproject'),
]


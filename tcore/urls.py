from django.urls import path
from .views import IndexView,AboutView,ServicesView,BlogView,ContactView,BlogDetailView,CategoryDetailView,BlogSearchView,PageDetailView


urlpatterns=[
   path('',IndexView.as_view(),name='index'),
   path('about',AboutView.as_view(),name='about'),
   path('services',ServicesView.as_view(),name='services'),
   path('blog',BlogView.as_view(),name='blog'),
   path('blogs/<slug:slug>/',BlogDetailView.as_view(),name='blog-details'),
   path('category/<slug:slug>/',CategoryDetailView.as_view(),name='category-details'),
   path('search/',BlogSearchView.as_view(),name='blog-search'),
   path('contact',ContactView.as_view(),name='contact'),
   path('pages/<slug:slug>/',PageDetailView.as_view(),name='page-detail')


]
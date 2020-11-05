from . import views
#from django.urls import include
from django.urls import path
from .feeds import LatestPostsFeed

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path("feed/rss", LatestPostsFeed(), name="post_feed"),
    #path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'), #sufficient for post in only
    path('<slug:slug>/', views.post_detail, name='post_detail'),
    #path('upload/', views.upload)

]

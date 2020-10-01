from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('',views.home,name="home"),
    path('directory/<slug>',views.directory,name='directory'),
    path('addFolder',views.addFolder,name='addFolder'),
    path("addFile",views.addFile,name="addFile"),
    path("renameFile",views.renameFile,name="renameFile"),
    path("deleteFile",views.deleteFile,name="deleteFile"),
    path("deleteFolder",views.deleteFolder,name="deleteFolder"),
    path('videos',views.videos,name='videos'),
    path('music',views.music,name='music'),
    path('search',views.search,name='search'),
]

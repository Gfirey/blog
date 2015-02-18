#coding: utf-8
from django.conf.urls import patterns, include, url
from blog.views import PostsListView, PostDetailView
from django.contrib import admin
admin.autodiscover()  #функция автоматического обнаружения файлов admin.py в наших приложениях

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)), #URL админки http://имя_сайта/admin/
    url(r'^blog/$', PostsListView.as_view(), name='list'), # то есть по URL http://имя_сайта/blog/
                                               # будет выводиться список постов
    url(r'^blog/(?P<pk>\d+)/$', PostDetailView.as_view()), # а по URL http://имя_сайта/blog/число/
                                              # будет выводиться пост с определенным номером

)


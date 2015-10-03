from django.conf.urls import include, url
from django.contrib import admin
from blog import views

urlpatterns = [
    # Examples:
    url(r'^$', views.post_list, name='post_list'),
    url(r'^admin/', include(admin.site.urls)),
]

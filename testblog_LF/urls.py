from django.conf.urls import include, url
from django.urls import path
from django.contrib.auth import views
from django.contrib import admin
# admin.autodiscover()


import blog.views


urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^', include('blog.urls')),
    url(r'accounts/login/$',views.login,name='login'),
    url(r'accounts/logout/$',views.logout,name='logout',kwargs={'next_page':'/'}),
]

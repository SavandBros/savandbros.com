from django.conf.urls import url
from basement import views

urlpatterns = [
    url(r'^$', views.HomeView.as_view(), name='home'),
    url(r'^about/$', views.AboutView.as_view(), name='about'),
]

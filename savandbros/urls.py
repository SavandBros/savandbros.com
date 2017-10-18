from django.conf.urls import url, include

urlpatterns = [
    url(r'^', include('basement.urls', namespace='basement')),
]

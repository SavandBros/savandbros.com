from django.conf.urls import url

from planet import views

urlpatterns = [
    url(
        r'^process-grant-application/$',
        views.GrantFormProcessor.as_view(),
        name='process_grant_application',
    ),
]

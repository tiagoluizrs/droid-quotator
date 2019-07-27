from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^demands/$', views.DemandList.as_view(), name='demand-list'),
    url(r'^demand/(?P<pk>[0-9]+)/$', views.DemandDetail.as_view(), name='demand-detail'),
]
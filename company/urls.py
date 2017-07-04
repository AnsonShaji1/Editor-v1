from django.conf.urls import url,include
from company import views

urlpatterns = [
	url(r'^$',views.start,name='start'),
	url(r'^edit/(?P<pk>\d+)/',views.edit,name='edit'),
]